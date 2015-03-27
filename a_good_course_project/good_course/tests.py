from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from good_course.models import Course, Review, School


class CourseMethodTests(TestCase):

    def test_ensure_average_rating_is_correct(self):

        """
                ensure_average_rating_is_correct should results True for courses
                where average_rating = total_rating/quantity_ratings
        """
        school = School(name='test', tag='test')
        school.save()
        course = Course(school=school, title='test',description='test',lecturer='test', total_rating=6, quantity_ratings=2)
        course.save()
        self.assertEqual((course.average_rating == 3), True)

    def test_slug_creation(self):
        
        """
        slug_line_creation makes sure that the slug has been created properly
        """

        school = School(name='test', tag='test')
        school.save()
        course = Course(school=school, title='Test to be slugged',description='test',lecturer='test', total_rating=6, quantity_ratings=2)
        course.save()
  
        self.assertEqual(course.slug, 'test-to-be-slugged')

class ReviewMethodTests(TestCase):

    def test_ensure_rating_is_valid(self):

        """
            checks that the rating for a review cannot go out the bounds 0-5,
            if they do they should be defaulted to 0
        """
        
        school = School(name='test', tag='test')
        school.save()
        course = Course(school=school, title='test',description='test',lecturer='test', total_rating=6, quantity_ratings=2)
        course.save()
        user = User(username='test', password='test')
        user.save()
        negReview = Review(rating=-2, text='test', course=course, user=user)
        overReview = Review(rating=7, text='test', course=course, user=user)
        negReview.save()
        overReview.save()
        
        self.assertEqual((negReview.rating == 0), True)
        self.assertEqual((overReview.rating == 0), True)



class HomeViewTests(TestCase):
    
    def test_home_view_with_no_courses(self):
        
        """
        If no courses exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No courses currently.")
        self.assertQuerysetEqual(response.context['top_courses'], [])


    def test_home_view_with_courses(self):
        """
        Check that the top 9 courses are being displayed and that they are
        presented in a 3x3 grid
        """

        school = School(name='test',tag='test')
        school.save()
        course1 = Course(school=school,title='test1',description='test',lecturer='test',total_rating=1,quantity_ratings=1)
        course2 = Course(school=school,title='test2',description='test',lecturer='test',total_rating=1,quantity_ratings=1)
        course3 = Course(school=school,title='test3',description='test',lecturer='test',total_rating=1,quantity_ratings=1)
        course4 = Course(school=school,title='test4',description='test',lecturer='test',total_rating=1,quantity_ratings=1)
        course1.save()
        course2.save()
        course3.save()
        course4.save()
        
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test1")
        self.assertContains(response, "test2")
        self.assertContains(response, "test3")
        self.assertContains(response, "test4")

        num_top =len(response.context['top_courses'])
        num_mid =len(response.context['mid_courses'])
        num_bot =len(response.context['bot_courses'])
        self.assertEqual(num_top , 3)
        self.assertEqual(num_mid , 1)
        self.assertEqual(num_bot , 0)
        
class SchoolViewTests(TestCase):

    def test_school_view_filter(self):
        """
        Check that the correct courses are displayed in the school view
        """

        school1 = School(name='school1',tag='school1')
        school2 = School(name='school2', tag='school2')
        school1.save()
        school2.save()
        
        course1 = Course(school=school1,title='test1',description='test',lecturer='test',total_rating=1,quantity_ratings=1)
        course2 = Course(school=school1,title='test2',description='test',lecturer='test',total_rating=1,quantity_ratings=1)
        course3 = Course(school=school1,title='test3',description='test',lecturer='test',total_rating=1,quantity_ratings=1)
        course4 = Course(school=school2,title='test4',description='test',lecturer='test',total_rating=1,quantity_ratings=1)
        course1.save()
        course2.save()
        course3.save()
        course4.save()

        response = self.client.get(reverse('school', kwargs={'school_tag': 'school2'}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test4")

        num_top =len(response.context['top_courses'])
        num_mid =len(response.context['mid_courses'])
        num_bot =len(response.context['bot_courses'])
        self.assertEqual(num_top , 1)
        self.assertEqual(num_mid , 0)
        self.assertEqual(num_bot , 0)
    
