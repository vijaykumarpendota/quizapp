from django.db import models
#from django.core.urlresolvers import reverse

# Create your models here.

#creating the Course model for adding the questions
class Course(models.Model):
    course_name=models.CharField(max_length=100)
    def __str__(self):
        return self.course_name

class Question(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    #slug=models.SlugField(max_length=100)
    question=models.CharField(max_length=100)
    answer=models.CharField(max_length=100)
    option_one=models.CharField(max_length=100)
    option_two=models.CharField(max_length=100)
    option_three=models.CharField(max_length=100, blank=True)
    option_four=models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.question

    



