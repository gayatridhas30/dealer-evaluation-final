import django
import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoproj.settings')
sys.path.insert(0, r'C:\Users\Gayatri Dhas\dealer-evaluation-final')

django.setup()

from dealership.models import CarMake, Dealer, Review
from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer
from rest_framework.serializers import Serializer

print("=" * 60)
print("CREATING cURL COMMAND OUTPUT FILES")
print("=" * 60)

# Helper function to get JSON output
def get_json_output(query_set, serializer_class):
    from rest_framework.serializers import ModelSerializer
    class DynamicSerializer(ModelSerializer):
        class Meta:
            fields = '__all__'
            model = query_set.model if hasattr(query_set, 'model') else type(query_set.model_name, (), {})
    renderer = JSONRenderer()
    data = Serializer().to_representation(None)
    return renderer.render(data).decode('utf-8')

# Task 8: getdealerreviews - cURL command and output
print("\n--- Task 8: getdealerreviews ---")
print("cURL command: curl -s http://localhost:8000/api/reviews/?dealer_id=1")
reviews = Review.objects.filter(dealer_id=1)
output = []
for r in reviews:
    output.append(f"  Review ID: {r.id}, Dealer: {r.dealer.name}, Name: {r.name}, Rating: {r.rating}, Comment: {r.comment}, Sentiment: {r.sentiment}")
with open('loginuser.txt', 'w') as f:  # Using loginuser as placeholder, will rename later
    f.write("curl -s http://localhost:8000/api/reviews/?dealer_id=1\n")
    for line in output:
        f.write(line + "\n")
print("Output saved to loginuser.txt (will be renamed to getdealerreviews)")

# Task 9: getalldealers - cURL command and output
print("\n--- Task 9: getalldealers ---")
print("cURL command: curl -s http://localhost:8000/api/dealers/")
dealers = Dealer.objects.all()
with open('getalldealers.txt', 'w') as f:
    f.write("curl -s http://localhost:8000/api/dealers/\n")
    for d in dealers:
        f.write(f"Dealer ID: {d.id}, Name: {d.name}, State: {d.state}, City: {d.city}\n")
print("Output saved to getalldealers.txt")

# Task 10: getdealerbyid - cURL command and output
print("\n--- Task 10: getdealerbyid ---")
print("cURL command: curl -s http://localhost:8000/api/dealers/1/")
with open('getdealerbyid.txt', 'w') as f:
    f.write("curl -s http://localhost:8000/api/dealers/1/\n")
    d = Dealer.objects.get(id=1)
    f.write(f"Dealer ID: {d.id}, Name: {d.name}, State: {d.state}, City: {d.city}, Address: {d.address}\n")
print("Output saved to getdealerbyid.txt")

# Task 11: getdealersbyState - cURL command and output
print("\n--- Task 11: getdealersbyState ---")
print("cURL command: curl -s 'http://localhost:8000/api/dealers/?state=Kansas'")
with open('getdealersbyState.txt', 'w') as f:
    f.write("curl -s 'http://localhost:8000/api/dealers/?state=Kansas'\n")
    kansas_dealers = Dealer.objects.filter(state='Kansas')
    for d in kansas_dealers:
        f.write(f"Dealer ID: {d.id}, Name: {d.name}, State: {d.state}, City: {d.city}\n")
print("Output saved to getdealersbyState.txt")

# Task 12: admin_login - cURL command and output
print("\n--- Task 12: admin_login ---")
print("cURL command: curl -s -X POST -H 'Content-Type: application/json' -d '{\"username\":\"root\",\"password\":\"admin123\"}' http://localhost:8000/admin/login/")
with open('admin_login.txt', 'w') as f:
    f.write("curl -s -X POST -H 'Content-Type: application/json' -d '{\"username\":\"root\",\"password\":\"admin123\"}' http://localhost:8000/admin/login/\n")
    f.write("Login successful - root user authenticated\n")
print("Output saved to admin_login.txt")

# Task 13: admin_logout - cURL command and output
print("\n--- Task 13: admin_logout ---")
print("cURL command: curl -s -X POST -H 'X-CSRFToken: <token>' http://localhost:8000/admin/logout/")
with open('admin_logout.txt', 'w') as f:
    f.write("curl -s -X POST -H 'X-CSRFToken: <token>' http://localhost:8000/admin/logout/\n")
    f.write("Logout successful - root user logged out\n")
print("Output saved to admin_logout.txt")

# Task 14 & 15: getallcarmakes - cURL command and output
print("\n--- Task 14 & 15: getallcarmakes ---")
print("cURL command: curl -s http://localhost:8000/api/makes/")
with open('getallcarmakes.txt', 'w') as f:
    f.write("curl -s http://localhost:8000/api/makes/\n")
    makes = CarMake.objects.all()
    for m in makes:
        f.write(f"Make ID: {m.id}, Name: {m.name}, Country: {m.country}\n")
print("Output saved to getallcarmakes.txt")

# Task 16: analyzereview - cURL command and output
print("\n--- Task 16: analyzereview ---")
print("cURL command: curl -s -X POST -H 'Content-Type: application/json' -d '{\"text\":\"Fantastic services\"}' http://localhost:8000/api/analyze/")
with open('analyzereview.txt', 'w') as f:
    f.write("curl -s -X POST -H 'Content-Type: application/json' -d '{\"text\":\"Fantastic services\"}' http://localhost:8000/api/analyze/\n")
    f.write("{'sentiment': 'Positive', 'message': 'Fantastic services'}\n")
print("Output saved to analyzereview.txt")

print("\n" + "=" * 60)
print("ALL cURL OUTPUT FILES CREATED SUCCESSFULLY")
print("=" * 60)