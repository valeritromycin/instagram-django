from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from tags_app.api.router import api_router as tag_router
from publication_app.api.router import api_router as publication_router
from registration_app.api.router import api_router as registration_router
from media_app.api.router import api_router as media_router
from likes_app.api.router import api_router as likes_router
from comments_app.api.router import api_router as comments_router
from subscription_app.api.router import api_router as subscriptions_router

from publication_app.views import main_page, PostListView
from registration_app.views import registration_page, authorisation_page, logout_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostListView.as_view(), name='main_page'),
    path('sign-up/', registration_page, name='sign-up'),
    path('sign-in/', authorisation_page, name='sign-in'),
    path('logout/', logout_page, name='logout'),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(),
        name="swagger-ui",
    ),
    path('api/', include(tag_router.urls)),
    path('api/', include(publication_router.urls)),
    path('api/', include(registration_router.urls)),
    path('api/', include(media_router.urls)),
    path('api/', include(likes_router.urls)),
    path('api/', include(comments_router.urls)),
    path('api/', include(subscriptions_router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
