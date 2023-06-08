# Pet Adoption Platform
from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import User, Pet

from .serializers import UserSerializer, PetSerializer

from rest_framework.generics import GenericAPIView

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated ,AllowAny, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend


from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

############################################################################################

# User Create

class UserLCView(GenericAPIView,ListModelMixin, CreateModelMixin):
 queryset = User.objects.all()
 serializer_class = UserSerializer
 
 authentication_classes = [BasicAuthentication]
 permission_classes = [IsAuthenticated]
 #permission_classes = [AllowAny]
 #permission_classes = [IsAdminUser]
 filter_backends =  [DjangoFilterBackend]
 
 
    
 def get(self, request, *args, **kwargs ):
     return self.list(request, request ,*args, **kwargs )
 
 def post(self, request, *args, **kwargs ):
     return self.create(request ,*args, **kwargs )
 
class UserRUDView(GenericAPIView,ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
 queryset = User.objects.all()
 serializer_class = UserSerializer
 
 authentication_classes = [BasicAuthentication]
 permission_classes = [IsAuthenticated]
 #permission_classes = [AllowAny]
 #permission_classes = [IsAdminUser]
 
 filter_backends =  [DjangoFilterBackend]
    
 def get(self, request, *args, **kwargs ):
     return self.retrieve(request, request ,*args, **kwargs )
 
 def put(self, request, *args, **kwargs ):
     return self.update(request ,*args, **kwargs ) 
 
 def delete(self, request, *args, **kwargs ):
     return self.destroy(request ,*args, **kwargs ) 


#####################################################################################################

# Pet API

class PetLCView(GenericAPIView,ListModelMixin, CreateModelMixin):
 queryset = Pet.objects.all()
 serializer_class = PetSerializer
 
 authentication_classes = [BasicAuthentication]
 permission_classes = [IsAuthenticated]
 
 #permission_classes = [AllowAny]
 #permission_classes = [IsAdminUser]
 
 filter_backends =  [DjangoFilterBackend]
 
    
 def get(self, request, *args, **kwargs ):
     return self.list(request, request ,*args, **kwargs )
 
 def post(self, request, *args, **kwargs ):
     return self.create(request ,*args, **kwargs )
 
class PetRUDView(GenericAPIView,ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
 queryset = Pet.objects.all()
 serializer_class = PetSerializer
 
 authentication_classes = [BasicAuthentication]
 permission_classes = [IsAuthenticated]

 
 #permission_classes = [AllowAny]
 #permission_classes = [IsAdminUser]
 filter_backends =  [DjangoFilterBackend]

    
 def get(self, request, *args, **kwargs ):
     return self.retrieve(request ,*args, **kwargs )
 
 def put(self, request, *args, **kwargs ):
     return self.update(request ,*args, **kwargs ) 
 
 def delete(self, request, *args, **kwargs ):
     return self.destroy(request ,*args, **kwargs ) 