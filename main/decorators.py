from django.contrib.auth.decorators import user_passes_test
import ishim.settings as settings


def login_forbidden(function=None, redirect_url=None):
    if not redirect_url:
        redirect_url = settings.LOGIN_REDIRECT_URL
    
    actual_decorator = user_passes_test(
        lambda u: u.is_anonymous,
        login_url =redirect_url,
    )

    if function:
        return actual_decorator(function)
    return actual_decorator


def hirer_required(function=None, redirect_url=None):
    if not redirect_url:
        redirect_url = settings.LOGIN_REDIRECT_URL
    
    actual_decorator = user_passes_test(
        lambda u: hasattr(u, 'hirer'),
        login_url =redirect_url,
    )

    if function:
        return actual_decorator(function)
    return actual_decorator


def employee_required(function=None, redirect_url=None):
    if not redirect_url:
        redirect_url = settings.LOGIN_REDIRECT_URL
    
    actual_decorator = user_passes_test(
        lambda u: hasattr(u, 'employee'),
        login_url =redirect_url,
    )

    if function:
        return actual_decorator(function)
    return actual_decorator