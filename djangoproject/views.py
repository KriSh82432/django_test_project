from django.http import HttpResponse

def handle404(request, exception):
    return HttpResponse("<center><h1 style='color: green;'>404 : Page not found </h1></center>")