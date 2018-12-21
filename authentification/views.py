# from django.contrib.auth import authenticate
# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.authtoken.models import Token
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import AllowAny
# from rest_framework.response import Response
# from rest_framework.status import (HTTP_200_OK, HTTP_400_BAD_REQUEST,
#                                    HTTP_404_NOT_FOUND)


# # Create your views here.
# # @csrf_exempt
# @api_view(["POST"])
# @permission_classes((AllowAny,))
# def login(request):
#     """ API endpoint that allows users to login """
#     username = request.data.get("username")
#     password = request.data.get("password")
#     if username is None or password is None:
#         return Response({'errors': 'Please provide both username and password'},
#                         status=HTTP_400_BAD_REQUEST)
#     user = authenticate(username=username, password=password)
#     if not user:
#         return Response({'errors': "Informations d'identifiaction invalides !"}, # Invalid Credentials
#                         status=HTTP_404_NOT_FOUND)
#     token, _ = Token.objects.get_or_create(user=user)
#     return Response({
#         'token': token.key,
#         'user_id': user.pk,
#         },status=HTTP_200_OK)
                    
# #@csrf_exempt
# #@csrf_exempt
# @permission_classes((AllowAny,))
# @api_view(["POST"])
# def logout_view(request):
#     request.user.auth_token.delete()
#     #logout(request)
#     return Response({"ok":True},status=HTTP_200_OK)

from rest_framework.authentication import BasicAuthentication
from knox.views import LoginView as KnoxLoginView
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes

# class LoginView(KnoxLoginView):
#     permission_classes = (AllowAny,)
#     # authentication_classes = [BasicAuthentication]


from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login


class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)


    