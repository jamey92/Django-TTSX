"""ttsx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include


urlpatterns = [
    # 后台管理路由
    url(r'^admin/', include('ttsxAdmin.urls', namespace='admin')),
    # 商城展示路由
    url(r'^store/', include('sx_store.urls', namespace='store')),
    # 购物过程路由
    url(r'^shopping/', include('sx_shopping.urls', namespace='shopping')),
    # 订单路由
    url(r'^order/', include('sx_order.urls', namespace='order')),
    # 用户中心路由
    url(r'^user/', include('sx_user.urls', namespace='user')),
]
