from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from . import views
from django_filters.views import FilterView
from .filters import *

urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^user/(\w+)/$', views.profile, name='profile'),
    url(r'post_treasure/', views.post_treasure, name='post_treasure'),
    url(r'^projetos/detalhes/(?P<slug>[-\w]+)/$', views.detail, name = 'detail'),
    url(r'^login/$', views.login_view, name='Login'),
    url(r'^logout/$', views.logout_view, name='Logout'),
    url(r'^like_treasure/$', views.like_treasure, name='like_treasure'),
    url(r'^register/$', views.register, name = 'register'),
    url(r'^estilos/(?P<slug>[-\w]+)/$', views.estilos_view, name = 'projetos_estilo'),
    url(r'^categorias/(?P<slug>[-\w]+)/$', views.categorias_view, name = 'projetos_categorias'),
    url(r'^projetos/$', FilterView.as_view(filterset_class=ProjetosFilter, template_name='projetos.html'), name = 'projetos'),
    #url(r'^projetos/$', views.projetos, name = 'projetos'),
    url(r'^procurar/$',views.search, name='procurar'),
    url(r'^pesquisa/$',views.pesquisa, name='pesquisa'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT,}),
    ]
