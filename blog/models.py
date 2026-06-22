from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)  # Qisqa matn uchun (max 200 ta harf)
    text = models.TextField()                 # Katta matn uchun
    created_at = models.DateTimeField(auto_now_add=True)  # Avtomatik vaqtni saqlaydi

    def __str__(self):
        return self.title