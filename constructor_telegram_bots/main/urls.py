from django.urls import path

from constructor_telegram_bots.main.views import main_page, view_site_user_profile_page

urlpatterns = [
	path('', main_page),
	path('view_site_user_profile/<int:other_user_id>/', view_site_user_profile_page)
]
