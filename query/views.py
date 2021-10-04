from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import simplejson as json
from django.db import models
from django.db.models import *
from django.db.models.functions import *
from django.core.exceptions import *

from django.forms.models import model_to_dict # is used to convert the single record into dic
# Create your views here.
def Home(request):
	emp = Emp.objects.all().count()
	dep = Deptno.objects.all().count()
	
	
	d=[{'Table':'Deptno' ,'count':dep,'q':'Deptno.objects.all()'},{'Table':'Emp' ,'count':emp,'q':'Emp.objects.all()'}]
	return  render(request,'index.html',{'d':d})

def Ajax(request):
	try:
		name = request.GET['name']
		l=[]
		if 'values'  in name:
			for i in eval(name):
				for j in i:
				   i[j]=str(i[j])
				l.append(i)
				
			return HttpResponse(json.dumps(l))
		elif '.annotate' or '.select_related' in name:
			for i in eval(name).values():
				for j in i:
				   i[j]=str(i[j])
				l.append(i)
			
			return HttpResponse(json.dumps(l))
		elif '.aggregate(' in name:
			l=eval(name)
			for i in l:
				l[i]=str(l[i])
			l=[l]
			return HttpResponse(json.dumps(l))
		elif '.count()' in name:
			d ={'count':str(eval(name))}
			l=[d]
			return HttpResponse(json.dumps(l))
		elif '.update(' in name:
			a=eval(name)
			a.save()
			return HttpResponse('<h1>Updated</h1>')
		else:
			for i in eval(name):
				s=model_to_dict(i)
				for j in s:
				   s[j]=str(s[j])
				l.append(s)
			print(l)
			return HttpResponse(json.dumps(l))
	except Exception as ex:
		return HttpResponse(str(ex)+str(name))
		
			