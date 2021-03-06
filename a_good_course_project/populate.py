import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'a_good_course_project.settings')

import django
django.setup()

from good_course.models import Course, School, UserProfile
from django.contrib.auth.models import User


def populate():
    business = add_school('Adam Smith Business School','business')
    cardiovascular = add_school('Institute of Cardiovascular and Med Sci','cardiovascular')
    architecture = add_school('Mackintosh School of Architecture','architecture')
    chemistry = add_school('School of Chemistry','chemistry')
    computing = add_school('School of Computing Science','computing')
    critical = add_school('School of Critical Studies','critical')
    culture = add_school('School of Culture and Creative Arts','culture')
    education = add_school('School of Education','education')
    engineering = add_school('School of Engineering','engineering')
    geography = add_school('School of Geography and Earth Sciences','geography')
    humanities = add_school('School of Humanities','humanities')
    interdisciplinary = add_school('School of Interdisciplinary Studies','interdisciplinary')
    law = add_school('School of Law','law')
    life = add_school('School of Life Sciences','life')
    maths = add_school('School of Mathematics and Statistics','maths')
    medicine = add_school('School of Medicine','medicine')
    mlc = add_school('School of MLC','mlc')
    physics = add_school('School of Physics and Astronomy','physics')
    psychology = add_school('School of Psychology','psychology')
    social = add_school('School of Social and Political Sciences','social')
    vet = add_school('School of Veterinary Medicine','veterinary')

    add_course(business, 'business 101', 'basics', 'lecturer', 5, 2)
    add_course(business, 'business 102', 'basics + more', 'lecturer', 4, 2)
    add_course(law, 'law 101', 'basics', 'law lecturer', 15, 4)
    add_course(maths, 'maths 101', 'basics', 'maths lecturer', 3, 1)
    add_course(physics, 'physics 101', 'basics', 'physics lecturer', 2, 2)
    add_course(social, 'social 101', 'basics', 'social lecturer', 8, 2)
    add_course(life, 'life 101', 'basics', 'life lecturer', 3, 2)

    test = User.objects.create_user('test','test@test.com','test')
    testProfile = UserProfile.objects.get_or_create(user=test, lecturer=False)[0]
    test.save()
    testProfile.save()

def add_course(school, title, desc, lecturer, total_rate, rate_quant):
    c = Course.objects.get_or_create(school=school, title=title, description=desc, lecturer=lecturer, total_rating=total_rate, quantity_ratings=rate_quant)[0]
    return c

def add_school(name,tag):
    s = School.objects.get_or_create(name=name, tag=tag)[0]
    return s

# Start execution here!
if __name__ == '__main__':
    print "Starting Good Course population script..."
    populate()
