from django.urls import path
from django.contrib.auth import views
from .views import Login, Registro, Logout

urlpatterns = [
    path("login/", Login.as_view(), name="login"),
    path("registro/", Registro.as_view(), name="registro"),
    path("logout/", Logout.as_view(), name="logout"),
    path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
]

#urlpatterns = [
    #path("users/", include("django.contrib.auth.urls")),
    #path("users/login/", views.LoginView.as_view(), name="login"),
    #path("users/logout/", views.LogoutView.as_view(), name="logout"),
    #path("users/password_change/", views.PasswordChangeView.as_view(), name="password_change"),
    #path("users/password_change/done/", views.PasswordChangeDoneView.as_view(), name="password_change_done"),
    #
    #path("users/password_reset/done/", views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    #path("users/reset/<uidb64>/<token>/", views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    #path("users/reset/done/", views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
#]
