from django.conf.urls import include, url, patterns
from django.contrib import admin
from store.views import store

urlpatterns = [
    # Examples:
    # url(r'^$', 'bookstore.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^store/', include('store.urls'), name='store'),

]
