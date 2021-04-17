from django.urls import path
# from . import views
from .views import Expense

urlpatterns = [
    path('dashboard/', Expense.as_view(),name='expense')
]