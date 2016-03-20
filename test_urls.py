from django.conf.urls import url
from django.contrib import admin

import test_views as views

urlpatterns = [
    url('^$', views.index, name='index'),

    url('^blocked-by-decorator/$', views.blocked_by_decorator, name='blocked_by_decorator'),

    url(r'^admin/', admin.site.urls),
]
