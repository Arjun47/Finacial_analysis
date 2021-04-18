from django.contrib import admin
from .models import Transaction, Category, Tr_type
# Register your models here.
admin.site.register(Transaction)
admin.site.register(Category)
admin.site.register(Tr_type)