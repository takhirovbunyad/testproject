from django.shortcuts import render, redirect
from .models import Author, Books
from django.shortcuts import get_object_or_404

def Getname(request):
    if request.POST:
        model = Author()
        model.first_name =  request.POST.get('first_name')
        model.last_name = request.POST.get('last_name')
        model.about = request.POST.get('about')
        model.save()
        return redirect('get_author', author_id=model.id)
    return render(request, 'main.html')

def getauthor(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    return render(request, 'suc.html', {'author': author})

def get_users(request):
    authors = Author.objects.prefetch_related('books')
    return render(request, 'userlist.html', {'authors': authors})