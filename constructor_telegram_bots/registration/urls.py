from django.urls import path

from constructor_telegram_bots.registration.views import registration_page, register_account

urlpatterns = [
	path('registration/', registration_page),
	path('registration/register_account/', register_account),
]
