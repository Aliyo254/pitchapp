import unittest
from app.models import User

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(username='ali2323',password = 'waroo')
    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)
    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('waroo'))

    def test_instance(self):
         self.assertEquals(self.new_user.username,'ali2323')
         self.assertEquals(self.new_user.email,'new@gmail.com')
