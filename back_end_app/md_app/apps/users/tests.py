from django.test import TestCase


# Create your tests here.


class test_redis(TestCase):

    def tearDown(self):
        from django_redis import get_redis_connection
        get_redis_connection('default').flushall()

    def test_1(self):
        assert 1 == 2
