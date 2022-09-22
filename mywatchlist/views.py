from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_watchlist_html(request):
    total_watched = 0 # Total film yang sudah ditonton
    total_film = 0 # Total film
    for item in MyWatchList.objects.all():
        total_film += 1
        if item.watched == "Sudah":
            total_watched += 1

    total_unwatched = total_film - total_watched # Film yang belum ditonton

    data_barang_mywishlist = MyWatchList.objects.all()
    context = {
        'list_film': data_barang_mywishlist,
        'nama': "Trisno Bayu Pamungkas",
        'npm': "2106702200",
        'total_watched': total_watched,
        'total_unwatched': total_unwatched,
    }
    return render(request, "mywatchlist.html", context)

def show_watchlist_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_watchlist_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
