from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as django_views
from django.urls import path
from django.views.generic import TemplateView #used to locate template files
from . import views
urlpatterns = [
	path('',                                django_views.LoginView.as_view(),                 name='login'),
	path('signin/',                         django_views.LoginView.as_view(),                 name='login'),
	path('signup/',                         views.signup,                                     name='signup'),
	path('log_out/',                        views.logout,                                     name='logout'),
	path('password-change/',                django_views.PasswordChangeView.as_view(),        name='password_change'),
	path('password-change/done/',           django_views.PasswordChangeView.as_view(),        name='password_change_done'),
	path('password-reset/',                 django_views.PasswordResetView.as_view(),         name='password_reset'),
	path('password-reset/done/',            django_views.PasswordResetView.as_view(),         name='password_reset_done'),
	path('reset/uidb64>/<token>/',          django_views.PasswordResetConfirmView.as_view(),  name='password_reset_confirm'),
	path('reset/done/',                     django_views.PasswordResetCompleteView.as_view(), name='password_reset_done'),

]
