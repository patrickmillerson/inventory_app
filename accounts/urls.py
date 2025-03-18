from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup_view, login_view, logout_view, delete_account, change_password, password_change_done

urlpatterns = [
    path("signup/", signup_view, name="signup"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),

    # Password Reset
    path("password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path("delete_account/", delete_account, name="delete_account"),
    path("password-change/", change_password, name="password-change"),
    path("password-change/done/", password_change_done, name="password_change_done"),
]
