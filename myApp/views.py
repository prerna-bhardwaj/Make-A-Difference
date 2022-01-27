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

    def get(self, request, id):
        return self.retrieve(request, id=id)

    def put(self, request, id):
        return self.update(request, id=id)

    def delete(self, request, id):
        return self.destroy(request, id=id)


class DriveHistory(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer
    model = Transactions

    lookup_field = 'id'

    def get_queryset(self):
        return Transactions.objects.filter(drive=self.kwargs['id'])

    def get(self, request, id):
        queryset = self.get_queryset()
        serializer = TransactionSerializer(queryset, many=True)
        return Response(serializer.data)


    def post(self, request):
        data = request.POST
        drive = Drive.objects.get(id=data['drive'])
        print(drive)
        transaction = Transactions(drive=drive, amount=data['amount'], userId=data['userId'])
        transaction.save()
        print(transaction)
        return Response(str(transaction), status=status.HTTP_201_CREATED)


class UserHistory(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer
    model = Transactions

    lookup_field = 'id'

    def get_queryset(self):
        return Transactions.objects.filter(userId=self.kwargs['id'])

    def get(self, request, id):
        queryset = self.get_queryset()
        serializer = TransactionSerializer(queryset, many=True)
        return Response(serializer.data)
        


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