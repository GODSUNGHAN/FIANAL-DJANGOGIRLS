from django.contrib import admin
from .models import Post
#아까 모델스에서 제작한 클래스 포스트를 가져온다.


admin.site.register(Post)

