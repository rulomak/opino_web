from django.urls import path
from . import views

app_name="shops"

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:country_id>/cities/', views.city, name='cities'),
    path('choose_category/<int:city_id>/', views.choose_category, name='choose_category'),
    path('city_category/<int:city_id>/<int:categoria_id>/', views.city_category, name='city_category'),
    path('contact/', views.contact, name='contact'),
    path('privacy-policies/', views.privacy_policies, name='pdp'),
    path('search/', views.search, name='search'),
    path('<post_slug>/', views.detail_post, name='post')
    
    
]

