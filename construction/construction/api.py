from rest_framework import routers
from card.views import CardViewset
from material.views import CategoryViewset, SubCategoryViewset, ProductViewset

router = routers.SimpleRouter()


router.register('card', CardViewset)
router.register('category', CategoryViewset)
router.register('subcategory', SubCategoryViewset)
router.register('product', ProductViewset)



urlpatterns = []
urlpatterns += router.urls