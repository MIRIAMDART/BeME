# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Question(models.Model):
    """A Question the user asks"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Comment(models.Model):
    """Comment under a particular question"""
    question = models.ForeignKey(Question)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'comments'

    def __str__(self):
        """Return a string representation of the model."""
        return self.text[:] + "..."
