from odoo.tests.common import TransactionCase


class TestCreatoCore(TransactionCase):

    def test_module_loaded(self):
        """Basic test to ensure Creato Core module is installed and running"""
        self.assertTrue(True)
