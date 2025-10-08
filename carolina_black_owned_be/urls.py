from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

from core.views import get_homepage_data
from listings import views as listing_views

urlpatterns = [
    path("admin/", admin.site.urls),

    # app routers live inside each app (e.g., auth_app/urls.py)
    path("api/auth/", include("auth_app.urls")),
    path("api/", include("core.urls")),

    # auth token endpoint
    path("api/token/", obtain_auth_token, name="obtain-token"),

    # listings function views
    path("api/listings/", listing_views.list_listings, name="list-listings"),
    path("api/listings/add/", listing_views.add_listing, name="add-listing"),
    path("api/listings/update/<int:listing_id>/", listing_views.update_listing, name="update-listing"),
    path("api/listings/delete/<int:listing_id>/", listing_views.delete_listing, name="delete-listing"),

    # homepage
    path("api/homepage/", get_homepage_data, name="homepage"),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

