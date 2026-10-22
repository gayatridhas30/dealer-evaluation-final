"""
URL configuration for djangoproj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from dealership import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('dealership.urls')),
    path('', views.home, name='home'),
    path('dealers/state/<str:state>/', views.dealers_by_state, name='dealers_by_state'),
    path('dealers/<int:dealer_id>/', views.dealer_detail, name='dealer_detail'),
    path('dealers/<int:dealer_id>/add-review/', views.add_review, name='add_review'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
