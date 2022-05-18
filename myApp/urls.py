from django.urls import path
from .views import *

app_name = 'myApp'

urlpatterns = [
    path('', BaseView.as_view(), name='baseUrl'),

    # Get list of all drives
    path('drive/', DriveList.as_view(), name='drives'),

    # Get details of a particular drive
    path('drive/<str:address>', DriveDetails.as_view(), name='driveDetails'),

    # Get recommended drives for a particular user based on his transaction history
    path('drive/recommend/<str:userAddress>', RecommendedDrives.as_view(),name='recommendedDrives'),

    # Register a User
    path('user/', UserDetails.as_view(), name='userRegister'),

    path('userProfile/', UserProfileDetails.as_view(), name='userProfile'),

    # User Login

    # View all transactions corresponding to a drive
    path('drive/<str:id>/history', DriveHistory.as_view(), name='driveHistory'),

    # View a User's transaction history
    path('user/<str:id>/history', UserHistory.as_view(), name='userHistory'),

]