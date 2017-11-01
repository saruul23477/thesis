from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.response import TemplateResponse
from .models import users, research as res, diplom as db_dip, detail, plan
from .forms import ProfileForm
from django.conf import settings
from django.conf.urls.static import static
from django.core.files import File
from django.db.models.functions import TruncDate

def enter(request):
	if 'code'  in request.session:
		if len(request.session['code'])==6:
			return teacher(request)
		elif len(request.session['code'])==10:	
			return student(request)

	if request.method == 'POST':  
		tmp=request.POST.get('tmp', '')
		
		if tmp=='logup':   
			try:
				n_mail=request.POST.get('mail', '')
				n_code=request.POST.get('code', '')
				n_pass=request.POST.get('password', '')
				n_lname=request.POST.get('lname', '')
				n_fname=request.POST.get('fname', '')
				phone=request.POST.get('phone', '')
				new_users=users.objects.create(mail=n_mail, code=n_code, password=n_pass, lname=n_lname, fname=n_fname, phone=phone )			

				return TemplateResponse(request, 'enter.html', {'log_up_sms': 'Бүртгэл амжилттай болсон. Та нэвтэрч орон уу'})
			except Exception as e:
				if str(e).find('code')>-1:
					return TemplateResponse(request, 'enter.html', {'log_up_sms': 'Код давхардсан байна'})
				else:
					return TemplateResponse(request, 'enter.html', {'log_up_sms': 'Алдаа гарсан'})
		elif tmp=='login':
			try:
				login_users=users.objects.get(code=request.POST.get('code', ''),  password=request.POST.get('password', ''))
				request.session['code']=request.POST.get('code', '')
				if len(request.POST.get('code', ''))==6:
					return redirect('teacher')
				elif len(request.POST.get('code', ''))==10:	
					return redirect('student')
			except Exception as e:
				return TemplateResponse(request, 'enter.html', {'message': 'Алдаа гарсан'})

		else:
			return render(request, 'enter.html')
	else:
		return render(request, 'enter.html')

def logout(request, ):
	if 'code' in request.session:
		del request.session['code']
		return redirect('enter')
	else:
		return redirect('enter')



def def_tosol(request):
	print(xaxa)



# parts for teacher
def teacher(request):
	if 'code' not in request.session:
		return enter(request)
	if len(request.session['code'])==10:	
		return student(request)
	user=users.objects.get(code=request.session['code'])
	try:
		researchs=res.objects.all().filter(user_id=request.session['code'])
	except Exception as e:
		error=e
	if user.degree== None or user.degree=='':	
		degree='no'	
		try:
			if request.method == 'POST':
				user.degree=request.POST.get('degree', '')
				user.save()
				return redirect('teacher')
		except Exception as e:
			print(e)
	else:
		degree=user.degree

	profile='True'

	context = {
		'image':'dist/img/default.png', 
		'status':'Багш',		
		'user':user,
		'researchs':researchs, 
		'degree':degree
			
	}

	if user.erhlegch==True:
		context['erhlegch']='True'
		if request.method == 'GET' :  
			if request.GET and request.GET['nariin'] :
				teachs=users.objects.all().filter(code__iregex=r'^.{6}$')
				context['teachs']=teachs
	if user.nariin==True:
		context['nariin']='True'
		if request.method == 'GET' :  
			if request.GET:
				if request.GET['add_st']=='tosol':					
					new_dip_uz=users.objects.get(code=request.GET['code'])
					new_dip_uz.tos=True;
					new_dip_uz.save()
				elif request.GET['add_st']=='diplom':					
					new_dip_uz=users.objects.get(code=request.GET['code'])
					new_dip_uz.dip=True;
					new_dip_uz.save()
				elif request.GET['add_st']=='hasah':
					try:	
						if request.GET['has']=='dip':	
							print('diplom hasah')			
							new_dip_uz=users.objects.get(code=request.GET['code'], dip=True)
							new_dip_uz.dip=False;
							new_dip_uz.save()
					except Exception as e:
						print(e)
					try:
						if request.GET['has']=='tos':
							print('tosol hasah')					
							new_dip_uz=users.objects.get(code=request.GET['code'], tos=True)
							new_dip_uz.tos=False;
							new_dip_uz.save()
					except Exception as e:
						print(e)			
			
				st_s=users.objects.all().filter(code__iregex=r'^.{10}$', dip=False) | users.objects.all().filter(code__iregex=r'^.{10}$', tos=False)
				context['st_s']=st_s
				st_dip_uz=users.objects.all().filter(code__iregex=r'^.{10}$', dip=True)
				context['st_dip_uz']=st_dip_uz
				st_tos_uz=users.objects.all().filter(code__iregex=r'^.{10}$', tos=True)
				context['st_tos_uz']=st_tos_uz
				profile='False'
				del context['researchs']



	context['profile']=profile
	return TemplateResponse(request, 'teacher.html', context)

def save_nariin(request):
	if request.method == 'POST':
		print('*'*10)
		nb=users.objects.get(code=request.POST.get('n_songolt', ''))
		nb.nariin=True;
		nb.save();
		return redirect('teacher')


def change_teach(request):
	if 'code' not in request.session:
		return enter(request)
	user=users.objects.get(code=request.session['code'])
	try:
		researchs=res.objects.all().filter(user_id=request.session['code'])
	except Exception as e:
		error=e
	if user.degree== None or user.degree=='':	
		degree='no'	
		try:
			if request.method == 'POST':
				user.degree=request.POST.get('degree', '')
				user.save()	
		except Exception as e:
			print(e)
	else:
		degree=user.degree



	if request.method == "POST":
		if request.FILES['image']:
			up_file = request.FILES['image']
			destination = open('/home/nuna/thesis/media/my_app/static/avatar/'+ up_file.name , 'wb')
			for chunk in up_file.chunks():
			    destination.write(chunk)
			destination.close()
			user.avatar='my_app/static/avatar/'+up_file.name
			user.save()
		user.mail=request.POST.get('mail', '')
		user.lname=request.POST.get('lname', '')
		user.fname=request.POST.get('name', '')
		user.phone=request.POST.get('phone', '')
		user.save()
		return redirect('teacher')
	
	
	if len(request.session['code'])==6:
		context = {
		'status':'Багш',		
		'user':user,
		'image':'dist/img/default.png',
		'researchs':researchs, 
		'degree':degree, 
		'change':'True' ,
		'profile':'True' 
		}
		return TemplateResponse(request, 'teacher.html', context)
	elif len(request.session['code'])==10:	
		context = {
		'status':'Оюутан',		
		'user':user,
		'image':'dist/img/default.png',
		'change':'True' ,
		'profile':'True' 
		}
		return TemplateResponse(request, 'student.html', context)
	


def research(request):
	

	if 'code' not in request.session:
		return enter(request)
	if len(request.session['code'])==10:	
		return student(request)
	user=users.objects.get(code=request.session['code'])
	img='dist/img/default.png'
	if user.avatar:
		img=user.avatar

	try:
		researchs=res.objects.all().filter(user_id=request.session['code'])
	except Exception as e:
		error=e
	add_sms=''
	if request.method == 'POST':  
		tmp=request.POST.get('sudalgaa', '')
		if tmp=='sudalgaa':
			try:
				n_topic=request.POST.get('topic', '')
				n_note=request.POST.get('note', '')
				new_users=res.objects.create(user_id=user, topic=n_topic, note=n_note)			

				add_sms='амжилттай болсон'
			except Exception as e:
				print(e)
	context = {
		'image':'dist/img/default.png', 
		'status':'Багш' , 
		'user':user,
		'research':'True',
		'researchs':researchs
	}
	if user.erhlegch==True:
		context['erhlegch']='True'
	return TemplateResponse(request, 'teacher.html', context)



def diplom(request):
	if 'code' not in request.session:
		return enter(request)
	if len(request.session['code'])==10:	
		return student(request)
	user=users.objects.get(code=request.session['code'])
	
	add_sms=''

	try:
		diploms=db_dip.objects.all().filter(user_id=request.session['code'], diplom=True)
	except Exception as e:
		error=e

	try:
		tosols=db_dip.objects.all().filter(user_id=request.session['code'], tosol=True)
	except Exception as e:
		error=e
	try:
		researchs=res.objects.all().filter(user_id=request.session['code'])
	except Exception as e:
		error=e

	if request.method == 'POST':  
		tmp=request.POST.get('dip', '')
		if tmp=='dip':
			try:
				n_topic=request.POST.get('topic', '')
				n_note=request.POST.get('note', '')
				n_diplom=request.POST.get('diplom', '')
				n_tosol=request.POST.get('tosol', '')
				if n_diplom and n_tosol:
					new_dip=db_dip.objects.create(user_id=user, topic=n_topic, note=n_note, diplom=True, tosol=True)
				elif n_diplom:
					new_dip=db_dip.objects.create(user_id=user, topic=n_topic, note=n_note, diplom=True)
				elif n_tosol:
					new_dip=db_dip.objects.create(user_id=user, topic=n_topic, note=n_note, tosol=True)
				else:
					context = {
						'image':'dist/img/default.png', 
						'status':'Багш' , 
						'diplom':'True',
						'error_dip':'Алдаа гарсан'
					}
					
					return TemplateResponse(request, 'teacher.html', context)					
				#new_users=res.objects.create(user_id=user, topic=n_topic, note=n_note)			

				add_sms='амжилттай болсон'
			except Exception as e:
				print(e)
	context = {
		'image':'dist/img/default.png', 
		'status':'Багш' , 
		'user':user,
		'diplom':'True',
		'diploms':diploms,
		'tosols':tosols,
		'researchs':researchs
	}
	if user.erhlegch==True:
		context['erhlegch']='True'
	
	return TemplateResponse(request, 'teacher.html', context)



def student(request):
	if 'code' not in request.session:
		return enter(request)
	if len(request.session['code'])==6:
		return teacher(request)


	user=users.objects.get(code=request.session['code'])
	context = {
		'image':'dist/img/default.png',
		'user':user, 
		'status':'Оюутан',
		'profile':'True'  
	}

	if user.songoson==True:
		try:
			this_det_tos=list(detail.objects.all().filter(st_id=request.session['code'], tos=True))
			context['this_det_tos']=this_det_tos[-1]
			this_det_dip=list(detail.objects.all().filter(st_id=request.session['code'], dip=True))
			context['this_det_dip']=this_det_dip[-1]
		except Exception as e:
			print(e)

	return TemplateResponse(request, 'student.html', context)









def view_list(request):
	if 'code' not in request.session:
		return enter(request)
	if len(request.session['code'])==6:
		return teacher(request)
	user=users.objects.get(code=request.session['code'])
	try:
		diploms=db_dip.objects.all().filter( diplom=True)
		
	except Exception as e:
		error=e

	try:
		tosols=db_dip.objects.all().filter(tosol=True)
	except Exception as e:
		error=e
	try:
		researchs=res.objects.all()
	except Exception as e:
		error=e


	context = {
		'user':user,
		'image':'dist/img/default.png', 
		'status':'Оюутан', 
		'diploms':diploms,
		'tosols':tosols,
		'researchs':researchs
	}

	if request.method == 'GET':  
		if request.GET:
			if request.GET['do']=='view':
				choose=db_dip.objects.get(d_id=request.GET['id'])			
				context['choose']=choose
				print(request.GET['id'] )
				return TemplateResponse(request, 'student.html', context)
			if request.GET['do']=='choose':
				if request.GET['choose']=='tos':
					choose=db_dip.objects.get(d_id=request.GET['code'])	
					try:
						del_det=detail.objects.all().filter(st_id=request.session['code'], tos=True)	
						del_list=list(del_det)	
						for i in del_list:
							false_dip=db_dip.objects.get(d_id=i.d_id.d_id)
							false_dip.songoson=False
							false_dip.save()			
						del_det.delete()	

					except Exception as e:
						print(e)
					choose.songoson=True
					choose.save()
					new_detail=detail.objects.create(d_id=choose, st_id=user, tos=True, tch_id=request.GET['tcode'])
					user.songoson=True
					user.save();
					return redirect('student')


				elif request.GET['choose']=='dip':
					choose=db_dip.objects.get(d_id=request.GET['code'])	
					try:
						del_det=detail.objects.all().filter(st_id=request.session['code'], dip=True)
						del_list=list(del_det)	
						for i in del_list:
							false_dip=db_dip.objects.get(d_id=i.d_id.d_id)
							false_dip.songoson=False
							false_dip.save()	
						del_det.delete()
					except Exception as e:
						print(e)
					choose.songoson=True
					choose.save()
					new_detail=detail.objects.create(d_id=choose, st_id=user, dip=True, tch_id=request.GET['tcode'] )
					user.songoson=True
					user.save();
					return redirect('student')
	return TemplateResponse(request, 'student.html', context)



def yvts_harah(request):
	

	if 'code' not in request.session:
		return enter(request)
	if len(request.session['code'])==10:	
		return student(request)
	user=users.objects.get(code=request.session['code'])
	
	try: 
		det_view=detail.objects.all().filter(tch_id=request.session['code'])
		all_det_view=detail.objects.all()
	except Exception as e:
		print(e)
	context = {
		'image':'dist/img/default.png', 
		'status':'Багш' , 
		'user':user,
		'yvts_harah':'True',
		'det_view':det_view,
		'all_det_view':all_det_view

	}


	return TemplateResponse(request, 'teacher.html', context)

class plan():	
	def create_plan(request):
		from .models import users, research as res, diplom as db_dip, detail, plan

		if 'code' not in request.session:
			return enter(request)
		if len(request.session['code'])==10:	
			return student(request)
		user=users.objects.get(code=request.session['code'])
		
		context = {
			'image':'dist/img/default.png', 
			'status':'Багш' , 
			'user':user, 
			'create_plan':'True',
			'plan':'True'
		}
		if request.method == 'POST':  
			p_topic = request.POST.get('topic', '') 
			p_note = request.POST.get('note', '') 
			p_s_date = request.POST.get('s_date', '') 
			p_s_time = request.POST.get('s_time', '') 
			p_f_date = request.POST.get('f_date', '') 
			p_f_time = request.POST.get('f_time', '')
			new_plan=plan.objects.create(topic=p_topic, note=p_note, start_date=p_s_date, start_time=p_s_time, finish_date=p_f_date, finish_time=p_f_time )
		try :
			view_plan=list(plan.objects.raw("select * from my_app_plan order by start_date, start_time"))
			j=0
			for i in range(1, len(view_plan)):
				if view_plan[j].start_date == view_plan[i].start_date:
					view_plan[i].start_date='xx'
				else:
					j=i
			context['view_plan']=view_plan
			if request.method == 'GET':
				del_plan=plan.objects.get(plan_id=request.GET['id'])
				del_plan.delete()
				return redirect('create_plan')
		except Exception as e:
			print(e)

		return TemplateResponse(request, 'teacher.html', context)



	def create_view(request):
		from .models import users, research as res, diplom as db_dip, detail, plan

		if 'code' not in request.session:
			return enter(request)
		if len(request.session['code'])==10:	
			return student(request)
		user=users.objects.get(code=request.session['code'])
		
		context = {
			'image':'dist/img/default.png', 
			'status':'Багш' , 
			'user':user, 
			'create_plan':'True',
			'plan_view':'True',

		}

		try :
			view_plan=list(plan.objects.raw("select * from my_app_plan order by start_date, start_time"))
			j=0
			for i in range(1, len(view_plan)):
				if view_plan[j].start_date == view_plan[i].start_date:
					view_plan[i].start_date='xx'
				else:
					j=i
			context['view_plan']=view_plan
			
		except Exception as e:
			print(e)

		return TemplateResponse(request, 'teacher.html', context)


	def view_plan(request):
		from .models import users, research as res, diplom as db_dip, detail, plan

		if len(request.session['code'])==6:
			return teacher(request)


		user=users.objects.get(code=request.session['code'])
		context = {
			'image':'dist/img/default.png',
			'user':user, 
			'status':'Оюутан',
			'plan_view':'True'
		}


		try :
			view_plan=list(plan.objects.raw("select * from my_app_plan order by start_date, start_time"))
			j=0
			for i in range(1, len(view_plan)):
				if view_plan[j].start_date == view_plan[i].start_date:
					view_plan[i].start_date='xx'
				else:
					j=i
			context['view_plan']=view_plan
			
		except Exception as e:
			print(e)

		return TemplateResponse(request, 'student.html', context)

