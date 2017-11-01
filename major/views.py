from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader, RequestContext
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views import generic
from .models import user
from .forms import UserForm

image_path_list=""
def index(request):	
	#image_path_list = user.objects.get(name='nuvaan')
	return render(request, 'major/enter.html')

def login(request):
    if request.method == 'POST':  # if the form has been filled
        form = UserForm(request.POST)
        if form.is_valid():  # All the data is valid  
        	try:
        		image_path_list = user.objects.get(name=request.POST.get('name', ''), password=request.POST.get('password', ''))
        		return HttpResponseRedirect(reverse('major:log', args=(request.POST.get('name', ''),)))
        	except Exception as e:
	        	return TemplateResponse(request, 'major/enter.html', {'message': 'Нэр эсвэл нууц үг буруу байна'})




def log(request, name):
    return render(request, 'major/base.html', {'name':name})


def video(request, name):
    return render(request, 'major/video.html', {'name':name})    


