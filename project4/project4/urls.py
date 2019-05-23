from django.contrib import admin
from django.urls import path, include
from love.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('love.urls')),
     path("", index, name="index")
]
