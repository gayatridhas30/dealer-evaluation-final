import urllib.request
import urllib.parse
import http.cookiejar
import json
import re

base_url = "http://127.0.0.1:8000"

# Create a cookie-aware opener
cookie_jar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))

# Get CSRF token from login page
print("=== GETTING CSRF TOKEN ===")
req = urllib.request.Request(f"{base_url}/admin/login/")
with opener.open(req) as response:
    html = response.read().decode('utf-8')
    csrf_match = re.search(r'name="csrfmiddlewaretoken" value="([^"]+)"', html)
    csrf_token = csrf_match.group(1) if csrf_match else "not found"
    print(f"CSRF Token: {csrf_token[:50]}...")

# Login
print("\n=== LOGIN ===")
login_data = urllib.parse.urlencode({
    'username': 'root',
    'password': 'admin123',
    'csrfmiddlewaretoken': csrf_token,
    'next': '/admin/'
}).encode('utf-8')
req = urllib.request.Request(f"{base_url}/admin/login/", data=login_data)
req.add_header('Referer', f"{base_url}/admin/login/")
req.add_header('Content-Type', 'application/x-www-form-urlencoded')
try:
    with opener.open(req) as response:
        print(f"Status: {response.status}")
        print(f"URL: {response.url}")
        if 'admin' in response.url and 'login' not in response.url:
            print("LOGIN SUCCESSFUL")
except Exception as e:
    print(f"Error: {e}")

# Check logged in
print("\n=== CHECKING LOGIN STATUS ===")
req = urllib.request.Request(f"{base_url}/admin/")
try:
    with opener.open(req) as response:
        html = response.read().decode('utf-8')
        if 'Log out' in html or 'logout' in html.lower():
            print("User is logged in - 'Log out' button visible")
        if 'root' in html:
            print("Username 'root' visible on page")
except Exception as e:
    print(f"Error: {e}")

# Get CSRF for logout
print("\n=== LOGOUT ===")
req = urllib.request.Request(f"{base_url}/admin/")
with opener.open(req) as response:
    html = response.read().decode('utf-8')
    csrf_match = re.search(r'name="csrfmiddlewaretoken" value="([^"]+)"', html)
    logout_csrf = csrf_match.group(1) if csrf_match else "not found"

logout_data = urllib.parse.urlencode({
    'csrfmiddlewaretoken': logout_csrf,
}).encode('utf-8')
req = urllib.request.Request(f"{base_url}/admin/logout/", data=logout_data)
req.add_header('Referer', f"{base_url}/admin/")
req.add_header('Content-Type', 'application/x-www-form-urlencoded')
try:
    with opener.open(req) as response:
        print(f"Status: {response.status}")
        html = response.read().decode('utf-8')
        if 'logged out' in html.lower() or 'Log in' in html:
            print("LOGOUT SUCCESSFUL - User logged out")
except Exception as e:
    print(f"Error: {e}")
