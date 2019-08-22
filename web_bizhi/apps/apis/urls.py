from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^mobile_captcha/$', views.get_mobile_captcha, name="mobile_captcha"),
    url(r'^get_captcha/$', views.get_captcha, name='get_captcha'),
    url(r'^check_captcha/$', views.check_captcha, name='check_captcha'),
    # url(r'^questions/$', views.QuestionsView.as_view(), name='questions'),
    # url(r'^question/collection/(?P<id>\d+)/$', views.QuestionCollectionView.as_view(), name='question_collection'),
    url(r'^change_avator/$', views.ChangeAvator.as_view(), name='change_avator'),
]