from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from account.api.views import PhonePrefixList, RegisterUser

urlpatterns = [
    path('phone-prefixes/', PhonePrefixList.as_view()),
    
    
]

urlpatterns = format_suffix_patterns(urlpatterns)