from django.urls import path

from . import views


app_name = 'foresttrees'

urlpatterns = [
    path('hospital/<int:hospital_id>/', views.regression_view, name='regression_view'),
]
