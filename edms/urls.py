from django.conf.urls import include, url

from edms.views import edms_hr, edms_hr_emp, edms_hr_dep, edms_hr_seat, edms_hr_emp_seat
from edms.views import edms_my_docs
from edms.views import edms_sub_docs

urlpatterns = [
  #  url(r'^$', RedirectView.as_view(url='/main', permanent=True)),
  #  url(r'^main/', edms_main, name='main'),
    url(r'^hr/emp/(?P<pk>\d+)/$', edms_hr_emp, name='hr_emp'),
    url(r'^hr/dep/(?P<pk>\d+)/$', edms_hr_dep, name='hr_dep'),
    url(r'^hr/seat/(?P<pk>\d+)/$', edms_hr_seat, name='hr_seat'),
    url(r'^hr/emp_seat/(?P<pk>\d+)/$', edms_hr_emp_seat, name='hr_seat'),
    url(r'^hr/', edms_hr, name='hr'),

    url(r'^my_docs/', edms_my_docs, name='my_docs'),

    url(r'^sub_docs/', edms_sub_docs, name='sub_docs'),
]
