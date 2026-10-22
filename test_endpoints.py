import urllib.request
import urllib.parse
import json
import ssl

base_url = "http://127.0.0.1:8000"

def make_get(url):
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        return str(e)

def make_post(url, data):
    try:
        json_data = json.dumps(data).encode('utf-8')
        req = urllib.request.Request(url, data=json_data, method='POST')
        req.add_header('Content-Type', 'application/json')
        with urllib.request.urlopen(req) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        return str(e)

# Test analyze endpoint
print("=== ANALYZE ===")
result = make_post(f"{base_url}/api/reviews/analyze/", {"text": "Fantastic services"})
print(result)

# Test create review
print("\n=== CREATE REVIEW ===")
result = make_post(f"{base_url}/api/reviews/", {
    "dealer": 1,
    "name": "John Doe",
    "rating": 5,
    "comment": "Fantastic services"
})
print(result)
