from django.urls import path
from .views import ArtistList, WorkList, WorkFilteredList, ArtistSearchList
urlpatterns = [
    path('api/artists/', ArtistList.as_view(), name='artist-list'),
    path('api/works/', WorkList.as_view(), name='work-list'),
    path('api/works/<str:work_type>/', WorkFilteredList.as_view(), name='work-filtered-list'),
    path('api/works/search/<str:artist_name>/', ArtistSearchList.as_view(), name='artist-search-list'),
]
