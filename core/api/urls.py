from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core.api import views

urlpatterns = [
    path('news/', views.NewsList.as_view()),
    path('countrues/', views.CountryList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)