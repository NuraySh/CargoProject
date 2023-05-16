from rest_framework.authtoken.models import Token

token = Token.objects.create()
print(token.key)
