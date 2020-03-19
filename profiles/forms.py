from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import BabysitterProfile, RecommendationsOfSitter, ParentProfile
from django.forms import ModelForm, DateInput


class BabysitterProfileForm(forms.ModelForm):
    email = forms.EmailField(label='email')

    class Meta:
        model = BabysitterProfile
        fields = ['email', 'city', 'age', 'about', 'experienceYears']


class CreateSitterProfileForm(forms.ModelForm):
    class Meta:
        model = BabysitterProfile
        exclude = ['user']


class RecommendationsSitterForm(ModelForm):
    class Meta:
        model = RecommendationsOfSitter
        fields = ('recommendation',)


class CreateParentProfileForm(ModelForm):
    class Meta:
        model = ParentProfile
        exclude = ['user']


class ParentProfileForm(forms.ModelForm):
    email = forms.EmailField(label='email')

    class Meta:
        model = ParentProfile
        fields = ['email', 'city', 'kidsAge', 'about']


class RecommendationsParentForm(forms.ModelForm):
    class Meta:
        model = RecommendationsOfSitter
        fields = ('recommendation',)


# class EventForm(ModelForm):
#     class Meta:
#         model = Event
#         # datetime-local is a HTML5 input type, format to make date time show on fields
#         widgets = {
#             'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
#             'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
#         }
#         fields = '__all__'
#
#     def __init__(self, *args, **kwargs):
#         super(EventForm, self).__init__(*args, **kwargs)
#         # input_formats to parse HTML5 datetime-local input to datetime field
#         self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
#         self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)
#
#
# class MyAuthenticationForm(forms.Form):
#     """
#     Base class for authenticating accounts. Extend this to get a form that accepts
#     username/password logins.
#     """
#     username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True}))
#     password = forms.CharField(
#         label="Password",
#         strip=False,
#         widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}))
#
#
#     def __init__(self, request=None, *args, **kwargs):
#         """
#         The 'request' parameter is set for custom auth use by subclasses.
#         The form data comes in via the standard 'data' kwarg.
#         """
#         self.request = request
#         self.user_cache = None
#         super().__init__(*args, **kwargs)