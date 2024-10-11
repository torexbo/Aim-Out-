# test_payment.py
# Unit test for payment.py

import unittest
from src.payment import bkash_payment

class TestPayment(unittest.TestCase):
    
    def test_payment_success(self):
        result = bkash_payment(1000, "017XXXXXXXX")
        self.assertIsNotNone(result)
        self.assertEqual(result.get('status'), 'success')

if __name__ == "__main__":
    unittest.main()
