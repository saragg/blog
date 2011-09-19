from django.template.loader import get_template
from django.template import Template, Context
from django.http import Http404, HttpResponse
from blog.blogapp.models import Book
from django.shortcuts import render_to_response
import datetime

def hello(request):
    return HttpResponse("Hello World!")

def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date' : now}))
    return HttpResponse(html)

def hours_ahead(request, offset):
     try:
          offset = int(offset)
     except ValueError:
          raise Http404()
     dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
     html = "<html><body>In %s hours(s), it will be %s.</body></html>" % (offset, dt)
     return HttpResponse(html)


def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</<table>' % '\n'.join(html))

def search(request):
    if 'q' in request.GET and request.GET['q']:
         q = request.GET['q']
	 books = Book.objects.filter(title__icontains=q)
	 return render_to_response('search_results.html',
	    {'books': books, 'query' : q})
    else:
        return render_to_response('search_form.html', {'error' : True})
