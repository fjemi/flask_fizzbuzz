import json
from flask import render_template, flash, redirect, url_for
from app import app
from app.main.forms import ResultForm
from app.main import bp


@bp.route('/result/')
@bp.route('/result/<result_nums>')
def result(result_nums=None):
	numbers = []
	
	try:
		semi_position = result_nums.find('&')
		a = int(result_nums[:result_nums.find('&')])
		b = int(result_nums[result_nums.find('&') + 1:])
	except:
		pass
	
	if result_nums is None:
		a = 3
		b = 5
		flash('This example shows the FizzBuzz results for the numbers {} and {}'.format(a, b))
	'''elif semi_position < 0 or a not in range(1, 101) or b not in range(1, 101):
		return render_template('errors/500.html', title = '500 Error')'''
	
	c = a * b
	
	for i in range(1, 101):
		if i % c == 0:
			numbers.append('Fizz Buzz!')
		elif i % a == 0:
			numbers.append('Fizz')
		elif i % b == 0:
			numbers.append('Buzz')
		else:
			numbers.append(i)
			
	return render_template('main/result.html', title = 'Result', numbers=numbers, a=a, b=b, c=c)

@bp.route('/', methods=['POST', 'GET'])
def home():
	form = ResultForm()
	
	if form.validate_on_submit():
		flash('The Fizz Buzz results for numbers {} and {}'.format(form.num_fizz.data, form.num_buzz.data))	
		return redirect(url_for('main.result') + ('%d&%d' % (form.num_fizz.data, form.num_buzz.data)))	
	
	return render_template('main/home.html', title='Home', form=form)
