from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
    # userlog = UserLog.objects.all()[0:10]
    # operator = dict(UserLog.OPERATE)
    # for log in userlog:
    #     log.operate_cn = operator[int(log.operate)]
    # kwgs = {
    #     "userlog":userlog
    # }

    # return render(request, "index.html", kwgs)
    return render(request, "index.html")