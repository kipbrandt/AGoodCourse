from django import forms
from django.contrib.auth.models import User
from good_course.models import Course, UserProfile, Review

class CourseForm(forms.ModelForm):
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
    class Meta:
        model = Review
        fields = ('rating',)
