from django.contrib import admin
from .models import Students, Marks, User
# Register your models here.

admin.site.register(User)
admin.site.register(Students)
admin.site.register(Marks) 