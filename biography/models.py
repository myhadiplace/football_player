from django.db import models
from django.utils.text import slugify

# Create your models here.

class Clubs(models.Model):
    club_name = models.CharField(max_length=100)
    club_country = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.club_name}'


class Player(models.Model):
    full_name = models.CharField(max_length=100,editable=True)
    nick_name = models.CharField(max_length=100,null=True)
    born = models.DateField()
    birth_place= models.CharField(max_length=100)
    foot = models.CharField(max_length=10,choices=[("right","Right"),("left","Left")])
    current_club = models.ForeignKey(Clubs, on_delete=models.SET_NULL,null=True,default="")
    player_image = models.ImageField(upload_to="player image",default='')
    slug = models.SlugField(default="",db_index=True,blank=True)

    def __str__(self):
        return f'{self.full_name} born in {self.born}'


    def save(self,*args, **kwargs):
        self.slug = slugify(self.nick_name)
        super().save(*args, **kwargs)
