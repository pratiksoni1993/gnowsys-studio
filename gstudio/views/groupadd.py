
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from gstudio.models import *
from gstudio.methods import *
import datetime
def groupadd(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a title.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
	stDate =  (request.POST["stDate"]).split("/")
        endDate=(request.POST["endDate"]).split("/")
        hours1 = int(request.POST["hours1"])
        minutes1 = int(request.POST["minutes1"])
        hours2 = int(request.POST["hours2"])
        minutes2 = int(request.POST["minutes2"])
        time1 = datetime.datetime(int(stDate[2]),int(stDate[0]),int(stDate[1]),hours1,minutes1)
        time2 = datetime.datetime(int(endDate[2]),int(endDate[0]),int(endDate[1]),hours2,minutes2)
	
        if not errors:
  	     title=request.POST['subject']
 	     content=request.POST['message']
	     idusr=request.POST['idusr']
             meetId = create_meeting(title,int(idusr),content)
	     schedule_time(time1, time2, meetId)
             if meetId :
                return HttpResponseRedirect('/nodetypes/group/gnowsys-grp/'+ str(meetId))
    variables = RequestContext(request,{'errors' : errors })
    template = "gstudio/NewGroup.html"
    return render_to_response(template, variables)
 
