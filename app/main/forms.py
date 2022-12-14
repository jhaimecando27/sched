from django import forms

class facultyForm(forms.Form):
    inputId = forms.CharField(max_length=100)
    inputFirstName = forms.CharField(max_length=100)
    inputLastName = forms.CharField(max_length=100)
    inputEmail = forms.CharField(max_length=100)
    inputEmployeeStatus = forms.CharField(max_length=100)
    inputDay = forms.CharField(max_length=100)
    inputStartTime = forms.CharField(max_length=100)
    inputEndTime = forms.CharField(max_length=100)
