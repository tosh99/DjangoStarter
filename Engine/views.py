from Engine.utilities.utilities import response, generic_database_connect
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def home(request):
    pass