from rest_framework.routers import SimpleRouter

from accounts import views

app_name = "accounts"

accounts_api_router = SimpleRouter(trailing_slash=True)

accounts_api_router.register(
    prefix='me',
    viewset=views.WhoAmI,
    basename='accounts-retrieve',
)

accounts_api_router.register(
    prefix='users',
    viewset=views.ListUsers,
    basename='accounts-list',
)

urlpatterns = accounts_api_router.urls
