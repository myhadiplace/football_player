from django import forms
from .models import Clubs, Player

# clubs = Clubs.objects.all()
# all_clubs = [(club["clubs_name"],club["clubs_name"].upper()) for club in clubs]
# print(all_clubs)
# clubs = Clubs.objects.all()
# all_clubs = [(club.club_name,club.club_name.capitalize()) for club in clubs ]

class NewPlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields =["nick_name","born","foot",'current_club',"player_image"]
        labels = {
            "nick_name":"Player Name",
            "born": "Date of Birth",
            "foot":"Foot",
            'current_club':"Current Club",
            "player_image":"Player Image"
        }
        error_messages = {
            "nick_name":{
                "required":"player name must not be empty"
            },
            "born" : {
                "required":"Date of Birth must not be empty"
            },
            "player_image":{
                "required":"image must not be empty"
            }
        }

        # widgets = {
        #     'born': forms.DateTimeInput(attrs={'class': 'datepicker'}),
        # }



    # nick_name = forms.CharField(label="Player Name",max_length=100,error_messages={
    #     'required':' name must not be empty',
    #     "max_length":"please enter a short name"
    # })

    # born = forms.DateTimeField(label="born",error_messages={
    #     'required':'your name must not be empty',
    # })
    # birth_place = forms.CharField(label="birth place",error_messages={
    #     'required':'birth of place must not be empty',
    #     "max_length":"please enter a short name"
    # })
    # foot = forms.TypedChoiceField(label="foot", choices=[('right','Right'),('left',"Left")])
    # current_club = forms.TypedChoiceField(label="current club",choices=all_clubs)
    # image = forms.URLField(label="image url",max_length=200,error_messages={
    #     'required':'your name must not be empty',
    #     "max_length":"please enter a short name"
    # })



class NewClubForm(forms.ModelForm):
    class Meta:
        model = Clubs
        fields = "__all__"
        labels = {"club_name":"club name",
                 "club_country":"club country"}
        
        error_messages = {
            "club_name":{
                "required":"club name must not be empty"

            },
            "club_country":{
                "required":"club country must not be empty"
            }
        }
    # club_name = forms.CharField(label="club name",max_length=100,error_messages={
    #     'required':'club name must not be empty',
    #     "max_length":"please enter a short name"})

    # club_country = forms.CharField(label="club country",max_length=100,error_messages={
    #     'required':'club country must not be empty',
    #     "max_length":"please enter a short name"})
    