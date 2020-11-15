from django.urls import path
from .views import *

urlpatterns = [
    # Account views
    path('account/<int:pk>', UserAccount.as_view(), name='account-view'),
    path('account/<int:pk>/update', UpdateAccount.as_view(), name='update-account'),
    path('account/<int:pk>/delete', DeleteAccount.as_view(), name='delete-account'),

    # Password management views
    path('account/<int:pk>/password-change/', PasswordChange.as_view(), name='pw-change'),
    path('account/<int:pk>/password-change-done/', PasswordChangeDone.as_view(), name='pw-change-done'),
    path('password-reset/', PasswordResetView.as_view(), name='pw-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(), name='pw-reset-done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='pw-reset-confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='pw-reset-complete'),

    # Other
    path('signup/', CreateUser.as_view(), name='signup')
]