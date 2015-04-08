from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from pattern.models import Item
# Create your views here.
def index(request):
	context = {}
	context['items'] = Item.objects.all()
	return render(request, 'i/index.html', context)