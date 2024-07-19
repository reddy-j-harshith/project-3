from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view as view

from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
    ]

    return Response(routes)

# Create your views here.
def register_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, "User already exists")
            return HttpResponse.status_code(409, "User already exists")

        user = User.objects.create_user(username = username, password = password)        
        user.save()

        messages.info(request, "User created successfully")
        return HttpResponse.status_code(200, "User created successfully")
        
    return HttpResponse.status_code(400, "Bad request")
