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

    lookup_field = 'address'

    def get(self, request, address):
        return self.retrieve(request, address=address)

    def put(self, request, address):
        return self.update(request, address=address)

    def delete(self, request, address):
        return self.destroy(request, address=address)


class DriveHistory(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer
    model = Transactions

    # lookup_field = 'address'

    def get_queryset(self):
        drive = Drive.objects.get(address=self.kwargs['id'])
        list = Transactions.objects.filter(drive=drive)
        # print(list)
        return list

    def get(self, request, id):
        print(self.kwargs)
        queryset = self.get_queryset()
        serializer = TransactionSerializer(queryset, many=True)
        return Response(serializer.data)


    def post(self, request, id):
        data = request.data
        print("Data : ", request.POST, request.data)
        drive = Drive.objects.get(address=id)
        drive.amount_raised += int(data['amount'])
        drive.donation_count += 1
        drive.save()
        transaction = Transactions(drive=drive, amount=data['amount'], userId=data['userId'])
        print(transaction)
        transaction.save()
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