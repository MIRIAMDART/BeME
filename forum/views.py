# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .forms import QuestionForm, CommentForm
from .models import Question, Comment

# Create your views here.


def questions(request):
        """Displays all the questions"""
        questions = Question.objects.order_by('date_added')
        context = {'questions': questions}
        return render(request, 'forum/questions.html', context)


def question(request, question_id):
        """Displays specific question"""
        question = Question.objects.get(id=question_id)
        comments = question.comment_set.order_by('-date_added')
        context = {'question': question, 'comments': comments}
        return render(request, 'forum/question.html', context)


@login_required
def new_question(request):
        """Asking a new question"""
        if request.method != 'POST':
            # No data submitted; create a blank form.
            form = QuestionForm()
        else:
            # POST data submitted; process data.
            form = QuestionForm(request.POST)
            if form.is_valid():
                new_question = form.save(commit=False)
                new_question.owner = request.user
                new_question.save()
                return HttpResponseRedirect(reverse('forum:questions'))

        context = {'form': form}
        return render(request, 'forum/new_question.html', context)


@login_required
def new_comment(request, question_id):
    """Add a new comment for a particular question."""
    question = Question.objects.get(id=question_id)
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = CommentForm()
    else:
        # POST data submitted; process data.
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.question = question
            new_comment.save()
            return HttpResponseRedirect(reverse('forum:question', args=[question_id]))

    context = {'question': question, 'form': form}
    return render(request, 'forum/new_comment.html', context)


@login_required
def edit_comment(request, comment_id):
    """Editing an exsiting comment"""
    comment = Comment.objects.get(id=comment_id)
    question = comment.question

    if request.method != 'POST':
        # Filling up the for with the original comment.
        form = CommentForm(instance=comment)
    else:
        # POST data submitted; process data.
        form = CommentForm(instance=comment, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('forum:question', args=[question.id]))

    context = {'comment': comment, 'question': question, 'form': form}
    return render(request, 'forum/edit_comment.html', context)
