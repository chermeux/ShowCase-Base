# pylint: disable=E1101
"""
View Page about product app
CRUD organization and by Model
"""
############################ Import, Librairies etc ##############################
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from product.models import Product
from product.forms import ProductForm

################# Views with Product Model - Organized in the order of CRUD ####################
def c_product(request):
    """
    Create Product
    """
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ProductForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required - I don't know if it is necessary

            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect("/product/")

        # if a GET (or any other method) we'll create a blank form
    else:
        form = ProductForm()

    return render(request, "Product/CreateProduct.html", {"form":form})

def r_products(request):
    """
    Read Products
    """
    products = Product.objects.all()
    context = {'Products':products}

    return render(request, "Product/ProductsMain.html", context)

def u_product(request, id_product):
    """
    Update Product
    """
    product_to_update = Product.objects.get(id=id_product)
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ProductForm(request.POST, request.FILES, instance=product_to_update)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required - I don't know if it is necessary

            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect("/product/")

        # if a GET (or any other method) we'll create a blank form
    else:
        form = ProductForm(instance=product_to_update)

    return render(request, "Product/UpdateProduct.html", {"form":form})

def d_product(request, id_product):
    """
    Delete Product
    """
    product_to_delete = Product.objects.get(id=id_product)
    url_remove = 'Product_d'
    url_cancel = 'Products_r'
    context = {'Id': product_to_delete.id, 'UrlRemove':url_remove, 'UrlCancel':url_cancel}
    if request.method == "POST":
        product_to_delete.delete()
        return redirect('/product/')

    return render(request, "base/confirmDelete.html", context)
