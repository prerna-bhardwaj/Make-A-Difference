from codecs import lookup
from django.http import HttpResponse, request
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework import status

class BaseView(APIView):
    def get(self, request):
        return HttpResponse("Base Url")



class DriveList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Drive.objects.all()
    serializer_class = DriveSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class DriveDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Drive.objects.all()
    serializer_class = DriveSerializer

    lookup_field = 'id'

    def get(self, request):
        return self.retrieve(request)

    def put(self, request):
        return self.update(request)

    def delete(self, request):
        return self.destroy(request)


class DriveHistory(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer

    lookup_field = 'id'

    def get(self, request, id):
        print(id)
        return self.list(request, drive=id)

    def post(self, request, id):
        data = request.POST
        drive = Drive.objects.get(id=data['drive'])
        print(drive)
        transaction = Transactions(drive=drive, amount=data['amount'], userId=data['userId'])
        transaction.save()
        print(transaction)
        print(request.POST)
        return Response(str(transaction), status=status.HTTP_201_CREATED)


class UserHistory(generics.ListCreateAPIView):
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer

    lookup_field = 'userId'


class UserProfileDetails(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


# Register a new user
class UserDetails(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    