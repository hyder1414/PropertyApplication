#
from django.urls import path, re_path
from . import views
urlpatterns =[
 path('property_list',views.property_list, name='property_list'),
 re_path(r'^property_detail/(?P<id>\d+)/',views.property_detail, name='property_detail'),
 re_path(r'^property_edit/(?P<id>\d+)/',views.property_edit, name='property_edit'),
 path('property_create',views.PropertyCreate.as_view(), name='property_create'),
 path('property/<int:pk>/update/',views.PropertyUpdate.as_view(),name='property_update'),
 path('owner_list',views.OwnerList.as_view(),name='owner_list'),
 path('owner/update/<int:pk>',views.OwnerUpdate.as_view(),name='owner_update'),
 path('owner/detail/<int:pk>',views.OwnerDetail.as_view(),name='owner_detail'),
 re_path(r'^property_search/$',views.PropertyOwnerList.as_view()),
 path('',views.index, name='index'),
  ]