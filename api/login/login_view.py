from django.shortcuts import render

#create your views here:
def login_views(request):
    template_name ="login.htm"
    
    return render(request,template_name)