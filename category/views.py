from base.views import BaseModelViewSet
from category.models import Category, SubCategory
from category.permissions import IsAdminUserOrReadOnly
from category.app_settings import api_settings
# Create your views here.

class CategoryViewSet(BaseModelViewSet):
    queryset = Category.objects.all()
    serializer_class = api_settings.CATEGORY_SERIALIZER
    permission_classes = [IsAdminUserOrReadOnly]
    http_method_names = ['get', 'post', 'patch', 'delete']


class SubCategoryViewSet(BaseModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = api_settings.SUB_CATEGORY_SERIALIZER
    permission_classes = [IsAdminUserOrReadOnly]
    http_method_names = ['get', 'post', 'patch', 'delete']