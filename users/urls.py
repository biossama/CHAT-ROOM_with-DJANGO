from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	path('signup/', views.SignUpView.as_view(), name='register'),

	path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),

	path('logout/', auth_views.LogoutView.as_view(), name='logout'),

	path('password-reset/', auth_views.PasswordResetView.as_view(template_name="auth/passwordReset.html"), name='passwordReset'),

	path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(template_name="auth/passwordResetDone.html"), name='password_reset_done'),

	path('reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="auth/passwordResetConfirm.html"), name='password_reset_confirm'),

	path('reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name="auth/passwordResetComplete.html"), name='password_reset_complete'),

	path('password-change/', auth_views.PasswordChangeView.as_view(template_name="auth/passwordChange.html"), name='passwordChange'),

	path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(template_name="auth/password_change_done.html"), name='password_change_done'),


]
