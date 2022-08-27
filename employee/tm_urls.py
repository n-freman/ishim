from django.urls import path
from . import tm_views

urlpatterns = [
    path('register/', tm_views.employee_create, name='create-employee-tm'),
    path('create-cv/', tm_views.create_cv, name='create-cv-tm'),
    path('my-cv/', tm_views.my_cv, name='my-cv-tm'),
    path('get-cv/<int:n>', tm_views.get_cv, name='get-cv-tm'),
    path('my-cv/<int:pk>', tm_views.MyCVDetailView.as_view(), name='my-cv-info-tm'),
    path('cv/<pk>', tm_views.CVDetailView.as_view(), name='cv-info-tm'),
    path('cv-edit/<int:id>', tm_views.edit_cv, name="cv-edit-tm"),
    path('delete-cv/<int:id>', tm_views.delete_cv, name='delete-cv-tm'),
    path('refresh-cv/<int:id>', tm_views.refresh_cv, name='refresh-cv-tm'),
    path('chosen', tm_views.chosen_cvs, name='hirer-chosen-tm'),
    path('chosen/<int:id>', tm_views.add_to_chosen, name='chosen-cv-tm'),
    path('suitable-cv/<int:id>', tm_views.suitable_cvs, name='suitable-cvs-tm'),
    path('response/<int:id>', tm_views.make_response, name='make-response-tm'),
    path('my-responses', tm_views.my_responses, name='my-responses-tm'),
]