# encoding: utf-8
from __future__ import unicode_literals

from django.db import models
from coaches.models import Coach

class Course(models.Model):
    name = models.CharField(verbose_name='Name',max_length=200)
    short_description = models.CharField(verbose_name='Short description',max_length=1000)
    description = models.TextField(verbose_name='Description')
    coach = models.ForeignKey(Coach, blank=True, null=True, related_name='coach_courses' )
    assistant = models.ForeignKey(Coach, blank=True, null=True, related_name='assistant_courses')
    def __unicode__(self):
        return  self.name

class Lesson(models.Model):
    subject = models.CharField(verbose_name='Subject',max_length=200)
    description = models.TextField(verbose_name='Description')
    course = models.ForeignKey(Course,verbose_name='Courses')
    order = models.PositiveIntegerField(verbose_name='Order')
    
    def __unicode__(self):
        return  self.subject





