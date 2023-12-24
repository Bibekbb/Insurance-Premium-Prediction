from django.urls import path, include
from django.contrib.auth.views import LogoutView
from home import views

urlpatterns = [
    path('base/', views.home, name=""),
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('predict/', views.prediction, name="predict"),
    path('user-login/', views.login, name="user-login"),
    path('user/register/', views.register, name="user-register"),
    path('logout/', LogoutView.as_view(), name='user-logout'),
    # path('accounts/', include('django.contrib.auth.urls')),
]   



