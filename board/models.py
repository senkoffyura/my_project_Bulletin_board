from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField

class Author(models.Model):
    # rating = models.IntegerField(default=0)
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)

# class Category(models.Model):
#     category = models.CharField(max_length=64, unique=True)
#
#     def __str__(self):
#         return self.category.title()

class Post(models.Model):
    tank = "TN"
    healer = "HL"
    damagedealer = "DD"
    guildmaster = "GM"
    questguiwer = "QG"
    blacksmith = "BM"
    leatherworker = "LW"
    potionmaker = "PM"
    caster = "CS"

    CHOICE_CONTENS = [(tank,'Танк'),
                      (healer,'Лекарь'),
                      (damagedealer,'Воин'),
                      (guildmaster,'Глава гильдии'),
                      (questguiwer,'Квестгивер'),
                      (blacksmith, 'Кузнец'),
                      (leatherworker, 'Кожевник'),
                      (potionmaker,'Зельевар'),
                      (caster,'Заклинатель'),
                      ]

    time_creates = models.DateTimeField(auto_now_add=True)
    choice_content = models.CharField(max_length=2, choices=CHOICE_CONTENS, default= tank)
    heading = models.CharField(max_length=64)
    rating = models.IntegerField(default=0)
    content_field = MarkdownxField()
    autor = models.ForeignKey(Author, on_delete=models.CASCADE)
    # category = models.ManyToManyField(Category, through='PostCategory')

class Comment(models.Model):
    time_creates = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
# Create your models here.
