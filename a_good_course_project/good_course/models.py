from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.core import validators

class School(models.Model):
        name = models.CharField(max_length=128, unique=True)
        tag = models.CharField(max_length=20, unique=True)

        def __unicode__(self):
                return self.name

class Course(models.Model):

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
                
        school_tag = models.CharField(max_length=20, choices=school_choices)
        school = models.ForeignKey(School)
        title = models.CharField(max_length=128, help_text ='Course title:' )
        slug = models.SlugField(unique=True)
        description = models.CharField(max_length=256, help_text ='Description: (max 256 characters)')
        lecturer = models.CharField(max_length=128, help_text ='Lecturer:')
        total_rating = models.IntegerField(default=0)
        quantity_ratings = models.IntegerField(default=0)
        average_rating = models.FloatField()

        def save(self, *args, **kwargs):
                self.slug = slugify(self.title)
                if (self.quantity_ratings > 0):
                        self.average_rating = self.total_rating/self.quantity_ratings
                else :
                        self.average_rating = 0
                super(Course, self).save(*args, **kwargs)

        def __unicode__(self):
                return self.title

class Review(models.Model):
        
        rating = models.IntegerField(validators=[validators.MaxValueValidator(5), validators.MinValueValidator(1)], help_text='Rate this course between 1 and 5')
        #comment = models.CharField(max_length=256, blank=True, help_text='Leave a comment')

        def __unicode__(self):
                return self.rating
        
class UserProfile(models.Model):

    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    # courses
    lecturer = models.BooleanField(default=False)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username

