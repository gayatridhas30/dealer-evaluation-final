from django.urls import path
from . import views

urlpatterns = [
    # HTML Views
    path('', views.home, name='home'),
    path('dealers/<int:dealer_id>/', views.dealer_detail, name='dealer_detail'),
    path('dealers/<int:dealer_id>/add-review/', views.add_review, name='add_review'),
    path('dealers/state/<str:state>/', views.dealers_by_state, name='dealers_by_state'),

    # Required API Endpoints
    path('djangoapp/login', views.djangoapp_login, name='djangoapp_login'),
    path('djangoapp/logout', views.djangoapp_logout, name='djangoapp_logout'),
    path('fetchDealers', views.fetch_dealers, name='fetch_dealers'),
    path('fetchDealers/<str:state>', views.fetch_dealers_by_state, name='fetch_dealers_by_state'),
    path('fetchDealer/<int:dealer_id>', views.fetch_dealer, name='fetch_dealer'),
    path('fetchDealerReviews/<int:dealer_id>', views.fetch_dealer_reviews, name='fetch_dealer_reviews'),
    path('analyzeReview', views.analyze_review, name='analyze_review'),
    path('getCarMakes', views.get_carmakes, name='get_carmakes'),
]
