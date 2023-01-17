from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from account.api import views

urlpatterns = [
    path('phone-prefixes/', views.PhonePrefixList.as_view()),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)