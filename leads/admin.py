from django.contrib import admin
from .models import User, Agent, Lead
# Register your models here.

@admin.register(User, Agent, Lead)

class UserAdmin(admin.ModelAdmin):
    pass

class AgentAdmin(admin.ModelAdmin):
    pass

class LeadAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'agent')