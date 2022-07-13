from django.urls import path
from .views import *

urlpatterns = [
    path('vacancy/', search_vacancy, name='search-vacancy'),
    path('cv', search_cv, name='search-cv'),
    path('vacancy-wide', wide_search_vacancy, name='wide-search-vacancy'),
    path('cv-wide', wide_search_cv, name='wide-search-cv'),
    path('history-employee', search_history_employee, name='search-histroy-employee'),
    path('history-hirer', search_history_hirer, name='search-histroy-hirer'),
    path('delete/<int:id>', delete_history, name='delete-history'),
    path('clear', clear_hisory, name='clear-history'),
    path('again/<int:id>', search_again, name='search-again')
]