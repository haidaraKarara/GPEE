from django.shortcuts import render
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt

from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

# Create your views here.
# @csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    """ API endpoint that allows users to login """
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'errors': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'errors': "Informations d'identifiaction invalides !"}, # Invalid Credentials
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({
        'token': token.key,
        'user_id': user.pk,
        },status=HTTP_200_OK)
                    
#@csrf_exempt
@permission_classes((AllowAny,))
@api_view(["POST"])
def logout_view(request):
    request.user.auth_token.delete()
    #logout(request)
    return Response({"ok":True},status=HTTP_200_OK)
