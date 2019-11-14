
from django.urls import path
from . import views

from django.views.generic.detail import DetailView
from .views import *
from .models import Photo

app_name = 'photo'

urlpatterns = [
    path('', views.base, name='base'),
    path('upload/', PhotoUploadView.as_view(), name='photo_upload'),
    path('output/', views.Output, name='output'),
    # path('delete/<int:pk>/', PhotoDeleteView.as_view(), name='photo_delete'),
    # path('update/<int:pk>/', PhotoUpdateView.as_view(), name='photo_update'),
]