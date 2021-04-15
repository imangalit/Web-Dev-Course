"""hhback URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from api.views import company_list,company_id,company_vacancy,vacancy_list,vacancy_id,vacancy_top_ten

urlpatterns = [
    path('companies/', company_list),
    path('companies/<int:new_id>/', company_id),
    path('companies/<int:new_id>/vacancies', company_vacancy),

    path('vacancies/', vacancy_list),
    path('vacancies/<int:pk>/', vacancy_id),
    path('vacancies/top_ten/', vacancy_top_ten)
]
