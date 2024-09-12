from django.conf import settings
from django.utils.translation import gettext_lazy as _
from rest_framework.settings import APISettings as _APISettings


USER_SETTINGS = getattr(settings, "CATEGORY", None)


DEFAULTS = {
    'CATEGORY_SERIALIZER': 'category.serializers.CategorySerializer',
    'SUB_CATEGORY_SERIALIZER': 'category.serializers.SubCategorySerializer',
}

# List of settings that may be in string import notation.
IMPORT_STRINGS = (
    'CATEGORY_SERIALIZER',
    'SUB_CATEGORY_SERIALIZER',
)


api_settings = _APISettings(USER_SETTINGS, DEFAULTS, IMPORT_STRINGS)