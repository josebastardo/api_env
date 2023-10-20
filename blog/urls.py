from django.urls import path
from .views import *

urlpatterns = [
  
    path('', index, name='index'),
    path('json_blog', blogJson, name="blogJson"),
    path('json_blog/<int:id>', blogDetail)
]
