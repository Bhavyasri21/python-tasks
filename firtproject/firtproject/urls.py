"""firtproject URL Configuration

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
from FirstApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('ht/',views.htmltag),
    path('un/<str:username>/',views.username),
    path('user/<str:username>/<int:age>/',views.user),
    path('emp/<int:id>/<str:username>/<int:sal>/',views.emp),
    path('hte/',views.htm),
    path('yt/<int:id>/<str:name>/',views.ytname),
    path('stud/',views.studentdetails),
    path('internalJs/',views.internalJs),
    path('myform/',views.myform,name="myform"),
    path('register/',views.register,name="myform1"),
    path('btrg/',views.btrg,name="btr"),
    path('reg1/',views.register1),
    path('reg2/',views.register2,name="register2"),
    path('display2/',views.display2,name="display2"),
    path('views/<int:num>/',views.view2,name="view2"),
]

