from django.urls import path
from . import views

urlpatterns = [
    path('Category/',views.Categoryview),
    path('Unit/',views.Unitview),
    path('test/',views.test),
    path('Item/',views.Itemview),
    path('Supplier/',views.Supplierview),
    path('Order/',views.Orderview),
    path('Employee/',views.Employeeview),

    ]   