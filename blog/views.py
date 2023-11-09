from django.shortcuts import render, redirect

from blog.forms import AuthorForm

from blog.models import Author

from rest_framework import viewsets

from .models import Author

from  .serializers import AuthorSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

def index_view(request):
    return render(request, 'index.html')

def blog_list_view(request):
    return render(request, 'blog_list.html')

def add_author_view(request):
    message = ''
    if request.method == "POST":
        author_form = AuthorForm(request.POST)

        if author_form.is_valid():
            author_form.save()
        message = "Author added Successfully"
    else:
        author_form = AuthorForm()

    authors = Author.objects.all()

    context = {
        'form': author_form,
        'msg': message,
        'authors':authors

    }

    return render(request, 'add_author.html', context)

def edit_author_view(request, author_id):
        author = Author.objects.get(id=author_id)
        message=''
        if request.method == "POST":
            author_form = AuthorForm(request.POST, instance=author)

            if author_form.is_valid():
                author_form.save()
                message = "Changes saved Successfully"
            else:
                message = "Form has Invalid data"
        else:
            author_form = AuthorForm(instance=author)

        context = {
            'form':author_form,
            'author':author,
            'message':message
        }

        return render(request, 'edit_author.html', context)

def delete_author_view(request, author_id):
    author = Author.objects.get(id=author_id)

    author.delete()

    return redirect( add_author_view)




        

