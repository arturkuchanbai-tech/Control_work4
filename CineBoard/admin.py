from django.contrib import admin
from .models import Movie,Genre,Tag,Comment

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Tag)
admin.site.register(Comment)
