from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField("Жанр", max_length=50)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField("Тег", max_length=50)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, verbose_name="Жанр")
    release_date = models.DateField("Дата выхода")
    rating = models.FloatField("Рейтинг")
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="Теги")

    def __str__(self):
        return self.title

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField("Комментарий")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} - {self.movie.title}"