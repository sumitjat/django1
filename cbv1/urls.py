"""cbv1 URL Configuration

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
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Simple.as_view(),name="main"),
    path('template/',views.TemplateExam.as_view()),
    path('context/',views.ContextExam.as_view(),name="context"),
    path('listdata/',views.ListExam.as_view(),name="listview"),
    path('detailview/<slug:pk>/',views.DetailExam.as_view(),name="deatilview"),
    path('deleteview/<slug:pk>/', views.DeleteExam.as_view(), name="deleteview")

]
