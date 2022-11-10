from django.contrib import admin
from constructor_telegram_bots.constructor.models import TelegramBotModel

# Register your models here.

@admin.register(TelegramBotModel)
class TelegramBotModelAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'online')
