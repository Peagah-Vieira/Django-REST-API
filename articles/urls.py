from rest_framework.routers import SimpleRouter

from articles import views

app_name = "articles"

articles_api_router = SimpleRouter(trailing_slash=True)

articles_api_router.register(
    prefix="api",
    viewset=views.ArticlesAPIViewSet,
    basename="articles-api",
)

articles_api_router.register(
    prefix="categories/api",
    viewset=views.CategoriesAPIViewSet,
    basename="articles-category-api",
)

urlpatterns = articles_api_router.urls