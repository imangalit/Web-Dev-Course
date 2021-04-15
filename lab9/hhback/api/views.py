from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.http import JsonResponse
from api.models import Vacancy
from api.models import Company

def company_list(request):
    companies = Company.objects.all()
    new_companies_json = [c.to_json() for c in companies]
    return JsonResponse(new_companies_json, safe=False)

def company_id(request, new_id):
    try:
        company = Company.objects.get(id=new_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(company.to_json())

def company_vacancy(request, new_id):
    try:
        company = Company.objects.get(id=new_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    vacancies = company.vacancy_set.all()
    json_vacancies = [j_v.to_json() for j_v in vacancies]
    return JsonResponse(json_vacancies, safe=False)

def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    json_vacancies = [j_v.to_json() for j_v in vacancies]
    return JsonResponse(json_vacancies, safe=False)

def vacancy_id(request, pk):
    try:
        vacancy = Vacancy.objects.get(id=pk)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(vacancy.to_json())

def vacancy_top_ten(request):
    vacancies = Vacancy.objects.order_by('-salary')[0:10]
    json_vacancies = [j_v.to_json() for j_v in vacancies]
    return JsonResponse(json_vacancies, safe=False)