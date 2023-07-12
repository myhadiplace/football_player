
from . import views
from django.urls import path

urlpatterns = [
    path("delete",views.BioListView.as_view(),name='delete_page_url'),
    path('',views.BioListView.as_view(),name='bio_page_url'),
    path("add",views.AddPlayer.as_view(),name = "add_url"),
    path("add-club",views.AddClub.as_view(),name = "add_club_url"),
    path("<str:club_name>",views.ClubFinder.as_view(), name="club_finder_url"),
    path('delete/<int:pk>',views.DeletePlayerView.as_view(),name='delete_url'),
   

] 