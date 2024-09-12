from rest_framework.routers import DefaultRouter
from category.views import CategoryViewSet, SubCategoryViewSet



router = DefaultRouter()

router.register('sub-category', SubCategoryViewSet)
router.register('', CategoryViewSet)

urlpatterns = router.urls