# Create your views here.
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.shortcuts import render_to_response
from comics.comic.models import Comic
from django.http import HttpResponse 
from comics.comic.forms import AddComic
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
import re


#This function is called when you want to add a comic
@login_required
def add_comic(request):
	if request.method == 'POST':	#Checking if data is submitted form POST or nor
		form = AddComic(request.POST, request.FILES) #Storing the detials entered from form into "form" variable (Note: request.FILES Parmeter is only requited when there is a file upload, in this case comic image is being uploaded) 
		if form.is_valid(): #Checking is the form valid accoring to the constrains speicied in the forms file
			cd = form.cleaned_data #Making form in proper format and storing it in cd variable
			#Following lines store the data into the database
			comic = Comic(name=cd['name'],
			comic_image=cd['comic'],
			description=cd['description'])
			comic.save()
			#if save sucessfull then redirect to the first comic
			return HttpResponseRedirect('/comics/1/')
		else:
			#if save failed then display the form again with errors
			return render_to_response('add_comic.html',
			{'form':form},context_instance=RequestContext(request))
	else: #if the data is not submitted form the POST method then display the form again
		form = AddComic()
		return render_to_response('add_comic.html',
		{'form':form},context_instance=RequestContext(request))
		

#This is used to display the comics
def display_comic(request, offset=1): #here offset is the comic number, if no number is provided then go to default 1
	offset  = int(offset) #Storing the passed offset into offset variable and converting it into int

	if offset <= len(Comic.objects.all()): #If the length of offset is less than or equal to the number of comics in the database then coniinue processing
		#inefficent code
		comics = Comic.objects.all() #Fetching all the comics form the database and storing it in "comics" variable
		prev_link = ''
		next_link = ''
		c =  comics[offset-1] #Storing the queried comic in variable "c", comics in the database are indexed from 0 and offset is provided from 1, hence -1 is used
		if offset > 1: #If the fetched object is not the first variable then generate previous link
			#Generates the prev link
			prev_link = re.sub('/\d+/$','/',str(request.path)) + str(offset-1)

		if offset < len(Comic.objects.all()): #if offset is not the last variable then genrate next link
			#Generates the next link	
			next_link = re.sub('/\d+/$','/',str(request.path)) + str(offset+1)
		
		#Passing fetched data to the template
		return render_to_response('comics.html',{'comic_name':c.name,
		'image':c.comic_image,
		'description':c.description,
		'comics':comics,
		'next':next_link,'prev':prev_link},context_instance=RequestContext(request))
