from random import randint


from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from pattern.models import Item
# Create your views here.

def index(request):
	context = {}
	context['items'] = Item.objects.all()
	# hold = []
	# for item in context['items']:
	# 	hold.append(item.id)

	
	# # for i in range(0,20):
	# # 	hold.append(i)

	# context['hold'] = hold

	# max_value = max(hold)
	# min_value = min(hold)


	# randomized = []
	# while len(randomized) <= len(hold) - 1:
	# 	rand_num = randint(min_value, max_value)
	# 	if rand_num not in randomized:
	# 		randomized.append(rand_num)
	# t = {}
	# for i in randomized:
	# 	t[i] = Item.objects.get(unique_id=i)

	context['scrambled'] = Item.objects.all().order_by('?')


	hold = []
	for item in context['scrambled']:
		hold.append(item.id)


	context['hold'] = hold
	request.session['solution'] = hold
	# context['randomized'] = randomized
	return render(request, 'i/index.html', context)



def test(request):
	return HttpResponse(request.session['solution'])