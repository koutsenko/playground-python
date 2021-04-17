from datetime import datetime
from django.shortcuts import render, redirect

from web.models import Publication


def hello(request):
    return render(request, 'main.html')


def contacts(request):
    return render(request, 'contacts.html')


def publication(request, pub_id):
    try:
        publication = Publication.objects.get(id=pub_id)
    except Publication.DoesNotExist:
        return redirect('/')
    return render(request, 'publication.html', {
        'publication': publication
    })


def publications(request):
    pubs_sorted = Publication.objects.order_by('-date')

    return render(request, 'publications.html', {
        'publications': pubs_sorted
    })


def post(request):
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        if title and text:
            Publication.objects.create(title=title, text=text)
            return redirect('/publications/')
        else:
            return render(request, 'post.html', {
                'error': 'Both title and text must not be empty'
            })

    return render(request, 'post.html')
