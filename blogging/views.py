from django.shortcuts import render
from django.template import loader
from blogging.models import Post

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect, Http404

def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")

## and this view
#def list_view(request):
#    published = Post.objects.exclude(published_date__exact=None)
#    posts = published.order_by('-published_date')
#    template = loader.get_template('blogging/list.html')
#    context = {'posts': posts}
#    body = template.render(context)
#    return HttpResponse(body, content_type="text/html")


# rewrite our view
def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')
    context = {'posts': posts}
    return render(request, 'blogging/list.html', context)

