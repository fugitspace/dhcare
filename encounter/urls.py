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
    url(r'^patient/(?P<patient_id>[0-9]+)/new/$', views.new_encounter, name='new_encounter'),
    url(r'^encounter/(?P<encounter_id>[0-9]+)/$', views.end_encounter, name='end_encounter'),
]
