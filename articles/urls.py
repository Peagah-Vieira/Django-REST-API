from rest_framework.routers import SimpleRouter

from articles import views

app_name = "articles"

articles_api_router = SimpleRouter(trailing_slash=True)

urlpatterns = articles_api_router.urls