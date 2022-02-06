from django.urls import path
from . import views


app_name = 'housing'
urlpatterns = [
    path('building-create/', views.BuildingCreateAPIView.as_view(), name='building_create'),
    path('building-retrieve/<pk>/', views.BuildingRetrieveAPIView.as_view(), name='building_retrieve'),
    path('building-update/<pk>/', views.BuildingUpdateAPIView.as_view(), name='building_update'),
    path('building-delete/<pk>/', views.BuildingDeleteAPIView.as_view(), name='building_delete'),
    path('building-list/', views.BuildingListAPIView.as_view(), name='building_list'),
]
