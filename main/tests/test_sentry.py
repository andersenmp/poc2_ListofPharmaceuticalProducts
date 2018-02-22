from django.test import TestCase
from DjangoPython.core.Sentry import Sentry
from django.contrib.auth.models import User
from main.models import SentryModel


class TestSentry(TestCase):
    # def setUp(self):
    #     self.user = User.objects.create_user('temp', 'temp@gmail.com', 'temp')

    def test_no_features(self):
        user = User.objects.create_user('temp')
        sentry = Sentry(user)
        self.assertEqual(sentry.get_first_name(), user.username)
        self.assertEqual(sentry.get_last_name(), "Not in Sentry")
        self.assertEqual(sentry.get_email(), "email@not.registed.com")
        self.assertFalse(sentry.has_access_to_feature('/FEATURE'))
        self.assertEqual(sentry.get_total_rows(), 0)

    def test_has_feature(self):
        user = User.objects.create_user('temp')
        SentryModel.objects.create(login='temp',
                                   first_name='First',
                                   last_name='Last',
                                   email='temp@email.com',
                                   feature='/FEATURE',
                                   access_mode='I')
        sentry = Sentry(user)
        self.assertEqual(sentry.get_first_name(), "First")
        self.assertEqual(sentry.get_last_name(), "Last")
        self.assertEqual(sentry.get_email(), "temp@email.com")
        self.assertTrue(sentry.has_access_to_feature('/FEATURE'))
        self.assertEqual(sentry.get_total_rows(), 1)

    def test_has_more_features(self):
        user = User.objects.create_user('temp')
        SentryModel.objects.create(login='temp',
                                   first_name='First',
                                   last_name='Last',
                                   email='temp@email.com',
                                   feature='/FEATURE',
                                   access_mode='I')
        SentryModel.objects.create(login='temp',
                                   first_name='First',
                                   last_name='Last',
                                   email='temp@email.com',
                                   feature='/FEATURE',
                                   access_mode='I')
        SentryModel.objects.create(login='temp',
                                   first_name='First',
                                   last_name='Last',
                                   email='temp@email.com',
                                   feature='/FEATURES',
                                   access_mode='I')
        sentry = Sentry(user)
        self.assertEqual(sentry.get_first_name(), "First")
        self.assertEqual(sentry.get_last_name(), "Last")
        self.assertEqual(sentry.get_email(), "temp@email.com")
        self.assertTrue(sentry.has_access_to_feature('/FEATURE'))
        self.assertEqual(sentry.get_total_rows(), 3)

    def test_has_partial_feature(self):
        user = User.objects.create_user('temp')
        SentryModel.objects.create(login='temp',
                                   first_name='First',
                                   last_name='Last',
                                   email='temp@email.com',
                                   feature='/FEATURE/VIEW',
                                   access_mode='I')
        sentry = Sentry(user)
        self.assertEqual(sentry.get_first_name(), "First")
        self.assertEqual(sentry.get_last_name(), "Last")
        self.assertEqual(sentry.get_email(), "temp@email.com")
        self.assertTrue(sentry.has_access_to_feature('/FEATURE'))
        self.assertEqual(sentry.get_total_rows(), 1)

    def test_has_or_feature(self):
        user = User.objects.create_user('temp')
        SentryModel.objects.create(login='temp',
                                   first_name='First',
                                   last_name='Last',
                                   email='temp@email.com',
                                   feature='/FEATURE/VIEW',
                                   access_mode='I')
        sentry = Sentry(user)
        self.assertEqual(sentry.get_first_name(), "First")
        self.assertEqual(sentry.get_last_name(), "Last")
        self.assertEqual(sentry.get_email(), "temp@email.com")
        self.assertTrue(sentry.has_access_to_feature('/FEATURE/VIEW|/ADMINISTRATOR'))
        self.assertEqual(sentry.get_total_rows(), 1)
