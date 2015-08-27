from django.conf.urls import include, url

from django.contrib import admin

from django.contrib.staticfiles.urls import staticfiles_urlpatterns  


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'',include('blog.urls')),
    url(r'',include('vmaig_comments.urls')),
    url(r'',include('vmaig_auth.urls')),
]

urlpatterns += staticfiles_urlpatterns()  