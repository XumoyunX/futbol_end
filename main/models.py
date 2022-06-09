from django.db import models
from django.utils.translation import get_language

class TranslateHelperMixin:
    pass
    # def __getattr__(self, item):
    #     if item in self.translate_fields:
    #         lang = get_language()
    #         return getattr(self, '{}_{}'.format(item, lang))
    #
    #     return super(TranslateHelperMixin, self).__getattr__(item)



class Region(models.Model, TranslateHelperMixin):
    parent = models.ForeignKey('Region', on_delete=models.RESTRICT, null=True, default=None, blank=True)
    name_uz = models.CharField(max_length=250)
    name_ru = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_uz


class District(models.Model):
    region = models.ForeignKey(Region, null=True, on_delete=models.SET_NULL)
    name_uz = models.CharField(max_length=250)
    name_ru = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_uz


class Post(models.Model):
    region = models.ForeignKey(Region, null=True, on_delete=models.SET_NULL)
    district = models.ForeignKey(District, null=True, on_delete=models.SET_NULL)
    name_uz = models.CharField(max_length=250)
    name_ru = models.CharField(max_length=250)
    text_uz = models.TextField()
    text_ru = models.TextField()
    number = models.CharField(max_length=250)
    telegram = models.CharField(max_length=250)
    vaqt = models.CharField(max_length=250)
    price = models.PositiveIntegerField()
    img = models.ImageField(upload_to="images/")
    maydon_soni = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name_uz


