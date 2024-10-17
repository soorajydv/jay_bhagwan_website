
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "jay Bhagwan sweets Admin"
admin.site.site_title = "jay Bhagwan sweets Admin Portal"
admin.site.index_title = "Welcome to jay Bhagwan sweets"


urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include('home.urls'))
]
