from django.shortcuts import redirect, render
from .models import Book
from django.contrib import messages
from django.views.generic import ListView
from .forms import BookForm
from . import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def publisher(request):
	return render(request, 'publisher/home.html')

def uabook_form(request):
	return render(request, 'publisher/add_book.html')

class UBookListView(ListView):
	model = Book
	template_name = 'publisher/book_list.html'
	context_object_name = 'books'
	paginate_by = 5

	def get_queryset(self):
		return Book.objects.order_by('-id')


def uabook(request):
	if request.method == 'POST':
		title = request.POST['title']
		year = request.POST['year']
		image = request.FILES['image']
		pdf = request.FILES['pdf']
		
		a = Book(title=title, year=year, image=image, pdf=pdf)
		a.save()
		messages.success(request, 'Book was uploaded successfully')
		return redirect('publisher')
	else:
	    messages.error(request, 'Book was not uploaded successfully')
	    return redirect('uabook_form')	
		
