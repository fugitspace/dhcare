"""patient URL Configuration

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from patient import views

app_name = 'patient'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^create/$', views.create_patient, name='create_patient'),
    url(r'^search/$', views.search_patient, name='search_patient'),
    url(r'^view/(?P<patient_id>[0-9]+)/$', views.view_patient, name='view_patient'),
    url(r'^edit/(?P<patient_id>[0-9]+)/$', views.edit_patient, name='edit_patient'),
    url(r'^(?P<patient_id>[0-9]+)/demographic/$', views.create_patient_demographic, name='create_patient_demographic'),
    url(r'^(?P<patient_id>[0-9]+)/contact/$', views.create_patient_contact, name='create_patient_contact'),
    url(r'^(?P<patient_id>[0-9]+)/vitals/$', views.create_patient_vitals, name='create_patient_vitals'),
    url(r'^(?P<patient_id>[0-9]+)/index_card/$', views.patient_index_card, name='create_patient_index_card'),
    url(r'^(?P<patient_id>[0-9]+)/relative/$', views.create_patient_relative, name='create_patient_relative'),
]
