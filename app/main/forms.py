from django import forms
from .models import Course, Faculty, Department, Subject, Availability, EMPLOYMENT_TYPE_CHOICES, COLLEGE_CHOICES


class FacultyForm(forms.ModelForm):
    course_id = forms.ModelChoiceField(
        Course.objects.all(), empty_label="test")
    employment_status = forms.ChoiceField(
        widget=forms.RadioSelect, choices=EMPLOYMENT_TYPE_CHOICES)

    class Meta:
        model = Faculty
        fields = ['college_id', 'course_id',
                  'employment_status', 'name', 'school_id']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course_id'].queryset = Course.objects.none()

        if 'college_id' in self.data:
            try:
                college_id = int(self.data.get('college_id'))
                self.fields['course_id'].queryset = Course.objects.filter(
                    college_id=college_id).order_by('college_id')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['course_id'].queryset = self.instance.department.course


class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = Availability
        fields = ['week_day', 'start_time', 'end_time']
