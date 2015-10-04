from django.conf.urls import patterns, url


urlpatterns = patterns('categorias.views',
      url(r'^$', 'home',name='home'),
      url(r'^lista/$', 'lista_categorias',name='lista_categorias'),
      url(r'^nova/$', 'nova_categoria',name='nova_categoria'),
      url(r'^editar/(?P<pk>\d+)$','editar_categoria', name='editar_categoria'),
)
