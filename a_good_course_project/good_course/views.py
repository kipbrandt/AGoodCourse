from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from good_course.forms import CourseForm, UserForm, UserProfileForm, ReviewForm
from good_course.models import School, Course

from datetime import datetime

def home(request):

    context_dict ={}
    course_list1 = Course.objects.order_by('-average_rating')[:3]
    course_list2 = Course.objects.order_by('-average_rating')[3:6]
    course_list3 = Course.objects.order_by('-average_rating')[6:9]
    context_dict['top_courses'] = course_list1
    context_dict['mid_courses'] = course_list2
    context_dict['bot_courses'] = course_list3

    response = render(request,'good_course/home.html', context_dict)

    return response
    
def school(request, school_tag):

    context_dict = {}
    
    try:
        school = School.objects.get(tag=school_tag)
        context_dict['school_name'] = school.name
        context_dict['school_tag'] = school.tag

        course_list1 = Course.objects.filter(school=school).order_by('-average_rating')[:3]
        course_list2 = Course.objects.filter(school=school).order_by('-average_rating')[3:6]
        course_list3 = Course.objects.filter(school=school).order_by('-average_rating')[6:9]
        context_dict['top_courses'] = course_list1
        context_dict['mid_courses'] = course_list2
        context_dict['bot_courses'] = course_list3
        context_dict['school'] = school
    except School.DoesNotExist:
        pass
           
    return render(request, 'good_course/school.html', context_dict)

def course(request, course_name_slug):

    context_dict = {}

    try:
        course = Course.objects.get(slug=course_name_slug)
        context_dict['title'] = course.title
        context_dict['title_slug'] = course.slug
        context_dict['school'] = course.school
        context_dict['desc'] = course.description
        context_dict['lecturer'] = course.lecturer
        context_dict['rating'] = course.average_rating
        context_dict['course'] = course

        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                course.total_rating = course.total_rating + form.cleaned_data['rating']
                course.quantity_ratings = course.quantity_ratings + 1
                course.save()
            else :
                print form.errors

        else:
            form = ReviewForm()
            
    except Course.DoesNotExist:
        pass

    context_dict['form'] = form
    return render(request, 'good_course/course.html', context_dict)

def add_course(request):
    
    if request.method == 'POST':
        form = CourseForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return home(request)
        else:
            print form.errors
    else:
        form = CourseForm()

    return render(request, 'good_course/add_course.html', {'form': form})

def register_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return home(request)
        
        else:
            print form.errors
    else:
        form = UserProfileForm()

    return render(request, 'good_course/profile_registration.html', {'form': form})

def profile(request):
    context_dict = {}


    return render(request, 'good_course/profile.html', context_dict)



