# Dealer Evaluation - RUNBOOK (do everything in IBM Cloud Shell)

Open **https://cloud.shell.ibm.com** and log in with the IBM Cloud account you use for the
course/labs. Upload this whole `dealer-evaluation-final` folder into Cloud Shell (Cloud Shell
**Upload** button), then:

```bash
cd dealer-evaluation-final
bash deploy.sh
```

That script does **everything** (deploy all three microservices and wire the frontend to the
live URLs). Follow the steps below to know **when to take each screenshot**.

---

## Screenshot filenames and where to take them

| # | File to save | What the screenshot must show | Points |
|---|--------------|-------------------------------|--------|
| 1 | `product_details_deploy.png` | Code Engine **Application** `products` = Ready, plus its URL | 2 |
| 2 | `dealer_details_deploy.png` | Code Engine **Application** `dealers` = Ready, plus its URL | 2 |
| 3 | `git_clone.png` | Terminal showing the frontend repo cloned | 1 |
| 4 | `index_urlchanges.png` | `index.html` with the two deployed URLs (not localhost) | 2 |
| 5 | `frontend_deploy.png` | Code Engine **Application** `frontend` = Ready, plus its URL | 2 |
| 6 | `homepage.png` | Homepage with products preloaded in the dropdown | 2 |
| 7 | `product_dealer.png` | A product selected -> dealers supplying it listed | 1 |
| 8 | `product_dealer_price.png` | A dealer selected -> its price for that product | 1 |
| 9 | `product_all_dealers_price.png` | "All Dealers" selected -> price table for every dealer | 2 |
| | | **Total** | **15** |

---

## Task 3 - clone the frontend repo (do this BEFORE running deploy.sh)

In Cloud Shell:

```bash
git clone https://github.com/ibm-developer-skills-network/dealer_evaluation_frontend.git
ls dealer_evaluation_frontend
```

Take `git_clone.png` of that terminal output.

Then copy the ready-made files on top so you work from one folder:

```bash
cp -r dealer_evaluation_frontend/* dealer-evaluation-final/frontend/ 2>/dev/null || true
```

> Note: the `frontend/` folder already in this package **is** that repo (same files), so you
> can skip the copy if you already ran `bash deploy.sh`.

---

## Tasks 1 & 2 - product details (Python) + dealer pricing (Node.js)

`deploy.sh` builds, pushes and deploys both. Watch for these lines:

```
PRODUCTS_URL = https://products.<id>.us-south.codeengine.appdomain.cloud
DEALERS_URL  = https://dealers.<id>.us-south.codeengine.appdomain.cloud
```

To make the screenshots obvious, run:

```bash
ibmcloud ce application list
ibmcloud ce application get --name products -o yaml   # shows Ready + URL
ibmcloud ce application get --name dealers  -o yaml
```

Screenshot the **Code Engine -> Applications** page showing both apps `Ready` and their URLs.
That is `product_details_deploy.png` and `dealer_details_deploy.png`.

---

## Task 4 - point index.html at the deployed URLs

This is done automatically by `deploy.sh`. To show the change, run:

```bash
grep -n "let produrl\|let dealerurl" dealer-evaluation-final/frontend/html/index.html
```

Expected:

```
let produrl = "https://products.<id>.us-south.codeengine.appdomain.cloud/"
let dealerurl = "https://dealers.<id>.us-south.codeengine.appdomain.cloud/"
```

Take `index_urlchanges.png` of that output (or open the file in the editor and screenshot it).

---

## Task 5 - deploy the frontend

`deploy.sh` deploys it. Verify and screenshot:

```bash
ibmcloud ce application get --name frontend -o yaml
```

Shows `Ready` + URL -> `frontend_deploy.png`.

---

## Tasks 6, 7, 8, 9 - use the live app

Open the printed `FRONTEND_URL` in your browser:

1. **homepage.png** - the dropdown already shows Headphones, Laptop, Mouse, Printer (no click needed).
2. **product_dealer.png** - pick e.g. **Headphones** -> the second dropdown lists Binglee, DXC
   Electronics, Bobay (+ "All Dealers").
3. **product_dealer_price.png** - pick a single dealer, e.g. **Binglee** -> text like
   `Headphones costs $30 at Binglee` appears.
4. **product_all_dealers_price.png** - pick **All Dealers** -> a table of every dealer's price.

---

## Troubleshooting

- `registry-secret` not found -> `ibmcloud ce registry create --name icr-secret --server us.icr.io --password <IAM_API_KEY>`
- App stays not Ready -> `ibmcloud ce application logs --name products` (same for dealers/frontend)
- Empty dropdown -> the frontend is still pointing at `localhost`; re-run the `sed` lines from
  Task 4 and rebuild, or check that the products app URL is correct.
- Update an app after code change:
  ```bash
  ibmcloud ce application update --name frontend --image us.icr.io/<NS>/frontend:v1 --registry-secret icr-secret
  ```
