from django.shortcuts import render
from django.views.generic.base import View
from django.template.context_processors import csrf
from django.core.exceptions import ObjectDoesNotExist
import logging

from django.utils.translation import ugettext as _

from registry.patients.models import ParentGuardian
from .models import Registry
from rdrf.utils import process_embedded_html

logger = logging.getLogger(__name__)


class RegistryView(View):

    def get(self, request, registry_code):
        try:
            if registry_code != "admin":
                registry = Registry.objects.get(code=registry_code)
            else:
                return render(request, 'rdrf_cdes/splash.html', {'body_expression': ' ',"state": "admin"})
        except ObjectDoesNotExist:
            return render(request, 'rdrf_cdes/splash.html', {'body': _('Oops, wrong registry code...'), "state": "missing"})

        context = {
            'body_expression': "rdrf://%s/splash_screen" % registry_code,
            'registry_code': registry_code,
            'state': "ok",
        }

        context.update(csrf(request))
        return render(request, 'rdrf_cdes/splash.html', context)
