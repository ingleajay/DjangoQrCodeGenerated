"""qr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from account import views as v
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('account/', include('account.urls'))
    path('', v.index, name="index"),
    path('signup/', v.sign_up, name="signup"),
    path('login/', v.user_login, name="login"),
    path('dash/', v.user_dash, name="dash"),
    path('logout/', v.user_logout, name="logg"),
    path('changepass/', v.user_change_pass, name="changepass"),
    path('userdetail/<int:id>', v.user_detail, name="userdetail"),
    path('profile/', v.user_profile, name="userprofile"),
    path('send', v.qr_code),
    path('viewhistory', v.user_histroy, name="userhistory")
]
