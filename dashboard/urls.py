from django.urls import path
from .views import Expense
from rest_framework import routers
from .api import TranViewSet

router = routers.DefaultRouter()
router.register('api/trans', TranViewSet, 'trans')

urlpatterns = [
    path('dashboard/', Expense.as_view(),name='expense')
]
urlpatterns += router.urls