import os
import sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoproj.settings')
sys.path.insert(0, r'C:\Users\Gayatri Dhas\dealer-evaluation-final')
import django
django.setup()
from dealership.models import Review
for r in Review.objects.all():
    if r.rating >= 4:
        r.sentiment = 'Positive'
    elif r.rating <= 2:
        r.sentiment = 'Negative'
    else:
        r.sentiment = 'Neutral'
    r.save()
    print(f"Review {r.id}: {r.name} - {r.rating} stars - {r.sentiment}")
print("Done updating sentiments")
