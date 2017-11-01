from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.enter, name='enter' ),
    url(r'^enter$', views.enter, name='enter' ),
    url(r'^logout$', views.logout, name='logout' ),
    url(r'^teacher$', views.teacher, name='teacher' ),
    url(r'^research$', views.research, name='research' ),
    url(r'^diplom$', views.diplom, name='diplom' ),
    url(r'^student$', views.student, name='student' ),
    url(r'^view_list$', views.view_list, name='view_list' ),
    url(r'^change$', views.change_teach, name='change_teach' ),
    url(r'^save_nariin$', views.save_nariin, name='save_nariin' ),
    url(r'^yvts_harah$', views.yvts_harah, name='yvts_harah' ),
    url(r'^create_plan$', views.plan.create_plan, name='create_plan' ),   
    url(r'^create_view$', views.plan.create_view, name='create_view' ),
    url(r'^view_plan$', views.plan.view_plan, name='view_plan' ),


]
