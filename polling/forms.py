from django import forms
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string


from polling.models import *

#hospital subject device registration

class ButtonWidget(forms.Widget):
    template_name = 'auth_button_widget.html'

    def render(self, name, value, attrs=None):
        context = {
            'url': 'http://localhost:9000/patients/'
        }
        return mark_safe(render_to_string(self.template_name, context))

class RegisterSubjectForm(forms.ModelForm):
    FetchHospitalData = forms.CharField(widget=ButtonWidget)
    class Meta:
        model = HospitalSubjectDeviceRegistration
        exclude =[]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # exclude = ['author', 'updated', 'created', ]
        fields = ['text']
        widgets = {
            'text': forms.TextInput(
                attrs={'id': 'post-text', 'required': True, 'placeholder': 'Say something...'}
            ),
        }


class HospitalSubjectDeviceRegistrationForm(forms.ModelForm):
     url = forms.URLField()
class Meta:
	model = HospitalSubjectDeviceRegistration
	exclude = []





