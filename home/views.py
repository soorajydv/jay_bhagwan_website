from django.shortcuts import render, HttpResponse, get_object_or_404
from home.models import Product,  Category
# Create your views here.
def index(request):
    products = Product.objects.all()[:10]  # Fetch all products
    context = {
        'products': products
    }
    return render(request, 'home.html', context)

def category_products(request, name):
    # Get the category object or return a 404 error if not found
    category = get_object_or_404(Category, name=name)
    
    # Fetch products belonging to the selected category
    products = category.products.all()  
    
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'home.html', context)


def search_products(request):
    query = request.GET.get('q', '')  # Get the query from the GET parameters
    if query:
        products = Product.objects.filter(name__icontains=query)  # Adjust this line based on your model fields
    else:
        products = Product.objects.none()  # No products if no query

    return render(request, 'home.html', {'products': products, 'search_query': query})


def about(request):
    return HttpResponse("jay shree Ram")