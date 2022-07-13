from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import EmailMessage
from django.conf import settings
from django.db.models import Count, F
from django.db.models.lookups import GreaterThan
from django.utils import timezone as tz
import six
from employee.models import CV
from hirer.models import Company, Enterpreneuer
from vacancy.models import Vacancy
from articles.models import Article


class TokenGenerator(PasswordResetTokenGenerator):

    def _make_hash_value(self, user, timestamp):
        return six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.is_active)


generate_token = TokenGenerator()


def send_activation_email(user, request):
    current_site = get_current_site(request)
    email_subject = 'Activate your account'
    email_body = render_to_string(
        'main/activate.html',
        {
            'user': user,
            'domain': current_site,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': generate_token.make_token(user),
        }
    )
    email = EmailMessage(
        subject=email_subject, 
        body=email_body, 
        from_email=settings.EMAIL_FROM_USER,
        to=[user.email]
    )
    try:
        email.send()
        return True
    except Exception as identifier:
        return False


def get_user_type(user):
    if hasattr(user, 'employee'):
        user_type = user.employee
    elif hasattr(user, 'hirer'):
        user_type = user.hirer
    return user_type


def get_data(u_type):
    data = {}
    data['city_data'] = list(CV.objects.values('registration').annotate(dcount=Count('registration')).order_by())[:5]
    data['payment_data'] = CV.objects.aggregate(
        one=Count('min_salary', filter=GreaterThan(F('min_salary'), 999)),
        two=Count('min_salary', filter=GreaterThan(F('min_salary'), 1999)),
        three=Count('min_salary', filter=GreaterThan(F('min_salary'), 2999)),
        four=Count('min_salary', filter=GreaterThan(F('min_salary'), 3999)),
        five=Count('min_salary', filter=GreaterThan(F('min_salary'), 4999)),
    )
    if u_type == 'employee':
        data['vacancies'] = Vacancy.objects.all().order_by('-id')[:20]
    else:
        data['cv_list'] = CV.objects.all().order_by('-id')[:20]
        data['cv_list'] = []
    now = tz.now()
    data['now'] = now.year
    data['spheres'] = list(CV.objects.values('sphere').annotate(dcount=Count('sphere')).order_by())[:5]
    data['articles'] = list(Article.objects.all()[:3])
    return data


def get_footer():
    data = {
        'cv_num': CV.objects.count(),
        'vacancy_num': Vacancy.objects.count(),
        'user_num': User.objects.count()
    }
    return data