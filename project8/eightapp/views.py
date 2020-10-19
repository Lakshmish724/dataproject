from django.shortcuts import render

import datetime

# Create your views here.
def Welcome_clint(request):
	date=datetime.datetime.now()
	my_dict={'date':date}

	return render(request=request,template_name='eightapp/displaytime.html',context=my_dict)