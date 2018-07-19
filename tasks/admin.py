# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from tasks.models import Topic, Note

# Register your models here.

admin.site.register(Topic)
admin.site.register(Note)