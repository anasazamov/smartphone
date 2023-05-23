from django.contrib import admin
from .models import Phone

model_list = [Phone]

admin.site.register(model_list)