from urllib.request import Request

from django.contrib.auth.models import User
from django.test import TestCase

from TechKiteLMSappstore.core.caching import TechKiteLMS_release_etag, \
    categories_etag, app_ratings_etag
from TechKiteLMSappstore.core.models import TechKiteLMSRelease, Category, \
    AppRating, App


class CachingTest(TestCase):

    def test_cache_TechKiteLMS_release_etag_empty(self):
        etag = TechKiteLMS_release_etag(Request('https://'))
        self.assertEquals('0-', etag)

    def test_cache_TechKiteLMS_release_etag(self):
        TechKiteLMSRelease.objects.create(version='12.0.2')
        TechKiteLMSRelease.objects.create(version='12.0.1')

        etag = TechKiteLMS_release_etag(Request('https://'))
        self.assertEquals('2-12.0.2', etag)

    def test_categories_etag(self):
        category = Category.objects.create(pk='test')
        etag = categories_etag(Request('https://'))
        self.assertEquals(str(category.last_modified), etag)

    def test_app_ratings_etag(self):
        user = User.objects.create(username='hi')
        app = App.objects.create(id='test', owner=user)
        rating = AppRating.objects.create(app=app, user=user)

        etag = app_ratings_etag(Request('https://'))
        self.assertEquals(str(rating.rated_at), etag)
