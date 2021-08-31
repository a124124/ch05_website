# blog/urls.py

from django.urls import path
from . import views

urlpatterns =[
    path('', views.PostList.as_view()),
    path('<int:pk>', views.PostDetail.as_view(), name='detail'),
    # path('<int:pk>', views.detail, name='detail'),



]