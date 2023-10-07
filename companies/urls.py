from django.urls import path
from companies import views

urlpatterns = [
    path('companies/', views.CompanyList.as_view()),
]
