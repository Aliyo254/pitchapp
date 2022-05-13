import unittest
from app.models import Comment
from app import db

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_comment = Comment(comment='good')

    def tearDown(self):

        Comment.query.delete ( )

    def test_check_instance_variables(self):
            self.assertEquals ( self.new_comment.comment , 'good' )