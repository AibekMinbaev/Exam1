from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model): 
    text = models.TextField() 
    date_published = models.DateField(auto_now_add = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self): 
        return self.text 


class Comment(models.Model): 
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()


    def __str__(self): 
        return self.comment_text 


class Like(models.Model): 
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


