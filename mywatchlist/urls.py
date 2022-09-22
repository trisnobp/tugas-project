from django.urls import path
from mywatchlist.views import show_watchlist_html
from mywatchlist.views import show_watchlist_xml
from mywatchlist.views import show_watchlist_json

app_name = 'mywatchlist'

# Routing untuk menunjukkan data dalam bentuk html, xml, atau json
urlpatterns = [
    path('', show_watchlist_html, name='show_watchlist_html1'),
    path('html/', show_watchlist_html, name='show_watchlist_html'),
    path('xml/', show_watchlist_xml, name='show_watchlist_xml'),
    path('json/', show_watchlist_json, name='show_watchlist_json')
]