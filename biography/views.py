from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,HttpResponseRedirect,get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView,CreateView,DeleteView
from django.views.generic import ListView
from django.views import View
from .models import Player
from .forms import NewPlayerForm, NewClubForm
from .models import Clubs
# Create your views here.


class BioListView(ListView):
    template_name = 'biography/home.html'
    model = Player
    context_object_name = "player"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_url'] = self.request.path
        return context
    
    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query[:5]
      
        return data
  
    # template_name = 'biography/home.html'
    # def get_context_data(self,**kwargs):
    #     context = super().get_context_data(**kwargs)
    #     player = Player.objects.all()[:3]
    #     context['player'] = player
    #     return context
    
class ClubFinder(ListView):
    template_name = "biography/home.html"
    context_object_name = 'player'
    def get_queryset(self) :
        club_name = self.kwargs.get('club_name')
        club = get_object_or_404(Clubs,club_name= club_name)
        player = Player.objects.filter(current_club=club)
        return player

# clubfinder(View)
#     def get(self,request,club_name):
#         club = get_object_or_404(Clubs,club_name=club_name)
#         players = Player.objects.filter(current_club = club)
#         return render(request,"biography/home.html",{"player":players})



class AddClub(CreateView):
    model = Clubs
    form_class = NewClubForm
    template_name = "biography/add-club.html"
    success_url = '/bio/add'



# class AddClub(View):
#     def post(self,request):
#         form = NewClubForm(request.POST)
#         if form.is_vaild():
#             return HttpResponseRedirect('/bio/add-club')
#         else:
#             return render(request, "biography/add-form.html",{"form":form})
#     def get(self,request):
#         form = NewClubForm()
#         return render(request, "biography/add-form.html",{"form":form})
    
class AddPlayer(CreateView):
    model = Player
    form_class = NewPlayerForm
    template_name = "biography/add-form.html"
    success_url = '/bio/add'

    # def post(self,request):
    #     form = NewPlayer(request.POST)
    #     if form.is_valid():
    #         return HttpResponseRedirect('/bio/add')
    #     else:
    #         return render(request,"biography/add-form.html",{'form':form})


    # def get(self,request):
    #     form = NewPlayer()
    #     return render(request,"biography/add-form.html",{'form':form})

class DeletePlayerView(DeleteView):
    model = Player
    template_name = 'biography/confirm.html'
    success_url = "/bio/delete"



