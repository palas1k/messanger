from django.contrib.auth.models import User
from django.db.models import Q
from django.http import request
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from messenger.models import Message

class CreateMessageView(CreateView):
    model = Message
    template_name = 'messenger/createmessage.html'
    fields = ['addressee', 'text']
    success_url = '/chat/'

    def get_context_data(self, **kwargs):
        query = self.request.GET.get('q')
        context = super(CreateMessageView, self).get_context_data(**kwargs)
        context['users'] = User.objects.all()
        if query:
            context['messages_list'] = Message.objects.filter(Q(addressee__username__contains = query) | Q(author__username__contains = query))
            return context
        return context
