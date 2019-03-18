from rest_framework.views import exception_handler as drf_exception_handler
import logging
from django.db import DatabaseError
from redis.exceptions import RedisError
from rest_framework.response import Response
from rest_framework import status

logger = logging.getLogger('django')


def exception_handler(exc, context):
    """
    自定义异常处理

    :param exc: 异常
    :param context: 异常上下文
    :return: Response 响应对象
    """
    response = drf_exception_handler(exc, context)
    if response is None:

        view = context['view']

        if isinstance(exc, DatabaseError) or isinstance(exc, RedisError):
            logger.error(f'{view}{exc}')
            response = Response({'服务器内部错误'}, status.HTTP_501_NOT_IMPLEMENTED)
        return response
    return response
