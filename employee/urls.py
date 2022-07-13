from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.employee_create, name='create-employee'),
    path('create-cv/', views.create_cv, name='create-cv'),
    path('my-cv/', views.my_cv, name='my-cv'),
    path('get-cv/<int:n>', views.get_cv, name='get-cv'),
    path('my-cv/<int:pk>', views.MyCVDetailView.as_view(), name='my-cv-info'),
    path('cv/<pk>', views.CVDetailView.as_view(), name='cv-info'),
    path('cv-edit/<int:id>', views.edit_cv, name="cv-edit"),
    path('delete-cv/<int:id>', views.delete_cv, name='delete-cv'),
    path('refresh-cv/<int:id>', views.refresh_cv, name='refresh-cv'),
    path('chosen', views.chosen_cvs, name='hirer-chosen'),
    path('chosen/<int:id>', views.add_to_chosen, name='chosen-cv'),
    path('suitable-cv/<int:id>', views.suitable_cvs, name='suitable-cvs'),
    path('response/<int:id>', views.make_response, name='make-response'),
    path('my-responses', views.my_responses, name='my-responses')
]