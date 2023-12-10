from django.contrib import admin
from .models import Food
from .models import Crops

models_list = [Food,Crops]
admin.site.register(models_list)

# Register your models here.
