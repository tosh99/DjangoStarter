from django.views.decorators.csrf import csrf_exempt
from Engine.apimanager.ApiManager import APIManager


@csrf_exempt
def resolveapi(request):
    return APIManager().resolve_context(request)
