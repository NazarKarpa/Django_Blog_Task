from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    instead = models.TextField()
    data_create = models.DateField()

    def __str__(self):
        return self.name

class Comment(models.Model):


    text = models.CharField(max_length=1000)
    author = models.CharField(max_length=100)
    data = models.DateField()
    comment_to = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, blank=True)



    def __str__(self):
        return self.text
