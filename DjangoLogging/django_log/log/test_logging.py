from django.test import TestCase
import logging 


class Logging(TestCase):
    def test_logging(self):
        logger = logging.getLogger(__name__)
        logger.info('Test logging message')
        self.assertEqual(1,1)