from django.urls import path
from . import views


urlpatterns = [
    path('', views.VacancyListView.as_view(), name='vacancies-all'),
    path('delete/<pk>', views.delete_my_vacancy, name='vacancy-delete'),
    path('edit/<int:id>', views.edit_vacancy, name='vacancy-edit'),
    path('create/', views.vacancy_create, name='create-vacancy'),
    path('refresh/<id>', views.refresh, name='refresh-vacancy'),
    path('my/', views.my_vacancies, name='my-vacancies'),
    path('my/<int:pk>', views.MyVacancyDetailView.as_view(), name='my-vacancy-info'),
    path('<int:pk>', views.VacancyDetailView.as_view(), name='vacancy-info'),
    path('chosen/', views.chosen_vacancies, name='employee-chosen'),
    path('chosen/<id>', views.add_to_chosen, name='chosen-vacancy'),
    path('get/<int:n>', views.get_vacancies, name='get-vacancies'),
    path('suitable/<int:id>', views.suitable_vacancies, name='suitable-vacancies'),
    path('response-notifications/', views.response_notifications, name='response-notifications'),
    path('<int:pk>/responses', views.vacancy_responses, name='vacancy-responses'),
]