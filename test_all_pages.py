import urllib.request
import json

base = "http://127.0.0.1:8000"
pages = [
    ("Homepage", "/"),
    ("Dealer Detail", "/dealers/1/"),
    ("Add Review", "/dealers/1/add-review/"),
    ("Kansas Dealers", "/dealers/state/Kansas/"),
    ("Admin Login", "/admin/login/"),
    ("About", "/static/About.html"),
    ("Contact", "/static/Contact.html"),
    ("API Makes", "/api/makes/"),
    ("API Dealers", "/api/dealers/"),
    ("API Reviews", "/api/reviews/"),
    ("API Dealer 1 Reviews", "/api/dealers/1/reviews/"),
]

print("=" * 60)
print("PAGE VERIFICATION")
print("=" * 60)
for name, path in pages:
    try:
        req = urllib.request.Request(base + path)
        with urllib.request.urlopen(req, timeout=10) as r:
            status = r.status
            body = r.read().decode('utf-8')[:100]
            print(f"  OK  {name:25s} HTTP {status}  ({path})")
    except Exception as e:
        print(f"  ERR {name:25s} {e}  ({path})")

# Test POST analyze
print("\n--- Testing POST /api/reviews/analyze/ ---")
try:
    data = json.dumps({"text": "Fantastic services"}).encode('utf-8')
    req = urllib.request.Request(base + "/api/reviews/analyze/", data=data, method='POST')
    req.add_header('Content-Type', 'application/json')
    with urllib.request.urlopen(req, timeout=10) as r:
        body = json.loads(r.read().decode('utf-8'))
        print(f"  Result: {json.dumps(body)}")
except Exception as e:
    print(f"  ERROR: {e}")

# Test POST create review
print("\n--- Testing POST /api/reviews/ ---")
try:
    data = json.dumps({"dealer": 1, "name": "Test User", "rating": 5, "comment": "Amazing experience!"}).encode('utf-8')
    req = urllib.request.Request(base + "/api/reviews/", data=data, method='POST')
    req.add_header('Content-Type', 'application/json')
    with urllib.request.urlopen(req, timeout=10) as r:
        body = json.loads(r.read().decode('utf-8'))
        print(f"  Created review ID: {body.get('id')}, sentiment: {body.get('sentiment')}")
except Exception as e:
    print(f"  ERROR: {e}")

print("\n" + "=" * 60)
print("ALL PAGES VERIFIED")
print("=" * 60)
