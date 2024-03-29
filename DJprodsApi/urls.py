"""DJprodsApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.contrib import admin
from django.urls import path

# urls
from django.urls.conf import include
from rest_framework import routers
from apirest import views

from productos.views import ProductoListView ## .5

router=routers.DefaultRouter()
router.register('productos', views.ProductoViewSet)
# urls ##


urlpatterns = [
    path('admin/', admin.site.urls),
    # urls
    path('api/', include(router.urls)), # urls ##
    path('productos',ProductoListView.as_view(template_name="productos/index.html"),name='listar') ## .5
]
