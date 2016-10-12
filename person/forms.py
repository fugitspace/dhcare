from django.forms import ModelForm, Textarea, TextInput, Select, CharField
from person.models import Person, PersonContact, PersonDemographic, Relationship, PersonRelative

class PersonForm(ModelForm):
    class Meta:
        model = Person
        #id_number = CharField(200, disabled=True)
        fields = ['prefix', 'firstname', 'surname', 'othername']
        widgets = {
            'prefix':Select(attrs={'class':'form-control'}),
            'firstname':TextInput(attrs={'class':'form-control'}),
            'othername':TextInput(attrs={'class':'form-control'}),
            'surname':TextInput(attrs={'class':'form-control'}),
            #'id_number':TextInput(attrs={'class': 'form-control'})
        }
        
class PersonContactForm(ModelForm):
    class Meta:
        model = PersonContact
        fields = ['mobile', 'alt_mobile', 'telephone', 'email', 'mailing_address']
        widgets = {
            'mailing_address':Textarea(
                attrs={'cols':4, 'rows':5, 'class':"form-control"}
            ),
            'mobile':TextInput(attrs={'class':'form-control'}),
            'alt_mobile':TextInput(attrs={'class':'form-control'}),
            'telephone':TextInput(attrs={'class':'form-control'}),
            'email':TextInput(attrs={'class':'form-control'}),            
        }

class PersonDemographicForm(ModelForm):
    class Meta:
        model = PersonDemographic
        fields = ['gender', 'birthdate', 'marital_status', 'religion']
        widgets = {
            'gender':Select(attrs={'class':'form-control'}),
            'marital_status':Select(attrs={'class':'form-control'}),
            'religion':Select(attrs={'class':'form-control'}),            
            'birthdate':TextInput(attrs={'class':'form-control', 'id':'birthdate'}),              
        }

class PersonRelativeForm(ModelForm):
    class Meta:
        model = PersonRelative
        fields = ['full_name', 'relationship', 'mobile', 'alt_mobile', 'telephone', 'email', 'mailing_address']
        widgets = {
            'mailing_address':Textarea(
                attrs={'cols':4, 'rows':5, 'class':"form-control"}
            ),
            'mobile':TextInput(attrs={'class':'form-control'}),
            'alt_mobile':TextInput(attrs={'class':'form-control'}),
            'telephone':TextInput(attrs={'class':'form-control'}),
            'email':TextInput(attrs={'class':'form-control'}),
            'relationship':Select(attrs={'class':'form-control'}),            
            'full_name':TextInput(attrs={'class':'form-control'}),
        }
