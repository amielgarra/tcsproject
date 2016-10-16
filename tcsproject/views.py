from django.http import HttpResponse, HttpResponseRedirect,Http404
from django.shortcuts import get_object_or_404, render, redirect
from .models import Thesis, Like
from .forms import AddThesisForm, ContactForm, LikeForm, SearchForm
from django.contrib.auth.models import User
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.contrib import messages
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random
import datetime, time
import collections
from django.template import Context

def home(request):
    template_name = 'tcsproject/home.html'
    user = request.user
    ts = time.time()
    session_id = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d')
    request.session['session_id'] = session_id
    likeform = LikeForm()
    likes = collections.Counter(Like.objects.all())
    print likes
    thesis = Thesis.objects.all()
    
    thesis_likes = {}
    for i in thesis:
    	thesis_likes[i.title] = len(Like.objects.filter(thesis = i))

    if request.method == 'POST':
    	contactform = ContactForm(request.POST)
    	if contactform.is_valid():
    		contact = contactform.save(commit=False)
    		contact.save()
    else:
    	contactform = ContactForm()
    print thesis_likes


    allthesis = Thesis.objects.all()
    paginator = Paginator(allthesis, 4)

    page = request.GET.get('page')
    try:
        thesis_by_8 = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        thesis_by_8 = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        thesis_by_8 = paginator.page(paginator.num_pages)
    
    context = {'recently_added': Thesis.objects.order_by('-date_added')[:4]
    ,
               'featured' : Thesis.objects.order_by('-likes')[:4],
               'contactform':contactform,
               'session':session_id,
               'likeform':likeform,
               'likes': thesis_likes
              }
    return render(request, template_name, context)


def viewall(request):
    template_name = 'tcsproject/viewall.html'
    allthesis = Thesis.objects.all()
    paginator = Paginator(allthesis, 8)

    page = request.GET.get('page')

    try:
        thesis_by_8 = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        thesis_by_8 = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        thesis_by_8 = paginator.page(paginator.num_pages)

    thesis = Thesis.objects.all()
    thesis_likes = {}
    for i in thesis:
        thesis_likes[i.title] = len(Like.objects.filter(thesis = i))

    context = {'viewall': thesis_by_8,
    'likes': thesis_likes
            }
    return render(request, template_name, context)

def viewallbyauthor(request):
    template_name = 'tcsproject/viewall.html'
    allthesis = Thesis.objects.all().order_by('-authors')
    paginator = Paginator(allthesis, 8)

    page = request.GET.get('page')

    try:
        thesis_by_8 = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        thesis_by_8 = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        thesis_by_8 = paginator.page(paginator.num_pages)

    thesis = Thesis.objects.all()
    thesis_likes = {}
    for i in thesis:
        thesis_likes[i.title] = len(Like.objects.filter(thesis = i))

    context = {'viewall': thesis_by_8,
    'likes': thesis_likes
            }
    return render(request, template_name, context)

def viewallbypublished(request):
    template_name = 'tcsproject/viewall.html'
    allthesis = Thesis.objects.all().order_by('-date_published')
    paginator = Paginator(allthesis, 8)

    page = request.GET.get('page')

    try:
        thesis_by_8 = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        thesis_by_8 = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        thesis_by_8 = paginator.page(paginator.num_pages)

    thesis = Thesis.objects.all()
    thesis_likes = {}
    for i in thesis:
        thesis_likes[i.title] = len(Like.objects.filter(thesis = i))

    context = {'viewall': thesis_by_8,
    'likes': thesis_likes
            }
    return render(request, template_name, context)

def viewallbyadded(request):
    template_name = 'tcsproject/viewall.html'
    allthesis = Thesis.objects.all().order_by('-date_added')
    paginator = Paginator(allthesis, 8)

    page = request.GET.get('page')

    try:
        thesis_by_8 = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        thesis_by_8 = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        thesis_by_8 = paginator.page(paginator.num_pages)

    thesis = Thesis.objects.all()
    thesis_likes = {}
    for i in thesis:
        thesis_likes[i.title] = len(Like.objects.filter(thesis = i))

    context = {'viewall': thesis_by_8,
    'likes': thesis_likes
            }
    return render(request, template_name, context)


def categories(request,id=id):
    template_name = 'tcsproject/categories.html'
    thesis_likes = {}
    thesis_by_8 = []
    if not len(Thesis.objects.filter(category=id)) == 0:
        thesis_by_8 = Thesis.objects.filter(category=id)
        thesis = Thesis.objects.all()
        for i in thesis:
            thesis_likes[i.title] = len(Like.objects.filter(thesis = i))
        paginator = Paginator(thesis_by_8, 8)

        page = request.GET.get('page')

        try:
            thesis_by_8 = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            thesis_by_8 = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            thesis_by_8 = paginator.page(paginator.num_pages)

    else:
        thesis_by_8 = 'None'

    context = {'categories' : thesis_by_8,
			   'category' : id,
               'likes':thesis_likes
			  }
    return render(request, template_name, context)

def viewthesis(request, id=id):
	template_name = 'tcsproject/thesis.html'
	context = {'topic' : Thesis.objects.get(pk=id)}
	return render(request, template_name, context)

def addnewthesis(request):
	template_name = 'tcsproject/new.html'
	if request.user.is_authenticated:
		if request.method == 'POST':
			form = AddThesisForm(request.POST)
			if form.is_valid():
				thesis = form.save(commit=False)
				thesis.save()
				return HttpResponseRedirect('/tcsproject/home/')
		else:
			form = AddThesisForm()
	else:
		raise Http404("Page does not exist")
	context = {'newthesis':form}
	return render(request, template_name, context)

def deletethesis(request,id=id):
    if request.user.is_authenticated:
	   Thesis.objects.filter(id=id).delete()
	   return HttpResponseRedirect('/tcsproject/home/')
    else:
        raise Http404("Page does not exist")

def sendemail(request):
    if request.method == 'POST':
        contactform = ContactForm(request.POST)
        if contactform.is_valid():
            email = contactform.data['email']
            msg = contactform.data['message']
            send_mail('A comment to your thesis', msg, '<amiel.garra@outlook.com>', [email])
            return HttpResponse('Success')
    else:
        contactform = ContactForm()
    return HttpResponse('HEY')

def likethesis(request, thesis, session_id):
    t = Thesis()
    t = Thesis.objects.get(title=thesis)
    if len(Like.objects.filter(thesis=t, session=session_id)) == 0:
    	like = Like()
    	like.thesis = t
    	like.session = session_id
    	like.save()
    	messages.add_message(request, messages.SUCCESS, 'You liked ' + t.title +".")
        return redirect('/tcsproject/thesis/'+str(t.id))
    else:
        messages.add_message(request, messages.SUCCESS, 'You already liked ' + t.title +".")
    	return redirect('/tcsproject/thesis/'+str(t.id))

def searchthesis(request, thesis):
    template_name = 'tcsproject/results.html'
    ts = time.time()
    session_id = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d')
    request.session['session_id'] = session_id
    if thesis == "":
        return HttpResponseRedirect('/tcsproject/home/')
    results = Thesis.objects.filter(title__icontains = thesis)
    print results   
    likeform = LikeForm()
    likes = collections.Counter(Like.objects.all())
    print likes
    thesis = Thesis.objects.all()
    thesis_likes = {}
    for i in thesis:
        thesis_likes[i.title] = len(Like.objects.filter(thesis = i))
    if request.method == 'POST':
        contactform = ContactForm(request.POST)
        if contactform.is_valid():
            contact = contactform.save(commit=False)
            contact.save()
    else:
        contactform = ContactForm()
    print thesis_likes

    paginator = Paginator(results, 8)

    page = request.GET.get('page')

    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        results = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        results = paginator.page(paginator.num_pages)

    thesis = Thesis.objects.all()

    context = {'results':results,
               'contactform':contactform,
               'session':session_id,
               'likeform':likeform,
               'likes':thesis_likes}

    return render(request, template_name, context)


def thesis_view(request, id=id):
    template_name='tcsproject/thesis.html'
    user = request.user
    ts = time.time()
    session_id = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d')
    request.session['session_id'] = session_id
    likeform = LikeForm()
    likes = collections.Counter(Like.objects.all())
    print likes
    thesis = Thesis.objects.all()
    thesis_likes = {}
    for i in thesis:
        thesis_likes[i.title] = len(Like.objects.filter(thesis = i))
    if request.method == 'POST':
        contactform = ContactForm(request.POST)
        if contactform.is_valid():
            contact_name = request.POST.get('name','')
            message = request.POST.get('message','')
            template = get_template('tcsproject/email_temp.txt')
            t = Thesis.objects.get(pk=id)
            email = t.emails
            context = Context({'name': contact_name,'message': message, 'thesis_title':t.title})
            content = template.render(context)
            email = EmailMessage("A Message To A Thesis", content, "amiel.garra@outlook.com",['Amiel Garra <amiel.garra@outlook.com>'],headers = {'Reply-To': t })
            email.send()
            messages.add_message(request, messages.SUCCESS, "Message sent!")
            return redirect('/tcsproject/thesis/'+str(t.id))
    else:
        contactform = ContactForm()
    print thesis_likes

    context = {'topic':Thesis.objects.get(pk=id),
               'contactform':contactform,
               'session':session_id,
               'likeform':likeform,
               'likes': thesis_likes
              }
    return render(request,template_name,context)