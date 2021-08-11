from django.urls import path
from .views import HomePageView, ListView

urlpatterns = [
    path('', HomePageView, name='home'),
    path('telegram_bots/', ListView, name='telegram_bots'),
]