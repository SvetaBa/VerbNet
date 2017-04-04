import json, time

from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.utils import timezone
from .forms import ContactForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.template import RequestContext
from django.core.mail import mail_admins
from django.conf import settings
from django.http import JsonResponse

from .models import Synset, SubSynset


def index(request):
    return render(request, 'VerbNet/index.html', {})


def synsets(request):
    synsets = [{'predicates': x['predicates'], 'id': x['id']} for x in Synset.objects.all().values() if x['predicates']]
    return render(request, 'VerbNet/synsets.html', {'synsets': synsets})

def synset(request, id):
    synset = Synset.objects.get(pk=id).predicates
    verbs = SubSynset.objects.filter(synset__id=id)
    return render(request, 'VerbNet/synset.html', {'verbs': verbs, 'synset': synset})


def graphs(request):
    return render(request, 'VerbNet/graphs.html', {})


def verbnet(request):
    return render(request, 'VerbNet/verbnet.html', {})


def about(request):
    return render(request, 'VerbNet/about.html', {})


# def contacts(request):
#     return render(request, 'VerbNet/contacts.html', {})


# def thanks(request):
#     return HttpResponse('Thank you for your message.')


def sendemail(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        mess = 'something wrong!'
        if form.is_valid():
            sender = form.cleaned_data['sender']
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            mess = 'Thank you for your message.'

            recipients = ['rus.verbnet@gmail.com']

            if name and message and sender:
                try:
                    send_mail(name, message + '\n' + sender, sender, recipients, fail_silently=False)
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')

        return HttpResponse(json.dumps({'message': mess}))
            # return HttpResponseRedirect('/thanks/')
    else:
      form = ContactForm()
    return render(request, 'VerbNet/contacts.html', {'form': form})
    