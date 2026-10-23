from django.db import models


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name='models')
    name = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.make.name} {self.name} ({self.year})"


class Dealer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=50, blank=True)
    full_name = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    address = models.TextField(blank=True)
    zip = models.CharField(max_length=10, blank=True)
    lat = models.FloatField(default=0.0)
    long = models.FloatField(default=0.0)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.state})"


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    comment = models.TextField()
    sentiment = models.CharField(max_length=50, blank=True)
    purchase = models.CharField(max_length=100, blank=True)
    purchase_date = models.CharField(max_length=50, blank=True)
    car_make = models.CharField(max_length=100, blank=True)
    car_model = models.CharField(max_length=100, blank=True)
    car_year = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.dealer.name}"
