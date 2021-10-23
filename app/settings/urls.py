from django.contrib import admin
from django.urls import path
from currency.views import hello_world, rate_list, contact_list

urlpatterns = [
    path('admin/', admin.site.urls),

    path('hello-world/', hello_world),
    path('rate/list/', rate_list),
    path('contact/list/', contact_list),
]
