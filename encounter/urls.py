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
from encounter import views

app_name = 'encounter'
urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^encounter/(?P<encounter_id>[0-9]+)/$', views.view_patient_encounter, name='view_patient_encounter'),
    url(r'^encounter/(?P<encounter_id>[0-9]+)/history/$', views.create_patient_encounter_history, name='create_patient_encounter_history'),
    url(r'^encounter/edit/(?P<history_id>[0-9]+)/history/$', views.edit_patient_encounter_history, name='edit_patient_encounter_history'),
    url(r'^encounter/(?P<encounter_id>[0-9]+)/exam/$', views.create_patient_encounter_exam, name='create_patient_encounter_exam'),
    url(r'^encounter/edit/(?P<exam_id>[0-9]+)/exam/$', views.edit_patient_encounter_exam, name='edit_patient_encounter_exam'),
    url(r'^encounter/(?P<encounter_id>[0-9]+)/diagnosis/$', views.create_patient_encounter_diagnosis, name='create_patient_encounter_diagnosis'),
    url(r'^encounter/edit/(?P<diagnosis_id>[0-9]+)/diagnosis/$', views.edit_patient_encounter_diagnosis, name='edit_patient_encounter_diagnosis'),
    url(r'^patient/(?P<patient_id>[0-9]+)/new/$', views.new_encounter, name='new_encounter'),
    url(r'^encounter/(?P<encounter_id>[0-9]+)/$', views.end_encounter, name='end_encounter'),
]
