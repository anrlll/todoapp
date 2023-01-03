from django.db import models

# Create your models here.

#色の定義
CHOICE = (("danger","high"),("warning","normal"),("primary","low"))

class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length=50,
        choices=CHOICE
    )

    duedate = models.DateField()

    #データ名変更
    def __str__(self):
        return self.title



