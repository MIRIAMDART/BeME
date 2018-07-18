# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .forms import TopicForm, NoteForm
from .models import Topic, Note

# Create your views here.

def index(request):
    """The home page for Checkify"""
    return render(request, 'tasks/index.html')


@login_required
def topics(request):
        """Displays all the Topics"""
        topics = Topic.objects.filter(owner=request.user).order_by('date_added')
        context = {'topics': topics}
        return render(request, 'tasks/topics.html', context)


@login_required
def topic(request, topic_id):
        """Displays all the Topics"""
        topic = Topic.objects.get(id=topic_id)
        if topic.owner != request.user:
            raise Http404
        notes = topic.note_set.order_by('-date_added')
        context = {'topic': topic, 'notes': notes}
        return render(request, 'tasks/topic.html', context)


@login_required
def new_topic(request):
        """Adding a new topic"""
        if request.method != 'POST':
            # No data submitted; create a blank form.
            form = TopicForm()
        else:
            # POST data submitted; process data.
            form = TopicForm(request.POST)
            if form.is_valid():
                new_topic = form.save(commit=False)
                new_topic.owner = request.user
                new_topic.save()
                return HttpResponseRedirect(reverse('tasks:topics'))
        
        context = {'form': form}
        return render(request, 'tasks/new_topic.html', context)


@login_required
def new_note(request, topic_id):
    """Add a new note for a particular topic."""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = NoteForm()
    else:
        # POST data submitted; process data.
        form = NoteForm(data=request.POST)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.topic = topic
            new_note.save()
            return HttpResponseRedirect(reverse('tasks:topic', args=[topic_id]))
    
    context = {'topic': topic, 'form': form}
    return render(request, 'tasks/new_note.html', context)


@login_required
def edit_note(request, note_id):
    """Editing an exsiting note"""
    note = Note.objects.get(id=note_id)
    topic = note.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Filling up the for with the original note.
        form = NoteForm(instance=note)
    else:
        # POST data submitted; process data.
        form = NoteForm(instance=note, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tasks:topic', args=[topic.id]))

    context = {'note': note, 'topic': topic, 'form': form}
    return render(request, 'tasks/edit_note.html', context)
