from django.shortcuts import render, get_object_or_404, redirect
from car import Car
from forms import SaleForm, TradeINForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def car_list(request):
    query = request.GET.get("q", "")
    cars = Car.objects.filter(
        Q(make__icontains=query) | Q(model__icontains=query)
    )
    return render(request, "showroom/car_list.html", {"cars": cars, "query": query})


def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, "showroom/car_detail.html", {"car": car})


@login_required
def buy_car(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == "POST":
        form = SaleForm(request.POST, request.FILES)
        if form.is_valid():
            sale = form.save(commit=False)
            sale.client = request.user
            sale.car = car
            sale.save()
            return redirect("car_list")
    else:
        form = SaleForm(initial={'car': car})
    return render(request, "showroom/buy_car.html", {"form": form, "car": car})


@login_required
def tradein(request):
    if request.method == "POST":
        form = TradeINForm(request.POST)
        if form.is_valid():
            deal = form.save(commit=False)
            deal.client = request.user
            deal.save()
            return redirect("car_list")
    else:
        form = TradeINForm()
    return render(request, "showroom/tradein.html", {"form": form})
