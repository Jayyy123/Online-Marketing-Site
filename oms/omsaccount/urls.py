from unicodedata import name
from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('login/', views.loginuser, name = 'login'),
    path('logout/', views.logout_user, name = 'logout'),
    path('account/', views.account, name = 'account'),
    path('profile/<str:pk>/', views.profile, name = 'profile'),
    path('prof/', views.prof, name = 'prof'),
    path('edit_profile/<str:pk>/', views.edit_profile, name = 'edit_profile'),
    path('delete_profile/<str:pk>/', views.delete_profile, name = 'delete_profile'),
    path('user_profiles/', views.user_profiles, name = 'user_profiles'),
    path('page/', views.page, name = "page"),
]