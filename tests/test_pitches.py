
import unittest
from app.models import Pitch
from app import db

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_pitch = Pitch(category='inspiration',pitch= 'you good')

    def tearDown(self):
        Pitch.query.delete ( )


    def test_check_instance_variables(self):
            self.assertEquals ( self.new_pitch.category , 'inspiration' )
            self.assertEquals ( self.new_pitch.pitch , 'you good' )
