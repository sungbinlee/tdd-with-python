from django.contrib import admin
from django.urls import path, include
from lists import views as home_views

urlpatterns = [
    # path("admin/", admin.site.urls),
    path('', home_views.home_page, name='home'),
]
