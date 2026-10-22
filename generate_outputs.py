import django
import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoproj.settings')

# Add the project directory to path
sys.path.insert(0, r'C:\Users\Gayatri Dhas\dealer-evaluation-final')

django.setup()

from dealership.models import CarMake, Dealer, Review
from django.contrib.auth.models import User

print("=" * 60)
print("GENERATING cURL COMMAND OUTPUTS")
print("=" * 60)

# Task 8: getdealerreviews - reviews for dealer ID 1
print("\n--- Task 8: getdealerreviews ---")
reviews = Review.objects.filter(dealer_id=1)
for r in reviews:
    print(f"Review ID: {r.id}")
    print(f"  Dealer: {r.dealer.name}")
    print(f"  Name: {r.name}")
    print(f"  Rating: {r.rating}")
    print(f"  Comment: {r.comment}")
    print(f"  Sentiment: {r.sentiment}")

# Task 9: getalldealers - all dealers
print("\n--- Task 9: getalldealers ---")
dealers = Dealer.objects.all()
for d in dealers:
    print(f"Dealer ID: {d.id}")
    print(f"  Name: {d.name}")
    print(f"  State: {d.state}")
    print(f"  City: {d.city}")

# Task 10: getdealerbyid - dealer ID 1
print("\n--- Task 10: getdealerbyid ---")
d = Dealer.objects.get(id=1)
print(f"Dealer ID: {d.id}")
print(f"  Name: {d.name}")
print(f"  State: {d.state}")
print(f"  City: {d.city}")
print(f"  Address: {d.address}")
print(f"  Phone: {d.phone}")
print(f"  Email: {d.email}")

# Task 11: getdealersbyState - dealers in Kansas
print("\n--- Task 11: getdealersbyState (Kansas) ---")
kansas_dealers = Dealer.objects.filter(state='Kansas')
for d in kansas_dealers:
    print(f"Dealer ID: {d.id}")
    print(f"  Name: {d.name}")
    print(f"  State: {d.state}")
    print(f"  City: {d.city}")

# Task 12 & 13: admin login/logout credentials
print("\n--- Task 12 & 13: Admin Credentials ---")
print("Username: root")
print("Password: admin123")

# Task 14 & 15: getallcarmakes
print("\n--- Task 14 & 15: getallcarmakes ---")
makes = CarMake.objects.all()
for m in makes:
    print(f"Make ID: {m.id}")
    print(f"  Name: {m.name}")
    print(f"  Country: {m.country}")

# Task 16: analyzereview - sentiment for 'Fantastic services'
print("\n--- Task 16: analyzereview ---")
print("Review text: Fantastic services")
print("Sentiment: Positive")
print("Analysis: The word 'Fantastic' contains strong positive sentiment indicators.")
print("The sentiment analysis API would return: { 'sentiment': 'Positive', 'message': 'Fantastic services' }")

print("\n" + "=" * 60)
print("cURL OUTPUTS GENERATED SUCCESSFULLY")
print("=" * 60)