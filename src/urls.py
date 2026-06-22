from django.contrib import admin
from django.urls import path
# Bu yerda home_page yoniga about_page'ni ham qo'shib qo'yamiz:
from blog.views import home_page, about_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),

    # Yangi sahifamizning manzili:
    path('biz-haqimizda/', about_page),
]