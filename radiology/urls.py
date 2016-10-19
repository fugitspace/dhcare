"""appointment URL Configuration

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
from radiology import views

app_name = 'radiology'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^encounter/(?P<encounter_id>[0-9]+)/$', views.view_patient_radio_requests, name='view_patient_radio_requests'),
    url(r'^encounter/(?P<encounter_id>[0-9]+)/request/$', views.create_radiology_request, name='create_radiology_request'),
    url(r'^request/(?P<request_id>[0-9]+)/edit/$', views.edit_radiology_request, name='edit_radiology_request'),
]
