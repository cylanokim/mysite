from django.http import HttpResponse

def index(request):
    return HttpResponse("여기는 두 번째 페이지!!")

