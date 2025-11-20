from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from .forms import EmailPostForm, CommentForm , BookForm
from .models import Book , Comment
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from . import services
def login_required_decorator(func):
    return login_required(func, login_url='my_app:login_page')

@login_required_decorator
def logout_view(request):
    logout(request)
    return redirect('my_app:logout_page')

def login_view(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('my_app:homepage')
    return render(request, 'book/login.html')

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("my_app:login_page")
    template_name = "book/signup.html"


class BookListView(ListView):
    model = Book
    template_name = 'book/main.html'
    context_object_name = 'books'
    paginate_by = 6

@login_required_decorator
def book_detail(request, year, month, day , slug):
    book = get_object_or_404(Book, slug=slug ,
                             status = 'published' ,
                             publish__year=year ,
                             publish__month=month ,
                             publish__day=day )
    new_comment = None
    comments = book.comments.filter(active=True)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = book
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'book/detail.html', {
        'book': book,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    })



@login_required_decorator
def book_share(request, book_id):
    book = get_object_or_404(Book, id=book_id, status='published')
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            book_url = request.build_absolute_uri(book.get_absolute_url())
            subject = f"{cd['name']} recommends you read '{book.title}'"
            message = f"Read '{book.title}' at {book_url}\n\n"
            message += f"{cd['name']}'s comments: {cd['comments']}"
            book.email_book(subject, message, cd['to'])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'book/share.html', {
        'book': book,
        'form': form,
        'sent': sent
    })


@login_required_decorator
def stats_page(request):
    books_len = services.get_books()
    users_len = services.get_users()
    context = {
        'books_len': len(books_len),
        'users_len': len(users_len),
    }
    return render(request, 'stats/stats.html', context)

@login_required_decorator
def crudpageadd(request):
    model = Book()
    form = BookForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('my_app:book_list_page')
    context = {
        'form': form,
    }
    return render(request, 'crudbookpage/add.html', context)

@login_required_decorator
def crudpageedit(request, book_id):
    model = get_object_or_404(Book, pk=book_id)
    form = BookForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('my_app:book_list_page')
    context = {
        'form': form,
    }
    return render(request, 'crudbookpage/add.html', context)

def book_list_page(request):
    books = services.get_books()
    context = {
        'books': books,
    }
    return render(request, 'crudbookpage/book_list.html', context)