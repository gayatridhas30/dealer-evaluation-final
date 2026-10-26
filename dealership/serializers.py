from rest_framework import serializers
from .models import CarMake, CarModel, Dealer, Review


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ['id', 'name', 'year']


class CarMakeSerializer(serializers.ModelSerializer):
    models = CarModelSerializer(many=True, read_only=True)

    class Meta:
        model = CarMake
        fields = ['id', 'name', 'country', 'models']


class DealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealer
        fields = ['id', 'name', 'short_name', 'full_name', 'city', 'state',
                  'address', 'zip', 'lat', 'long', 'phone', 'email', 'website']


class ReviewSerializer(serializers.ModelSerializer):
    review = serializers.CharField(source='comment', read_only=True)
    dealership = serializers.IntegerField(source='dealer_id', read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'dealer', 'dealership', 'name', 'rating', 'comment', 'review', 'sentiment',
                  'purchase', 'purchase_date', 'car_make', 'car_model', 'car_year']