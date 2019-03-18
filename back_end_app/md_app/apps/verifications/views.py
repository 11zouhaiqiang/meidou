# Create your views here.
from rest_framework.views import APIView
from md_app.libs.captcha.captcha import captcha
from django_redis import get_redis_connection
from apps.verifications import constants
from django.http import HttpResponse


class ImageCodeView(APIView):

    def get(self, request, image_code_id):
        """
        获取图片验证码
        :param request:
        :param image_code_id:
        :return:
        """
        text, image = captcha.generate_captcha()

        # 获取redis
        redis_conn = get_redis_connection('verify_code')

        redis_conn.setex(f'image_{image_code_id}', constants.IMAGE_CODE_REDIS_EXPIRES, text)

        return HttpResponse(image, content_type='images/jpg')
