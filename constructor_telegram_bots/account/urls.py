from django.urls import path

from constructor_telegram_bots.account.views import upgrade_account_page, view_profile_page, update_user_icon, sign_out

urlpatterns = [
	path('<str:username>/upgrade/', upgrade_account_page),
	path('view/<str:username>/', view_profile_page),
	path('view/<str:username>/update_user_icon/', update_user_icon),
	path('sign_out/<str:username>/', sign_out),
]
