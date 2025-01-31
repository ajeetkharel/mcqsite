"""mcqexamsite URL Configuration

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
from home import views
from user import views as userviews
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.online_exam, name='exam-home'),
    path('manage_exams/', views.manage_exams, name='exam-manage'),
    path('manage_exams/edit_exams/<int:id>/', views.edit_exams, name='edit-exam'),
    path('manage_exams/delete_exams/<int:id>/', views.delete_exams, name='delete-exam'),
    path('manage_exams/add_exams/', views.add_exams, name='add-exam'),
    path('', userviews.login_user, name='user-login'),
    path('register/', userviews.register_user, name='user-register'),
    path('logout/', userviews.logout_user, name='user-logout'),
    path('results/student00<pk>', userviews.user_result, name='user-result')
]+static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
