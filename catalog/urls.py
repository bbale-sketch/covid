from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('speeches/', views.SpeechListView.as_view(), name='speeches'),
    path('speakers/', views.SpeakerListView.as_view(), name='speakers'),
    path('speech/<int:pk>', views.SpeechDetailView.as_view(), name='speech-detail'),
    path('speaker/<int:pk>', views.SpeakerDetailView.as_view(), name='speaker-detail'),

]


# # Use include() to add paths from the catalog application
# from django.urls import include

# urlpatterns += [
#     path('catalog/', include('catalog.urls')),
# ]

# #Add URL maps to redirect the base URL to our application
# from django.views.generic import RedirectView
# urlpatterns + [
#     path('', RedirectView.as_view(url='catalog/', permanent=True)),

# ]

# # Use static() to add url mapping to serve static files during development (only)
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)