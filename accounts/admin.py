from django.contrib import admin
from .models import UserAccount

admin.site.site_header = "JavaScript"
# Register your models here.
class UserAccountAdmin(admin.ModelAdmin):
  list_display = ["username", "email", "claim"]
  search_fields = ["username"]
  exclude = ["slug"]

admin.site.register(UserAccount, UserAccountAdmin)
