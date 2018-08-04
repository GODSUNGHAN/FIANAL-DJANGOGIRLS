from django.db import models
from django.utils import timezone
#장고의 기본 데이터 베이스에 존재하는 모델 데이터를 불러온다.
#장고 기본데이타.유틸 에 드들어가 있는 시간데이터를 불러온다.


class Post(models.Model): #포스트(이름)라는 모델을 정의한다. (객체이자 대상(고양이 같은 느낌))
    #항상 첫글자 Post는 대문자로 작성해준다.
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    #author 이라는 Post-author 이라는 속성을 알려준다. #models.ForeignKey 은 다른 모델에 대한 링크를 말해준다.
    title = models.CharField(max_length=200)
    #글자수가 제한된 텍스트를 정의할때 사용한다. 제목은 당연히 길이제한을 해줘야지
    text = models.TextField()
    #models.TextField 글자수가 제한되지 않은 텍스트를 저장할떄 사용
    created_date = models.DateTimeField(
        default=timezone.now)
    # 타임존은 뭐.. 당연히 알고.. 디폴트값을 아까 서울로 설정하였다.
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publishe(selfself):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
