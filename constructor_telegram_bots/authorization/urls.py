from django.urls import path
from constructor_telegram_bots.authorization.views import authorization_page, authorize_in_account

urlpatterns = [
	path('authorization/', authorization_page),
	path('authorization/authorize_in_account/', authorize_in_account),
]
