from django.db import models


class BookInfo(models.Model):
    """数据信息模型类"""

    name = models.CharField(max_length=10)

    def __str__(self):

        return self.name


class People(models.Model):
    """人物信息模型类"""

    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    book = models.ForeignKey(BookInfo)

    def __str__(self):
        return self.name