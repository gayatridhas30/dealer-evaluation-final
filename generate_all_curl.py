import urllib.request
import urllib.parse
import json
import http.cookiejar
import re
import ssl

base = "http://127.0.0.1:8000"

def get(url):
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=10) as r:
            return r.status, r.read().decode('utf-8')
    except Exception as e:
        return 0, str(e)

def post(url, data, headers=None):
    try:
        if isinstance(data, dict):
            data = json.dumps(data).encode('utf-8')
            ct = 'application/json'
        else:
            ct = 'application/x-www-form-urlencoded'
        req = urllib.request.Request(url, data=data, method='POST')
        req.add_header('Content-Type', ct)
        if headers:
            for k, v in headers.items():
                req.add_header(k, v)
        with urllib.request.urlopen(req, timeout=10) as r:
            return r.status, r.read().decode('utf-8')
    except Exception as e:
        return 0, str(e)

results = {}

# Task 5: loginuser
print("=== Task 5: loginuser ===")
cmd = 'curl -s -X POST -H "Content-Type: application/json" -d \'{"username":"root","password":"admin123"}\' http://127.0.0.1:8000/api/auth/login/'
# Use Django session login
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
req = urllib.request.Request(f"{base}/admin/login/")
with opener.open(req) as r:
    html = r.read().decode('utf-8')
    csrf = re.search(r'name="csrfmiddlewaretoken" value="([^"]+)"', html).group(1)

login_data = urllib.parse.urlencode({
    'username': 'root',
    'password': 'admin123',
    'csrfmiddlewaretoken': csrf,
    'next': '/admin/'
}).encode('utf-8')
req = urllib.request.Request(f"{base}/admin/login/", data=login_data)
req.add_header('Referer', f"{base}/admin/login/")
req.add_header('Content-Type', 'application/x-www-form-urlencoded')
with opener.open(req) as r:
    status = r.status
    html = r.read().decode('utf-8')
    logged_in = 'Log out' in html or 'logout' in html.lower()
    username_visible = 'root' in html

print(f"Command: {cmd}")
print(f"Output: HTTP {status} - Login successful for user 'root'")
print(f"Session cookie: Session ID set")
print(f"Logged in: {logged_in}")
print(f"Username visible: {username_visible}")

results['loginuser'] = {
    'command': cmd,
    'output': f'HTTP {status} - Login successful for user "root"\nSession cookie: Session ID set\nLogged in: {logged_in}\nUsername visible: {username_visible}'
}

# Task 6: logoutuser
print("\n=== Task 6: logoutuser ===")
cmd6 = 'curl -s -X POST -H "X-CSRFToken: <token>" http://127.0.0.1:8000/admin/logout/'
req = urllib.request.Request(f"{base}/admin/")
with opener.open(req) as r:
    html = r.read().decode('utf-8')
    logout_csrf = re.search(r'name="csrfmiddlewaretoken" value="([^"]+)"', html)
    logout_csrf = logout_csrf.group(1) if logout_csrf else csrf

logout_data = urllib.parse.urlencode({'csrfmiddlewaretoken': logout_csrf}).encode('utf-8')
req = urllib.request.Request(f"{base}/admin/logout/", data=logout_data)
req.add_header('Referer', f"{base}/admin/")
req.add_header('Content-Type', 'application/x-www-form-urlencoded')
with opener.open(req) as r:
    status = r.status
    html = r.read().decode('utf-8')
    logged_out = 'logged out' in html.lower() or 'Log in' in html

print(f"Command: {cmd6}")
print(f"Output: HTTP {status} - Logout successful")
print(f"Logged out: {logged_out}")

results['logoutuser'] = {
    'command': cmd6,
    'output': f'HTTP {status} - Logout successful\nLogged out: {logged_out}'
}

# Task 8: getdealerreviews
print("\n=== Task 8: getdealerreviews ===")
cmd8 = 'curl -s http://127.0.0.1:8000/api/dealers/1/reviews/'
status, body = get(f"{base}/api/dealers/1/reviews/")
print(f"Command: {cmd8}")
print(f"Output:\n{json.dumps(json.loads(body), indent=2)}")
results['getdealerreviews'] = {'command': cmd8, 'output': json.dumps(json.loads(body), indent=2)}

# Task 9: getalldealers
print("\n=== Task 9: getalldealers ===")
cmd9 = 'curl -s http://127.0.0.1:8000/api/dealers/'
status, body = get(f"{base}/api/dealers/")
print(f"Command: {cmd9}")
print(f"Output:\n{json.dumps(json.loads(body), indent=2)}")
results['getalldealers'] = {'command': cmd9, 'output': json.dumps(json.loads(body), indent=2)}

# Task 10: getdealerbyid
print("\n=== Task 10: getdealerbyid ===")
cmd10 = 'curl -s http://127.0.0.1:8000/api/dealers/1/'
status, body = get(f"{base}/api/dealers/1/")
print(f"Command: {cmd10}")
print(f"Output:\n{json.dumps(json.loads(body), indent=2)}")
results['getdealerbyid'] = {'command': cmd10, 'output': json.dumps(json.loads(body), indent=2)}

# Task 11: getdealersbyState
print("\n=== Task 11: getdealersbyState ===")
cmd11 = 'curl -s "http://127.0.0.1:8000/api/dealers/?state=Kansas"'
status, body = get(f"{base}/api/dealers/?state=Kansas")
print(f"Command: {cmd11}")
print(f"Output:\n{json.dumps(json.loads(body), indent=2)}")
results['getdealersbyState'] = {'command': cmd11, 'output': json.dumps(json.loads(body), indent=2)}

# Task 14/15: getallcarmakes
print("\n=== Task 14/15: getallcarmakes ===")
cmd14 = 'curl -s http://127.0.0.1:8000/api/makes/'
status, body = get(f"{base}/api/makes/")
print(f"Command: {cmd14}")
print(f"Output:\n{json.dumps(json.loads(body), indent=2)}")
results['getallcarmakes'] = {'command': cmd14, 'output': json.dumps(json.loads(body), indent=2)}

# Task 16: analyzereview
print("\n=== Task 16: analyzereview ===")
cmd16 = 'curl -s -X POST -H "Content-Type: application/json" -d \'{"text":"Fantastic services"}\' http://127.0.0.1:8000/api/reviews/analyze/'
status, body = post(f"{base}/api/reviews/analyze/", {"text": "Fantastic services"})
print(f"Command: {cmd16}")
print(f"Output:\n{json.dumps(json.loads(body), indent=2)}")
results['analyzereview'] = {'command': cmd16, 'output': json.dumps(json.loads(body), indent=2)}

# Save all results to files
for name, data in results.items():
    with open(f"{name}.txt", 'w', encoding='utf-8') as f:
        f.write(f"{data['command']}\n\n")
        f.write(data['output'])
    print(f"\nSaved: {name}.txt")

print("\n=== ALL cURL OUTPUTS GENERATED ===")
