from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('addNotesGrainger', views.addNotesGrainger, name='addNotesGrainger'),
    path('addNotesGies', views.addNotesGies, name='addNotesGies'),
    path('addNotesLas', views.addNotesLas, name='addNotesLas'),
    path('<id>/<str:branch>/edit', views.edit, name='edit'),
    path('grainger', views.grainger, name='grainger'),
    path('gies', views.gies, name='gies'),
    path('las', views.las, name='las'),
    path('contact', views.contact, name='contact')
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)