from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 

def index(request):
    path = request.path
    method = request.method
    response = HttpResponse()
    response.headers['Name'] = 'Krishna'
    content = '''
    <center>
        <p>Path : {}</p>
        <p>Method : {}</p>
        <p>Header : {}</p>
    </center>
    '''.format(path, method, response.headers)
    return HttpResponse(content, content_type = 'text/html', charset='utf-8')

def show(request, name, age):
    return HttpResponse("Name: {} <br> Age: {}".format(name, age))

def main(request):
    return HttpResponse('<h1 style="border: 5px solid;display: flex;justify-content: center;">Hello Krishna</h1>')

"""def menu(request):
    template = loader.get_template('../templates/index.html')
    context = {}
    return HttpResponse(template.render(context, request))"""

def queryview(request):
    name = request.GET['name']
    age = int(request.GET['age'])
    content = '''
    <center>
        <p>Name : {}</p>
        <p>Age : {}</p>
    </center>
    '''.format(name, age)
    return HttpResponse(content)