from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photo')
    # on_delete: 연결된 모델이 삭제될 경우, CASCADE: 해당 하위객체도 같이 삭제
    # related_name: 연결된 객체에서 하위객체의 목록을 부를 때 사용할 이름
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='photos/no_image.png')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)  # auto_now_add: 객체가 추가될 때 자동생성
    updated = models.DateTimeField(auto_now=True)  # auto_now: 객체가 수정될때마다 자동설정

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.author.username + " " + self.created.strftime("%Y-%m-%d %H:%M:%S")

    def get_absolute_url(self): # 상세페이지의 주소를 반환하는 메서드, 객체를 생성수정했을 때 이동할 주소를 위해 호출sdfsfsdf
        # , 상세 화면으로 링크를 만들때 호출
        return reverse('photo:photo_detail', args=[str(self.id)])
