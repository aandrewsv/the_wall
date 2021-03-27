from django.http import request
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def wall(request):
    if 'userid' in request.session:
        context = {
            'user': User.objects.get(id=request.session['userid']),
            'all_messages': Message.objects.all(),
        }
        return render(request, 'wall.html', context)
    else:
        messages.error(request, "Please log in first!")
        return redirect('/')

def message_post(request):
    Message.objects.create(
        user_id = User.objects.get(id=request.session['userid']),
        message = request.POST['message']
    )
    messages.success(request, "Succesfully posted a message in The Wall!")
    return redirect('/wall')

def delete_message(request, idn):
    if 'userid' in request.session:
        this_message = Message.objects.get(id=idn)
        this_message.delete()
        messages.success(request, "Succesfully deleted a message in The Wall!")
        return redirect('/wall')
    else:
        messages.error(request, "Please log in first!")
        return redirect('/')

def comment_post(request):
    Comment.objects.create(
        message_id = Message.objects.get(id=request.POST['message_id']),
        user_id = User.objects.get(id=request.session['userid']),
        comment = request.POST['comment']
    )
    messages.success(request, "Succesfully posted a comment in The Wall!")
    return redirect('/wall')