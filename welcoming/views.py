from agenda.icalReader import IcalReader
from agenda.models import Event
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView
from guide.models import Guide
from members.models import AcademicYear
import json
import pprint

CAL_URL = "https://calendar.google.com/calendar/ical/b6s2tn7vm5mr8cl4sdq1m9qp0o%40group.calendar.google.com/public/basic.ics"

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        try:
            guide = Guide.objects.filter(active=True).get()
        except:
            guide = None
        try:
            year_active = AcademicYear.objects.filter(active=True).get()
        except ObjectDoesNotExist:
            year_active = None

        context['guide'] = guide
        context['events_dict'] = IcalReader.jsonify(IcalReader(CAL_URL).read())
        context['academic_year'] = year_active
        return context
