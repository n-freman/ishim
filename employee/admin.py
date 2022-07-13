from django.contrib import admin
from .models import (
    Employee, CV, 
    Response, ChosenVacancy,
    KnownLanguage, KnownProgram,
    WorkExperience, Education,
    ChosenCv
    )


admin.site.register(Employee)
admin.site.register(CV)
admin.site.register(Response)
admin.site.register(ChosenVacancy)
admin.site.register(ChosenCv)
admin.site.register(KnownLanguage)
admin.site.register(KnownProgram)
admin.site.register(WorkExperience)
admin.site.register(Education)
