from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),

    # 127.0.0.1:8000 으로 들어오는 모든 접속요청을 blog.url 로 전송해
    #추가 명령을 찾아낼것이다. r이 의미하는건 문자열에 특수문자가 있다는것을
    #알려주는것이다.
]

#유알엘 지정하는법
#http://www.mysite.com/post/12345
#^post/ : 유알엘이 오른쪽부터 포스트로 시작한다.
#(\d+) : 숫자가 한개이상 존재한다. 이숫자로 게시물을 찾을 수 있다.
#/ : /뒤에 문자가 들어간다.
# $ : 마지막이 /으로 끝난다.
#따라서  url(^post/(\d+)/$) = /post/12345/
