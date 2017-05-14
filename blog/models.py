from django.db import models

# Create your models here.


class Article(models.Model):
    subject = models.CharField(max_length=25)
    author = models.ForeignKey('User')
    pub_time = models.DateTimeField()
    content = models.TextField()

    article_type = models.ForeignKey('ArticleType')

    def __str__(self):
        return self.subject


class ArticleType(models.Model):
    type_name = models.CharField(max_length=25)
    who_created = models.ForeignKey('User')


class Comment(models.Model):
    who_comment = models.ForeignKey('User')
    comment_article = models.ForeignKey('Article')
    comment_time = models.DateTimeField()
    comment_content = models.TextField()

SEX = (
    ('1', '男'),
    ('2', '女'),
    ('3', '保密'),
)

class User(models.Model):
    account = models.CharField(unique=True, max_length=25)
    password = models.CharField(max_length=25)
    last_login_time = models.DateTimeField()

    nickname = models.CharField(max_length=25)
    email = models.EmailField()
    sex = models.CharField(max_length=1, choices=SEX)
    age = models.IntegerField()
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.nickname
