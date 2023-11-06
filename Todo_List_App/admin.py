from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from Todo_List_App.models import Task, Category, Profile, Activity, CustomUser

class TaskAdmin(admin.ModelAdmin):
    list_display = ('taskTitle', 'category', 'dueDate', 'completed','important', 'completedDate', 'createdDate', 'user')
    ordering = ('completed', 'dueDate',)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'completed_tasks_count')

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'account_created', 'task_created','task_completed', 'task_edited','task_deleted','last_online')
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'phone', 'address', 'is_staff')
admin.site.register(Category, CategoryAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
