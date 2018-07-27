from django.shortcuts import render

# Create your views here.
def index (request):
	
	poste = [
		{'id' : 1,'title' : 'first post', 'body' : 'this is my first post'},
		{'id' : 2,'title' : 'second post', 'body' : 'this is my second post'},
		{'id' : 3,'title' : 'third post', 'body' : 'this is my third post'},
	]
	return render (request,'myblog/index.html', {'poste' : poste})
