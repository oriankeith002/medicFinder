from django.http import HttpResponse 

def list_profile_view(request, id=None):
    return HttpResponse('<h1> User id %s </h1>'%id)

