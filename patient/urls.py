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
    url(r'^view/(?P<patient_id>[0-9]+)/$', views.view_patient, name='view_patient'),
    url(r'^edit/(?P<patient_id>[0-9]+)/$', views.edit_patient, name='edit_patient'),
]
