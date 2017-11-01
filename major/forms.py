from django import forms
 
class UserForm(forms.Form):
    #to take the input of username
    name = forms.CharField(max_length=140)
    password =forms.CharField(max_length=140)