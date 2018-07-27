from django.shortcuts import render
def home(request):
	return render (request, 'home.html')
def aboutus(request):
	return render (request, 'page/aboutus.html')
def contact(request):
	return render (request, 'page/contact.html')
def showroom(request):
	return render (request, 'page/showroom.html')
