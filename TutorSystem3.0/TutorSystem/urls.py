from django.conf.urls import patterns, include, url
from django.contrib import admin

from TutorSystem_app import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TutorSystem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'picture/(?P<path>.*)','django.views.static.serve',{'document_root':'./TutorSystem_app/TEMPLATE/'}),
    url(r'help_img/(?P<path>.*)','django.views.static.serve',{'document_root':'./TutorSystem_app/TEMPLATE/help'}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.TutorSystem_begin),
    url(r'^search/$',views.TutorSystem_search),
    url(r'help/$',views.TutorSystem_help),
    url(r'about/$',views.TutorSystem_about),
    url(r'^search/tut/$',views.TutorSystem_search_tut),
    url(r'^register/$',views.TutorSystem_reg),
    url(r'^login/$',views.TutorSystem_login),
    url(r'^logout/$',views.TutorSystem_logout),
    url(r'^person_center/$',views.person_center),
    url(r'^person_tut_page/$',views.person_tut_page),
    url(r'^person_center/tutor/$',views.person_center_tutor),
    url(r'^person_center/tutor/per_inf$',views.person_center_tutor_per),
    url(r'^person_center/tutor/rel_tutor_inf$',views.person_center_tutor_rel),
    url(r'^person_center/tutor/myprecontract$',views.person_center_tutor_myprecontract),
    url(r'^person_center/tutor/cha_passwd$',views.person_center_tutor_cha),
    url(r'^person_center/student$',views.person_center_student),
    url(r'^person_center/student/per_inf$',views.person_center_stu_per),
    url(r'^person_center/student/rel_stu_inf$',views.person_center_stu_rel),
    url(r'^person_center/student/math_tut$',views.person_center_stu_match),
    url(r'^person_center/student/judge$',views.person_center_stu_judge),
    url(r'^person_center/student/cha_passwd$',views.person_center_stu_cha),
    url(r'^person_center/student/precontract$',views.person_center_stu_myprecontract),
    url(r'^tutpage/([^/]+)/$',views.scan_tutpage),
)