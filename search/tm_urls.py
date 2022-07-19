from django.urls import path
from .tm_views import *

urlpatterns = [
    path('vacancy/', search_vacancy, name='search-vacancy-tm'),
    path('cv', search_cv, name='search-cv-tm'),
    path('vacancy-wide', wide_search_vacancy, name='wide-search-vacancy-tm'),
    path('cv-wide', wide_search_cv, name='wide-search-cv-tm'),
    path('history-employee', search_history_employee, name='search-histroy-employee-tm'),
    path('history-hirer', search_history_hirer, name='search-histroy-hirer-tm'),
    path('delete/<int:id>', delete_history, name='delete-history-tm'),
    path('clear', clear_hisory, name='clear-history-tm'),
    path('again/<int:id>', search_again, name='search-again-tm'),
]