from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from pattern.models import Item
# Create your views here.

def index(request):
	context = {}
	return render(request, 'p/index.html', context)


def test(request):
	context = {}
	context['items'] = Item.objects.all()

	context['scrambled'] = Item.objects.all().order_by('?')

	solution_id = []
	for item in context['scrambled']:
		solution_id.append(item.id)

	solution_name = []
	for i in context['scrambled']:
		solution_name.append(str(i.unique_name))

	request.session['solution_name'] = solution_name
	# --Debug
	# context['hold'] = solution_name
	# context['randomized'] = solution_id
	# --Debug

	return render(request, 'p/test.html', context)

def check_result(request):
	context = {}
	solution_name = request.session['solution_name']

	hold = []

	if request.method == 'POST':
		for i in solution_name:
			a = request.POST.get(str(i))
			hold.append(a)

	user_answers = []
	final_answer = 0
	a = 0
	for i in hold:
		bit = None
		try:
			bit = Item.objects.get(unique_id=i)
			if bit != None:
				user_answers.append(bit.unique_name)

		except:
			user_answers.append('none')
			pass
		a += 1


	b = 0
	while b <= len(solution_name) - 1:
		if solution_name[b] == user_answers[b]:
			print 'yes', solution_name[b], solution_name[b]
			final_answer += 1
		b += 1


	context['final_answer'] = final_answer
	# --Debug
	# print 'len(hold)', len(hold)
	# print 'len(solution_name)', len(solution_name)
	# print 'len(user_answers)', len(user_answers)
	# print 'final_answer', final_answer
	# --Debug

	return render(request, 'p/result.html', context)