# Dealer Evaluation - Final Project Submission (15 marks)

Project: multi-service **Dealer Evaluation** app deployed to IBM Cloud Code Engine.
Track: **Python Labs (Option A)**.

## Repos

| Service | Language | Repo |
|---------|----------|------|
| Product Details | Python (Flask) | `products_list/` (from `ibm-developer-skills-network/dealer_evaluation_backend`) |
| Dealer Pricing | Node.js (Express) | `dealer_details/` (from `ibm-developer-skills-network/dealer_evaluation_backend`) |
| Dealer Evaluation Frontend | Python (Flask, static HTML) | `frontend/` (from `ibm-developer-skills-network/dealer_evaluation_frontend`) |

Backend source: https://github.com/ibm-developer-skills-network/dealer_evaluation_backend
Frontend source: https://github.com/ibm-developer-skills-network/dealer_evaluation_frontend

## Files to upload (one screenshot per task, exact filenames)

| Task | Filename | Evidence | Points |
|------|----------|----------|--------|
| 1 | `product_details_deploy.png` | Products microservice deployed on Code Engine (Ready + URL) | 2 |
| 2 | `dealer_details_deploy.png` | Dealer pricing microservice deployed on Code Engine (Ready + URL) | 2 |
| 3 | `git_clone.png` | Frontend repo cloned from the provided Git URL | 1 |
| 4 | `index_urlchanges.png` | `index.html` placeholders replaced with deployed URLs | 2 |
| 5 | `frontend_deploy.png` | Frontend microservice deployed on Code Engine (Ready + URL) | 2 |
| 6 | `homepage.png` | Homepage with products preloaded in the dropdown | 2 |
| 7 | `product_dealer.png` | Selected product -> dealers supplying it listed | 1 |
| 8 | `product_dealer_price.png` | Selected dealer -> price shown | 1 |
| 9 | `product_all_dealers_price.png` | "All Dealers" -> price table for all dealers | 2 |
| | | **Total** | **15** |

## One-command deploy

In IBM Cloud Shell:

```bash
cd dealer-evaluation-final
bash deploy.sh
```

It builds, pushes and deploys all three services and rewrites `frontend/html/index.html` with
the live URLs. See `RUNBOOK.md` for the exact moment to take each screenshot.

## Code that was changed

`frontend/html/index.html` lines:

```js
let produrl   = "https://products.<id>.us-south.codeengine.appdomain.cloud/"
let dealerurl = "https://dealers.<id>.us-south.codeengine.appdomain.cloud/"
```

(replacing the template's `http://localhost:5000/` and `http://localhost:8080/`).

## API endpoints

| Method | URL | Service |
|--------|-----|---------|
| GET | `/products` | products_list |
| GET | `/getdealers/<product>` | products_list |
| GET | `/price/<dealer>/<product>` | dealer_details |
| GET | `/allprice/<product>` | dealer_details |
| GET | `/` | frontend (index.html) |
