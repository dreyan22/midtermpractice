from django.urls import path
from .views import CommissionListView, CommissionDetailView


urlpatterns = [
    path('commissions/list', CommissionListView.as_view(), name='commission_list'),
    path('', CommissionListView.as_view(), name='commission_list'),
    path('commission/<int:pk>', CommissionDetailView.as_view(), name='commission_detail'),
]


app_name = 'commission'