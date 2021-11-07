from django.shortcuts import render
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse

from AddPage.models import Users, UserDetails
from AddPage.serializers import UsersSerializer, UserDetailsSerializer

from django.core.files.storage import default_storage


# Create your views here.
@csrf_exempt
def AddPageApi(request):
    html = "<html><body>Welcome To AddPage</body></html>" 
    return HttpResponse(html)