from django.urls import path
from . import views
from stalls import views as stallviews
urlpatterns = [
    path('',views.HomePageView.as_view(),name='home'),
    path('about/',views.AboutPageView.as_view(),name='about'),
    path('contact/',views.ContactPageView.as_view(),name='contact'),
    path('thanks/',views.ThankYouView.as_view(),name='thanks'),
    path('photos/',views.PhotosView.as_view(),name='photos'),
]
