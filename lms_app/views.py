from django.shortcuts import redirect ,render, get_object_or_404
from .models import *  #s15
from .forms import BookForm, CategoryForm   #s19
# Create your views here.

def index(request):
    if request.method == 'POST':   #s20
        add_book = BookForm(request.POST, request.FILES)   #s20
        if add_book.is_valid():   #s20
            add_book.save()   #s20
        
        add_category = CategoryForm(request.POST)   #s21
        if add_category.is_valid():   #s21
            add_category.save()   #s21



    context = {  #s15
        'Category' : Category.objects.all(),   #s16
        'books' : book.objects.all(),  #s15
        'form' : BookForm(),   #s20
        'formcat' : CategoryForm(),   #s21
        'allbooks' : book.objects.filter(active=True).count(),   #s25
        'booksold' : book.objects.filter(status = 'sold').count(),   #s25
        'bookrental' : book.objects.filter(status = 'rental').count(),   #s25
        'bookavailble' : book.objects.filter(status = 'availble').count(),   #s25
    }
    return render(request, 'pages/index.html', context)



def books(request):
    search = book.objects.all()    #29
    title= None     #29
    if 'search_name' in request.GET:     #29
        title = request.GET['search_name']     #29
        if title:     #29
            search = search.filter(title__icontains=title)    #29


    context = {     #s16
        'Category' : Category.objects.all(),   #s16
        'books' : search,   # s18 book.objects.all()   s29 search
                'formcat' : CategoryForm(),   #s30
    }
    return render(request, 'pages/books.html', context)



def update(request, id):   #s22
    book_id = book.objects.get(id=id)   #s22
    if request.method == 'POST':   #s22
        book_save = BookForm(request.POST, request.FILES, instance=book_id)   #s22
        if book_save.is_valid():   #s22
            book_save.save()   #s22
    else:   #s22
        book_save = BookForm(instance=book_id)   #s22
    context = {   #s22
        'form':book_save,   #s22
    }   #s22
    return render(request, 'pages/update.html', context)   #s22

def delete(request, id):   #s23
    book_delete = get_object_or_404(book, id=id)   #s23
    if request.method =='POST':   #s23
        book_delete.delete()   #s23
        return redirect('/')   #s23
    return render(request, 'pages/delete.html')   #s23