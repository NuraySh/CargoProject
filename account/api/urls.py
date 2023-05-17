from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from account.api.views import (ActivateAccountView, LoginView, PhonePrefixList,
                               RegisterView)

urlpatterns = [
    path("phone-prefixes/", PhonePrefixList.as_view()),
    path("register/", RegisterView.as_view(), name="auth_register"),
    path("login/", LoginView.as_view(), name="login"),
    path(
        "activate/<str:uidb64>/<str:token>/",
        ActivateAccountView.as_view(),
        name="activate_account",
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
