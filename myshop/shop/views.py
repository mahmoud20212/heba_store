from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from cart.forms import CartAddProductForm
from .models import Category, Product
from .recommender import Recommender


def home(request):
    return render(request, 'shop/other/home.html')

def about_us(request):
    return render(request, 'shop/other/about_us.html')

def privacy(request):
    return render(request, 'shop/other/privacy.html')

def terms(request):
    return render(request, 'shop/other/terms.html')

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True).order_by('-created')

    query = request.GET.get('q')
    if query:
        products = products.filter(
            Q(translations__name__icontains=query) | 
            Q(translations__description__icontains=query)
        )
    
    if category_slug:
        language = request.LANGUAGE_CODE
        category = get_object_or_404(Category,
                                     translations__language_code=language,
                                     translations__slug=category_slug)
        products = products.filter(category=category)
    
    paginator = Paginator(products, 8)
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'query': query})


def product_detail(request, id, slug):
    language = request.LANGUAGE_CODE
    product = get_object_or_404(Product,
                                id=id,
                                translations__language_code=language,
                                translations__slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    # r = Recommender()
    # recommended_products = r.suggest_products_for([product], 4)
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form,
                   'recommended_products': None
                   })
