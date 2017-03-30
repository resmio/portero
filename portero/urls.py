from django.conf.urls import url
from django.contrib import admin

from vars.views import getvars

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', getvars),
]
