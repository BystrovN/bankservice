from django.urls import path, include

urlpatterns = [
    path('organizations/', include('apps.api.organizations.urls')),
    path('webhook/', include('apps.api.webhooks.urls')),
]
