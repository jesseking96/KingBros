from django.urls import path
from .views import StallListView,StallDetailView,StallInfoRequest
urlpatterns = [
    path('',StallListView.as_view(),name='stall_list'),
    path('info/<slug:slug>/',StallDetailView.as_view(),name='stall_detail'),
    path('info/<slug:slug>/requestinfo',StallInfoRequest.as_view(),name='info_request'),
]
