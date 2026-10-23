from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.decorators.http import require_GET, require_POST
import json
from .models import CarMake, CarModel, Dealer, Review
from .serializers import CarMakeSerializer, DealerSerializer, ReviewSerializer


# ===== HTML Views =====

def home(request):
    dealers = Dealer.objects.all()
    return render(request, 'home.html', {'dealers': dealers})


def dealer_detail(request, dealer_id):
    dealer = get_object_or_404(Dealer, id=dealer_id)
    reviews = dealer.reviews.all()
    return render(request, 'dealer_detail.html', {'dealer': dealer, 'reviews': reviews})


@csrf_protect
def add_review(request, dealer_id):
    dealer = get_object_or_404(Dealer, id=dealer_id)
    if request.method == 'POST':
        name = request.POST.get('name', '')
        rating = int(request.POST.get('rating', 3))
        comment = request.POST.get('comment', '')
        purchase = request.POST.get('purchase', '')
        purchase_date = request.POST.get('purchase_date', '')
        car_make = request.POST.get('car_make', '')
        car_model = request.POST.get('car_model', '')
        car_year = request.POST.get('car_year', '')
        sentiment = 'Positive' if rating >= 4 else ('Negative' if rating <= 2 else 'Neutral')
        Review.objects.create(
            dealer=dealer, name=name, rating=rating, comment=comment,
            sentiment=sentiment, purchase=purchase, purchase_date=purchase_date,
            car_make=car_make, car_model=car_model,
            car_year=int(car_year) if car_year else None,
        )
        messages.success(request, 'Review submitted successfully!')
        return redirect('dealer_detail', dealer_id=dealer_id)
    return render(request, 'add_review.html', {'dealer': dealer})


def dealers_by_state(request, state):
    dealers = Dealer.objects.filter(state__iexact=state)
    return render(request, 'home.html', {'dealers': dealers})


# ===== API Views - Required Endpoints =====

@csrf_exempt
@require_POST
def djangoapp_login(request):
    """POST /djangoapp/login - JSON login"""
    try:
        data = json.loads(request.body)
        username = data.get('userName', '')
        password = data.get('password', '')
        from django.contrib.auth.models import User
        user = User.objects.filter(username=username).first()
        if user and user.check_password(password):
            request.session['user'] = username
            return JsonResponse({'userName': username, 'status': 'success'})
        return JsonResponse({'userName': username, 'status': 'failed', 'message': 'Invalid credentials'}, status=401)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)


@csrf_exempt
@require_GET
def djangoapp_logout(request):
    """GET /djangoapp/logout - JSON logout"""
    username = request.session.get('user', '')
    if 'user' in request.session:
        del request.session['user']
    return JsonResponse({'userName': username, 'status': 'logged out'})


@require_GET
def fetch_dealers(request):
    """GET /fetchDealers - All dealers"""
    dealers = Dealer.objects.all()
    serializer = DealerSerializer(dealers, many=True)
    return JsonResponse(serializer.data, safe=False)


@require_GET
def fetch_dealers_by_state(request, state):
    """GET /fetchDealers/<state> - Dealers by state"""
    dealers = Dealer.objects.filter(state__iexact=state)
    serializer = DealerSerializer(dealers, many=True)
    return JsonResponse(serializer.data, safe=False)


@require_GET
def fetch_dealer(request, dealer_id):
    """GET /fetchDealer/<id> - Dealer by ID"""
    dealer = get_object_or_404(Dealer, id=dealer_id)
    serializer = DealerSerializer(dealer)
    return JsonResponse(serializer.data)


@require_GET
def fetch_dealer_reviews(request, dealer_id):
    """GET /fetchDealerReviews/<id> - Reviews for a dealer"""
    dealer = get_object_or_404(Dealer, id=dealer_id)
    reviews = dealer.reviews.all()
    serializer = ReviewSerializer(reviews, many=True)
    return JsonResponse(serializer.data, safe=False)


@require_GET
def analyze_review(request):
    """GET /analyzeReview?reviewText=Fantastic+services - Sentiment analysis"""
    text = request.GET.get('reviewText', '')
    positive_words = ['fantastic', 'great', 'excellent', 'good', 'amazing', 'wonderful', 'outstanding', 'love', 'perfect']
    negative_words = ['bad', 'terrible', 'horrible', 'poor', 'awful', 'worst', 'hate', 'disappointing']
    text_lower = text.lower()
    pos_count = sum(1 for w in positive_words if w in text_lower)
    neg_count = sum(1 for w in negative_words if w in text_lower)
    if pos_count > neg_count:
        sentiment = 'positive'
    elif neg_count > pos_count:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
    return JsonResponse({'sentiment': sentiment, 'reviewText': text})


@require_GET
def get_carmakes(request):
    """GET /getCarMakes - All car makes with nested models"""
    makes = CarMake.objects.prefetch_related('models').all()
    serializer = CarMakeSerializer(makes, many=True)
    return JsonResponse(serializer.data, safe=False)


# ===== DRF ViewSets (kept for API compatibility) =====

class CarMakeViewSet(viewsets.ModelViewSet):
    queryset = CarMake.objects.prefetch_related('models').all()
    serializer_class = CarMakeSerializer


class DealerViewSet(viewsets.ModelViewSet):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer