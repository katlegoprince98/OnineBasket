from django.shortcuts import render, redirect
from .models import TblBasket

# Create your views here.
def index(request):
    data = TblBasket.objects.all()
    context = {"data": data}
    return render(request, 'index.html', context)

def insertData(request):
    data = TblBasket.objects.all()
    context = {"data": data}
    if request.method == "POST":
        item = request.POST["item"]
        quantity = request.POST["quantity"]
        price = request.POST["price"]
        shopname = request.POST["shopname"]

        query = TblBasket(item=item, quantity=quantity, price=price, shopname=shopname)
        query.save()
        return redirect("/")

    return render(request, 'index.html', context)


def updateData(request, id):
    if request.method == "POST":
        item = request.POST["item"]
        quantity = request.POST["quantity"]
        price = request.POST["price"]
        shopname = request.POST["shopname"]

        edit = TblBasket.objects.get(id=id)
        edit.item = item
        edit.quantity = quantity
        edit.price= price
        edit.shopname = shopname
        edit.save()
        return redirect("/")


    data = TblBasket.objects.get(id=id)
    context = {"data": data}
    return render(request, 'edit.html', context)


def deleteData(request, id):
    data = TblBasket.objects.get(id=id)
    data.delete()
    return redirect("/")
