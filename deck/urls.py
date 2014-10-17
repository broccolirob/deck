from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from deck import settings

urlpatterns = patterns('',

    url(r'^$', 'cards.views.index', name='index'),
    url(r'^cards$', 'cards.views.cards', name='cards'),
    url(r'^clubs/$', 'cards.views.clubs', name='clubs'),
    url(r'^diamonds_hearts/$', 'cards.views.diamonds_hearts', name='diamonds_hearts'),
    url(r'^spade/$', 'cards.views.just_a_spade', name='spade'),
    url(r'^face/$', 'cards.views.face_only', name='face'),
    url(r'^filters/$', 'cards.views.filters', name='filters'),
    url(r'^first/$', 'cards.views.first', name='first'),
    url(r'^profile/$', 'cards.views.profile', name='profile'),
    url(r'^faq/$', 'cards.views.faq', name='faq'),
    url(r'^poker/$', 'cards.views.poker', name='poker'),
    url(r'^blackjack/$', 'cards.views.blackjack', name='blackjack'),
    url(r'^hearts/$', 'cards.views.hearts', name='hearts'),
    url(r'^num_cards/$', 'cards.views.num_cards', name='num_cards'),
    url(r'^war/$', 'cards.views.war', name='war'),
    url(r'^leaderboard/$', 'cards.views.leaderboard', name='leaderboard'),

    url(r'^register/$', 'cards.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
