"""Root URL configuration."""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.main.urls")),
    path("", include("apps.vehicles.urls")),
    path("", include("apps.services.urls")),
    path("", include("apps.orders.urls")),
    path("", include("apps.inventory.urls")),
    path("", include("apps.billing.urls")),
    path("", include("apps.accounts.urls")),
]
