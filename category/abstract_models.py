from django.utils.translation import gettext_lazy as _

from django.db import models

from base.models import BaseModel, i18nJSONField


# Create your models here.


class AbstractCategory(BaseModel):
    name = i18nJSONField(max_length=256)
    description = i18nJSONField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    cover_image = models.ImageField(null=True, blank=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        abstract = True    

    def __str__(self) -> str:
        return str(self.name)


class AbstractSubCategory(BaseModel):
    category = models.ForeignKey('category.category', on_delete=models.CASCADE)
    title = i18nJSONField(max_length=256)
    description = i18nJSONField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    cover_image = models.ImageField(null=True, blank=True)

    class Meta:
        abstract = True 

    def __str__(self) -> str:
        return str(self.title)