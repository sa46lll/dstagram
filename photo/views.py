from django.shortcuts import render, redirect
from django.views import generic

from photo.models import Photo


def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo/list.html', {'photos': photos})  # photos 라는 템플릿 변수를 같이 전달


class PhotoUploadView(generic.CreateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/upload.html'  # 실제 사용할 템플릿 설정


def form_valid(self, form):  # 업로드를 끝낸 후 이동할 페이지 호출
    form.instance_id = self.request.user.id  # 작성자는 현재 로그인 한 사용자로 설정
    if form.is_valid():  # 입력된 값들 검증
        form.instance.save()  # 데이터베이스 저장
        return redirect('/')  # 메인페이지 이동
    else:
        return self.render_to_response({'form': form})  # 이상이 있다면 작성된 내용 그대로 작성 페이지에 표시


class PhotoDeleteView(generic.DeleteView):
    model = Photo
    success_url = '/'
    template_name = 'photo/delete.html'


class PhotoUpdateView(generic.UpdateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/update.html'

