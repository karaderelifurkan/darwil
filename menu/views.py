from django.shortcuts import render
from .models import Product


# Create your views here.



def home(request):
    query = request.GET.get("q")  # arama kelimesi (Audi vb)
    model_filter = request.GET.get("model")

    products = Product.objects.all()
    popular_products = Product.objects.filter(is_popular=True)

    if query:
        products = products.filter(
            title__icontains=query
        ) | products.filter(
            brand__icontains=query
        ) | products.filter(
            model__icontains=query
        )

    if model_filter:
        products = products.filter(model=model_filter)

    context = {
        "popular_products": popular_products,
        "products": products,
    }
    return render(request, "index.html", context)




def our(request):

    return render(request,"our.html")


def login(request):

    return render(request,"login.html")


def register(request):

    return render(request,"register.html")



def şifre(request):

    return render(request,"şifre.html")



def sayfa(request):

    return render(request,"page.html")

def servis(request):

    return render(request,"servis.html")


def pay(request):

    return render(request,"pay.html")





