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

	solution = []
	for i in context['scrambled']:
		solution.append(str(i.unique_name))

	request.session['solution'] = solution

	return render(request, 'p/test.html', context)





def check_result(request):
	context = {}
	solution = request.session['solution']


	# should hold the numbers entered
	# represents the unique_id field
	hold = []
	# record all inputs in a list, including empty inputs
	if request.method == 'POST':
		for i in solution:
			a = request.POST.get(str(i))
			hold.append(a)

	user_answers = []

	# get the unique_id of each entry in the same way
	# they were displayed in the test using hold
	for i in hold:
		bit = None
		try:
			bit = Item.objects.get(unique_id=i)
			if bit != None:
				user_answers.append(bit.unique_name)

		except:
			user_answers.append('none')
			pass


	i = 0
	final_answer = 0
	# compare solution recorded with the one provided by user
	while i <= len(solution) - 1:
		if solution[i] == user_answers[i]:
			final_answer += 1
		i += 1


	context['final_answer'] = final_answer

	return render(request, 'p/result.html', context)