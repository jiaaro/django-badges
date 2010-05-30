from django.test import TestCase
from django.contrib.auth.models import User

from utils import MetaBadge, registered_badges
from utils import register as register_badge
from signals import badge_awarded
from models import Badge

class BadgeTests(TestCase):
    def setUp(self):
        registered_badges.clear()
        class YouveGotMail(MetaBadge):
            id = 'youve-got-mail'
            model = User
            one_time_only = True
            
            title = "You've got mail"
            description = "Filled in your E-mail address"
            level = "1"
            
            def get_user(self, instance):
                return instance
            
            def check_email(self, instance):
                return instance.email
            
        self.meta_badge = YouveGotMail
    
    def test_badge_creation(self):
        register_badge(self.meta_badge)
        badge = Badge.objects.get(id=self.meta_badge.id)
        self.assertTrue(isinstance(badge.meta_badge, self.meta_badge))
        
    def test_badge_registration_decorator(self):
        meta_badge = register_badge(self.meta_badge)
        self.assertTrue(meta_badge is self.meta_badge)
        
        meta_badge_instance = registered_badges[self.meta_badge.id]
        self.assertTrue(isinstance(meta_badge_instance, self.meta_badge))
        
    def test_badge_registration_only_happens_once(self):
        meta_badge = register_badge(self.meta_badge)
        meta_badge_instance = registered_badges[meta_badge.id]
        register_badge(self.meta_badge)
        
        self.assertTrue(registered_badges[meta_badge.id] is meta_badge_instance)
        
    def test_badge_earned_signal(self):
        register_badge(self.meta_badge)
        test_self = self
        
        signal_handler_kwargs = {}
        def signal_handler(**kwargs):
            signal_handler_kwargs.update(kwargs)
        badge_awarded.connect(signal_handler)
        
        user = User(username='tester', first_name='john', last_name='doe')
        user.save()
        
        # signal didn't fire because email was blank
        self.assertFalse(signal_handler_kwargs)
        
        user.email = 'woot@example.com'
        user.save()
        
        # make sure the signal fired and the kwargs were correct
        self.assertTrue( isinstance(signal_handler_kwargs.get('sender'), self.meta_badge) )
        self.assertEqual(signal_handler_kwargs.get('user'), user)
        self.assertEqual(signal_handler_kwargs.get('badge'), Badge.objects.all()[0])
        
        
        
        
                