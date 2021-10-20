"""Assing_Project URL Configuration

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
from django.urls import path
from application import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Employee_List, name='Employee_List'),
    path('Add_Employee', views.Add_Employee, name='Add_Employee'),
    path('Update_Employee/<int:id>', views.Update_Employee, name='Update_Employee'),
    path('Delete_Employee/<int:id>', views.Delete_Employee, name='Delete_Employee'),
    path('Same_Salary', views.Same_Salary, name='Same_Salary'),
    path('Second_Lowest_Salary', views.Second_Lowest_Salary, name='Second_Lowest_Salary'),
    path('Top_10_Salary', views.Top_10_Salary, name='Top_10_Salary'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
