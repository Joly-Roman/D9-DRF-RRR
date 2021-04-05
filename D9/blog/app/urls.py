from .views import *
from .views import *
from django.urls import path, include

app_name = 'app'
urlpatterns = [
    path('', PostList.as_view(), name='post-list'),
    path('<int:pk>', PostDetail.as_view(), name='post-detail'),
    path('categories/', CategotyList.as_view(), name='category-list'),
    path('categories/<int:pk>', CategotyDetail.as_view(), name='category-detail'),

]