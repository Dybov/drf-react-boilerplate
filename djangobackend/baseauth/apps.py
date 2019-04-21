from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BaseauthConfig(AppConfig):
    name = 'baseauth'
    verbose_name = _('authentication and authorization')
    verbose_name_plural = _('authentication and authorization')
