# from django.contrib import admin #最初からあった要らない
# from . import test
# from django.urls import path,include

# urlpatterns = [
#     path('admin/', admin.site.urls), #最初からあった要らない
#     path('test/', test.test, name='test'),
# ]

from django.urls import include, path
from django.contrib import admin
 
urlpatterns = [
    path(r'^myapp/', include('myapp.urls')),
    path(r'^admin/', admin.site.urls),
]