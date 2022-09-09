"""Customer_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# # from django.urls import path
# # from django.conf.urls import url,include
# #
# # urlpatterns = [
# #     path('admin/', admin.site.urls),
# #     path('api/Customer_App/',include('Customer_App.urls')),
# #     url(r'^api/', include('UserToken.urls')),
# # ]

from django.contrib import admin
from django.urls import path, re_path, include
# from rest_framework_swagger.views import get_swagger_view
# schema_view = get_swagger_view(title='SOLR BULK UPLOAD API')
# from rest_framework_swagger.views import get_swagger_view
# schema_view = get_swagger_view(title='Django Assesment')

urlpatterns = [
    path(r'^admin/', admin.site.urls),
    re_path('Employee/', include('Customer_App.urls')),
    # re_path('', schema_view),
    path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
