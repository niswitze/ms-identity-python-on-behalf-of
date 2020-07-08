from .views import ResourceGroupView
from django.urls import path

urlpatterns = [
    path('', ResourceGroupView.as_view(), name="azure_management_home"),
]