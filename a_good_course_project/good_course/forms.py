from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import HiddenInput
from good_course.models import Course, UserProfile, Review

class CourseForm(forms.ModelForm):
    school_choices = (
            ('business', 'Adam Smith Business School'),
            ('cardiovascular', 'Institute of Cardiovascular and Med Sci'),
            ('architecture', 'Mackintosh School of Architecture'),
            ('chemistry', 'School of Chemistry'),
            ('computing', 'School of Computing Science'),
            ('critical', 'School of Critical Studies'),
            ('culture', 'School of Culture and Creative Arts'),
            ('education', 'School of Education'),
            ('engineering', 'School of Engineering'),
            ('geography', 'School of Geography and Earth Sciences'),
            ('humanities', 'School of Humanities'),
            ('interdisciplinary', 'School of Interdisciplinary Studies'),
            ('law', 'School of Law'),
            ('life', 'School of Life Sciences'),
            ('maths', 'School of Mathematics and Statistics'),
            ('medicine', 'School of Medicine'),
            ('mlc', 'School of MLC'),
            ('physics', 'School of Physics and Astronomy'),
            ('psychology', 'School of Psychology'),
            ('social', 'School of Social and Political Sciences'),
            ('veterinary', 'School of Veterinary Medicine')
            )

    school = forms.ChoiceField(choices=school_choices, help_text='School')
    title = forms.CharField(max_length=128, help_text='Course Title')
    lecturer = forms.CharField(max_length=128, help_text='Lecturer')
    description = forms.CharField(max_length=256, help_text='Description')
    class Meta:
        model = Course
        fields = ('school', 'title', 'description', 'lecturer')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture','lecturer')

class ReviewForm(forms.ModelForm):
    text = forms.CharField(required=False, max_length=256, label='Leave a comment')
    class Meta:
        model = Review
        fields = ('rating','text')

    def __init__(self, *args, **kwargs):
        hide = kwargs.pop('hide',False)
        super(ReviewForm, self).__init__(*args, **kwargs)
        if hide:
            self.fields['rating'].widget=HiddenInput()
