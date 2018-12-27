# Author:Sunday
from django.urls import path, include, re_path

from .views import UserinfoView, UploadImageView, UpdatePwdView, SendEmailCodeView, UpdateEmailView
from .views import MyCourseView, MyFavOrgView, MyFavTeacherView

app_name = 'users'

urlpatterns = [
    # 用户信息
    path("info/", UserinfoView.as_view(), name='user_info'),
    # 用户图像上传
    path("image/upload/", UploadImageView.as_view(), name='image_upload'),
    # 用户个人中心修改密码
    path("update/pwd/", UpdatePwdView.as_view(), name='update_pwd'),
    #发送邮箱验证码
    path("sendemail_code/", SendEmailCodeView.as_view(),name='sendemail_code'),
    #修改邮箱
    path("update_email/", UpdateEmailView.as_view(),name='update_email'),

    path("mycourse/", MyCourseView.as_view(),name='mycourse'),
    # 我的收藏--课程机构
    path('myfav/org/', MyFavOrgView.as_view(), name="myfav_org"),
    # 我的收藏--授课讲师
    path('myfav/teacher/', MyFavTeacherView.as_view(), name="myfav_teacher"),
]
