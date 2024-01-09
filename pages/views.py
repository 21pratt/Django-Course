from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs): #*args, **kwargs
	print(args, kwargs)
	print(request.user)
	# return HttpResponse("<h1>Hello World</h1>") #srting of HTML code
	return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
	# return HttpResponse("<h1>Contact Page</h1>")
	return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
	my_context = {
		"my_text": "This is about us",
		"this_is_true": True,
		"my_number": 123,
		"my_list": [123, 415, 7, 'hello', 'django'],
		"my_html": "<h1>Hi Pratt!</h1>",

	}
	# return HttpResponse("<h1>About Page</h1>")
	return render(request, "about.html", my_context)

def career_view(request, *args, **kwargs):
	# return HttpResponse("<h1>Career Page</h1>")
	return render(request, "career.html", {})