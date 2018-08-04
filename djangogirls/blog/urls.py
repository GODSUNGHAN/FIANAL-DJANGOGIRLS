from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),

]
#포스트 리스트라는 뷰가 ^$ 에 할당이 되었다. 문자열이 아무것도 없는경우 매칭된다.
#이제 아이피 주소에 들어왓을떄 뷰 포스트 리스트를 보여주라고 할거야
#마지막 부분인 name = 'post_list'는 주소에 이름을 붙인걸로 뷰를 식별하낟.
#뷰의 이름이 같을수도 다를수도 있으니 일단은 넘어가고 외구기 쉽게 만들어야 한다.

#^은 "시작"을 뜻합니다.
#post/란 URL이 post 문자를 포함해야 한다는 것을 말함
#(?P<pk>\d+)정규표현식은 장고가 pk변수에 모든 값을 넣어 뷰로 전송하겠다는 뜻입니다.
# \d은 문자를 제외한 숫자 0부터 9 중, 한 가지 숫자만 올 수 있다는 것을 말합니다.
#  +는 하나 또는 그 이상의 숫자가 올 수 있습니다..
#  따라서 http://127.0.0.1:8000/post/라고 하면 post/
# 다음에 숫자가 없으므로 해당 사항이 아니지만,
# http://127.0.0.1:8000/post/1234567890/는 완벽하게 매칭됩니다.
#/은 다음에 / 가 한 번 더 와야 한다는 의미입니다.
#$는 "마지막"을 말합니다. 그 뒤로 더는 문자가 오면 안 됩니다.
