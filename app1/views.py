from django.shortcuts import render
from django.http import HttpResponse

def display_data(request):
	data = '<marquee direction="right"><font size=10, color=blue>Welcome to Learn DJANGO Framework</font></marquee>'
	return HttpResponse(data)