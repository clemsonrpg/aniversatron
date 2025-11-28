from django.http import HttpResponse

def index(request):
    return HttpResponse("Cadastro de Empréstimos")