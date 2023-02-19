from django.urls import path
from accounts import views
from django.contrib.auth.decorators import login_required

app_name = 'accounts'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('profile/', login_required(views.ProfileView.as_view()), name="profile"),
    path('profile_register/', views.ProfileRegisterView.as_view(), name="register"),
    path('profile_edit/', login_required(views.ProfileEditView.as_view()), name="profile_edit"),
]
