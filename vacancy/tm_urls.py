from django.urls import path
from . import tm_views


urlpatterns = [
    path('', tm_views.VacancyListView.as_view(), name='vacancies-all-tm'),
    path('delete/<pk>', tm_views.delete_my_vacancy, name='vacancy-delete-tm'),
    path('edit/<int:id>', tm_views.edit_vacancy, name='vacancy-edit-tm'),
    path('create/', tm_views.vacancy_create, name='create-vacancy-tm'),
    path('refresh/<id>', tm_views.refresh, name='refresh-vacancy-tm'),
    path('my/', tm_views.my_vacancies, name='my-vacancies-tm'),
    path('my/<int:pk>', tm_views.MyVacancyDetailView.as_view(), name='my-vacancy-info-tm'),
    path('<int:pk>', tm_views.VacancyDetailView.as_view(), name='vacancy-info-tm'),
    path('chosen/', tm_views.chosen_vacancies, name='employee-chosen-tm'),
    path('chosen/<id>', tm_views.add_to_chosen, name='chosen-vacancy-tm'),
    path('get/<int:n>', tm_views.get_vacancies, name='get-vacancies-tm'),
    path('suitable/<int:id>', tm_views.suitable_vacancies, name='suitable-vacancies-tm'),
    path('response-notifications/', tm_views.response_notifications, name='response-notifications-tm'),
    path('<int:pk>/responses', tm_views.vacancy_responses, name='vacancy-responses-tm'),
]