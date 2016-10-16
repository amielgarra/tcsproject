from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

class Thesis(models.Model):
    title = models.CharField(max_length=300,blank=False, unique=True)
    authors = models.CharField(max_length=300,blank=False)
    emails = models.EmailField(blank=False,default='')
    desc = models.TextField(blank=False)
    abstract = models.TextField(blank=False)
    no_of_pages = models.IntegerField(blank=False)
    date_published = models.DateField(auto_now=False, auto_now_add=False)
    date_added = models.DateField(auto_now=False, auto_now_add=True)
    DEPTS = [
     ('Accountancy','Accountancy'),
     ('Banking and Finance','Banking and Finance'),
     ('Management','Management'),
     ('Marketing','Marketing'),
     ('Customs Administration','Customs Administration'), 
     ('Hospitality Management','Hospitality Management'),
     ('Filipino','Filipino'),
     ('English and Foreign Language','English and Foreign Language'), 
     ('Physical Education','Physical Education'), 
     ('Social Science','Social Science'),
     ('Chemical Engineering','Chemical Engineering'), 
     ('Civil Engineering','Civil Engineering'), 
     ('Computer Engineering','Computer Engineering'), 
     ('Electrical Engineering','Electrical Engineering'),
     ('Electronics Engineering','Electronics Engineering'), 
     ('Industrial Engineering','Industrial Engineering'),
     ('Mechanical Engineering','Mechanical Engineering'), 
     ('Mining, Geology, and Ceramics Engineering','Mining, Geology, and Ceramics Engineering'),
     ('Biology','Biology'), 
     ('Chemistry','Chemistry'), 
     ('Computer Science','Computer Science'), 
     ('Mathematics','Mathematics'), 
     ('Psychology','Psychology'), 
     ('Information Technology and Management','Information Technology and Management')
     ]
    dept = models.CharField(max_length=300, choices = sorted(DEPTS), blank=False)
    CATEGORIES = [
    ('Books','Books'), 
    ('Business','Business'), 
    ('Catalogs','Catalogs'), 
    ('Education','Education'),
    ('Entertainment','Entertainment'), 
    ('Finance','Finance'), 
    ('Food and Drink','Food and Drink'), 
    ('Games','Games'), 
    ('Health and Fitness','Health and Fitness'),
    ('Lifestyle','Lifestyle'), 
    ('Magazines and Newspaper','Magazines and Newspaper'), 
    ('Medical','Medical'), 
    ('Music','Music'), 
    ('Navigation','Navigation'), 
    ('News','News'), 
    ('Photo and Video','Photo and Video'), 
    ('Productivity','Productivity'), 
    ('Reference','Reference'), 
    ('Shopping','Shopping'),
    ('Social Networking','Social Networking' ), 
    ('Sports','Sports'), 
    ('Travel','Travel'), 
    ('Utilities','Utilities'), 
    ('Weather','Weather')
    ]
    category = models.CharField(max_length=300, choices = sorted(CATEGORIES), blank=False)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title + " by " + self.authors
        
    class Meta:
        verbose_name='Thesis'

class Like(models.Model):
    thesis = models.ForeignKey(Thesis)
    session = models.CharField(max_length=500)

    def __str__(self):
        return str(self.thesis)