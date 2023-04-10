import unittest
from io import StringIO
from unittest.mock import patch 

class Authorizer_SMS_TestCase(unittest.TestCase):
    
    def test_init_authorized(self):
        auth = Authorizer_SMS()
        self.assertFalse(auth.is_authorized())
        
    def test_code_decimal(self):
        auth = Authorizer_SMS()
        auth.generate_sms_code()
        self.assertTrue(auth.code.isdecimal())
        
    def test_authorize_success(self):
        auth = Authorizer_SMS
        