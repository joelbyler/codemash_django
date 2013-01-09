from django.conf.urls import patterns, include, url

# Use include to connect a regex to an app's urls.py # Use namespace to keep app URL names nicely isolated
urlpatterns = patterns('contact.views',
    url(r'^$', 'contact', name='contact_view'),
)
