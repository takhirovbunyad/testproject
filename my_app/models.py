from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    about = models.TextField()
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Books(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='books')
    def __str__(self):
        return f"{self.title} <------> {self.author.first_name} {self.author.last_name}"