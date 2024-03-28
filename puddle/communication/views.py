from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from item.models import *
from .forms import *
from .models import *

# Create your views here.


@login_required
def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)
    
    if item.created_by == request.user:
        return redirect('dashboard:index')
    
    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])
    
    if conversations:
        pass # redirect to conversation
    
    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        
        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()
            
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            
            return redirect('item:detail', pk=item_pk)
        else:
            form = ConversationMessageForm()
            
        return render(request, 'communication/new.html', {
            'form': form
        })
    else:
        t = loader.get_template("communication/new.html")
        c = {"foo": "bar"}
        return HttpResponse(t.render(c, request))
    
    
@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])
    
    return render(request, 'communication/inbox.html', {
        'conversations': conversations,
    })
    
@login_required
def detail(request, pk):
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)
    
    return render(request, 'communication/detail.html', {
        'conversation': conversation
    })