from django.contrib import admin

# Register your models here.

from .models import User

class UserModelAdmin(admin.ModelAdmin):
	list_display = ["name", "age", "qualification"] 
	
	class Meta:                    
		model = User

admin.site.register(User, UserModelAdmin)
