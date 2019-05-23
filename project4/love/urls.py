from django.urls import path
from . import views

urlpatterns = [
    path('response/', views.get_results),
    path('names/', views.get_names),
    path('comment/', views.get_comment),
    path('all_comments/', views.all_comments)
]