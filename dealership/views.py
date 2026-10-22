from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Avg, Count
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from .models import CarMake, Dealer, Review
from .serializers import CarMakeSerializer, DealerSerializer, ReviewSerializer


def home(request):
    dealers = Dealer.objects.select_related('make').prefetch_related('reviews').all()
    state = request.GET.get('state', None)
    if state:
        dealers = dealers.filter(state__iexact=state)
    return render(request, 'home.html', {
        'dealers': dealers,
        'state_filter': state,
    })


def dealer_detail(request, dealer_id):
    dealer = get_object_or_404(Dealer.objects.select_related('make'), id=dealer_id)
    reviews = dealer.reviews.all()
    return render(request, 'dealer_detail.html', {
        'dealer': dealer,
        'reviews': reviews,
    })


@csrf_protect
def add_review(request, dealer_id):
    dealer = get_object_or_404(Dealer.objects.select_related('make'), id=dealer_id)
    if request.method == 'POST':
        name = request.POST.get('name', '')
        rating = int(request.POST.get('rating', 3))
        comment = request.POST.get('comment', '')
        if rating >= 4:
            sentiment = 'Positive'
        elif rating <= 2:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'
        Review.objects.create(
            dealer=dealer,
            name=name,
            rating=rating,
            comment=comment,
            sentiment=sentiment,
        )
        messages.success(request, 'Your review has been submitted successfully! Sentiment: ' + sentiment)
        return redirect('dealer_detail', dealer_id=dealer_id)
    return render(request, 'add_review.html', {
        'dealer': dealer,
    })


def dealers_by_state(request, state):
    dealers = Dealer.objects.select_related('make').prefetch_related('reviews').filter(state__iexact=state)
    return render(request, 'home.html', {
        'dealers': dealers,
        'state_filter': state,
    })


class CarMakeViewSet(viewsets.ModelViewSet):
    queryset = CarMake.objects.all()
    serializer_class = CarMakeSerializer


class DealerViewSet(viewsets.ModelViewSet):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer

    def list(self, request):
        queryset = Dealer.objects.all()
        state = request.query_params.get('state', None)
        if state:
            queryset = queryset.filter(state__iexact=state)
        serializer = DealerSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def reviews(self, request, pk=None):
        dealer = self.get_object()
        reviews = dealer.reviews.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def create(self, request, *args, **kwargs):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            rating = serializer.validated_data.get('rating', 3)
            if rating >= 4:
                serializer.validated_data['sentiment'] = 'Positive'
            elif rating <= 2:
                serializer.validated_data['sentiment'] = 'Negative'
            else:
                serializer.validated_data['sentiment'] = 'Neutral'
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def analyze(self, request):
        text = request.data.get('text', '')
        positive_words = ['fantastic', 'great', 'excellent', 'good', 'amazing', 'wonderful', 'outstanding', 'love', 'perfect']
        negative_words = ['bad', 'terrible', 'horrible', 'poor', 'awful', 'worst', 'hate', 'disappointing']
        text_lower = text.lower()
        pos_count = sum(1 for w in positive_words if w in text_lower)
        neg_count = sum(1 for w in negative_words if w in text_lower)
        if pos_count > neg_count:
            sentiment = 'Positive'
        elif neg_count > pos_count:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'
        return Response({'sentiment': sentiment, 'message': text})
