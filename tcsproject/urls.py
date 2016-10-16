from django.conf.urls import url

from . import views

app_name = 'tcsproject'
urlpatterns = [
    url(r'^home/$', views.home, name="home"),
    url(r'^categories/(?P<id>[a-zA-Z ]+)/$', views.categories, name='categories'),
    url(r'^new/$', views.addnewthesis, name='addnewthesis'),
    # url(r'^thesis/(?P<id>[0-9]+)/$', views.viewthesis, name='viewthesis'),
    url(r'^thesis/(?P<id>[0-9]+)/delete/$', views.deletethesis, name='deletethesis'),
     url(r'^thesis/(?P<thesis>.+)/(?P<session_id>[0-9]+)/like/$', views.likethesis, name='like'),
    url(r'^send/$', views.sendemail, name='sendemail'),
    url(r'^home/search=(?P<thesis>.*)/', views.searchthesis, name='search'),
    url(r'^thesis/(?P<id>[0-9]+)/$', views.thesis_view, name='thesisview'),
    url(r'^thesis/all/$', views.viewall, name='viewall'),
    url(r'^thesis/all/published/$', views.viewallbypublished, name='viewallbypublished'),
    url(r'^thesis/all/authors/$', views.viewallbyauthor, name='viewallbyauthor'),
    url(r'^thesis/all/added/$', views.viewallbyadded, name='viewallbyadded'),
    #url(r'^categories/[a-zA-z]+/$', views.category, name='category'),
]