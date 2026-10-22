#!/usr/bin/env bash
# Dealer Evaluation - one-shot deploy to IBM Cloud Code Engine
# Run this inside IBM Cloud Shell (https://cloud.shell.ibm.com), in this folder.
set -e

REGION=us-south
PROJECT=dealer-eval

echo "=== 1. Login ==="
ibmcloud login -r "$REGION"

# --- find an IBM Cloud Container Registry namespace ---
NS=$(ibmcloud cr namespaces 2>/dev/null | grep 'sn-labs-' | head -n1 | tr -d ' \r')
if [ -z "$NS" ]; then
  NS=$(ibmcloud cr namespaces 2>/dev/null | awk 'NR>2 {print $1}' | head -n1 | tr -d ' \r')
fi
if [ -z "$NS" ]; then
  NS=my-namespace
  ibmcloud cr namespace-add "$NS" || true
fi
echo "ICR namespace = $NS"

# --- Code Engine project ---
ibmcloud ce project create --name "$PROJECT" --region "$REGION" || true
ibmcloud ce project select --name "$PROJECT"

# --- docker credentials for ICR ---
eval "$(ibmcloud cr docker-config --quiet)"

REG_SECRET=icr-secret
ibmcloud ce registry get --name "$REG_SECRET" >/dev/null 2>&1 || \
  ibmcloud ce registry create --name "$REG_SECRET" --server us.icr.io --password "$IAM_API_KEY"

# ================= 2. PRODUCT DETAILS (Python) =================
echo "=== 2. Building products_list ==="
cd products_list
docker build -t us.icr.io/$NS/products:v1 .
docker push us.icr.io/$NS/products:v1
ibmcloud ce application create --name products \
  --image us.icr.io/$NS/products:v1 --port 5000 --registry-secret "$REG_SECRET"
PRODUCTS_URL=$(ibmcloud ce application get --name products -o url | tr -d '\r')
echo "PRODUCTS_URL = $PRODUCTS_URL"
cd ..

# ================= 3. DEALER PRICING (Node.js) =================
echo "=== 3. Building dealer_details ==="
cd dealer_details
docker build -t us.icr.io/$NS/dealers:v1 .
docker push us.icr.io/$NS/dealers:v1
ibmcloud ce application create --name dealers \
  --image us.icr.io/$NS/dealers:v1 --port 8080 --registry-secret "$REG_SECRET"
DEALERS_URL=$(ibmcloud ce application get --name dealers -o url | tr -d '\r')
echo "DEALERS_URL = $DEALERS_URL"
cd ..

# ================= 4. FRONTEND =================
echo "=== 4. Wiring frontend to deployed URLs ==="
cd frontend
sed -i "s|http://localhost:5000/|${PRODUCTS_URL}/|" html/index.html
sed -i "s|http://localhost:8080/|${DEALERS_URL}/|" html/index.html
grep -n "let produrl\|let dealerurl" html/index.html
docker build -t us.icr.io/$NS/frontend:v1 .
docker push us.icr.io/$NS/frontend:v1
ibmcloud ce application create --name frontend \
  --image us.icr.io/$NS/frontend:v1 --port 5001 --registry-secret "$REG_SECRET"
FRONTEND_URL=$(ibmcloud ce application get --name frontend -o url | tr -d '\r')
cd ..

echo
echo "=================================================="
echo "PRODUCTS_URL  = $PRODUCTS_URL"
echo "DEALERS_URL   = $DEALERS_URL"
echo "FRONTEND_URL  = $FRONTEND_URL"
echo "Open FRONTEND_URL in a browser to get the homepage screenshot."
echo "=================================================="
