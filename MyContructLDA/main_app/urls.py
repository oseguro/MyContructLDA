from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from . import views

urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^user/(\w+)/$', views.profile, name='profile'),
    url(r'post_treasure/', views.post_treasure, name='post_treasure'),
    url(r'^detalhes/(?P<slug>[-\w]+)/$', views.detail, name = 'detail'),
    url(r'^login/$', views.login_view, name='Login'),
    url(r'^logout/$', views.logout_view, name='Logout'),
    url(r'^like_treasure/$', views.like_treasure, name='like_treasure'),
    url(r'^register/$', views.register, name = 'register'),
    url(r'^estilos/(?P<slug>[-\w]+)/$', views.estilos_view, name = 'projetos_estilo'),
    url(r'^categorias/(?P<slug>[-\w]+)/$', views.categorias_view, name = 'projetos_categorias'),
    url(r'^projetos/$', views.projetos, name = 'projetos'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT,}),
    ]
