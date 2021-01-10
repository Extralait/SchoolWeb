from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin, UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Event, Organization, userProfile, BestStudent,Achievements

admin.site.register(Event)
admin.site.register(Organization)
admin.site.register(BestStudent)
admin.site.register(Achievements)



# Custom User admin with no username field


@admin.register(userProfile)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = userProfile
    list_display = ('email', 'is_staff', 'is_superuser','full_name')
    list_filter = ('is_staff', 'is_superuser','full_name')
    fieldsets = (
        (None, {'fields': ('email', 'password','full_name','status','SNILS','is_staff','is_superuser')}),
        # ('Permissions', {'fields': ('is_staff', 'is_superuser','full_name')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','full_name','status','SNILS','password1', 'password2', 'is_staff','is_superuser')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)