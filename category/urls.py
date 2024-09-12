from rest_framework.routers import DefaultRouter
from category.views import CategoryViewSet, SubCategoryViewSet



router = DefaultRouter()

router.register('', CategoryViewSet)
router.register('sub-category', SubCategoryViewSet)

urlpatterns = router.urls