# Copyright (c) 2026, devika and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestProduct(FrappeTestCase):
	def test_price_must_be_greater_than_zero(self):
		product = frappe.get_doc(
			{
				"doctype": "Product",
				"product_name": "Invalid Price Product",
				"product_code": "INV-PRICE-001",
				"price": 0,
			}
		)
		self.assertRaises(frappe.ValidationError, product.insert)

	def test_valid_product_is_saved(self):
		product = frappe.get_doc(
			{
				"doctype": "Product",
				"product_name": "Valid Product",
				"product_code": "VALID-001",
				"price": 100,
			}
		).insert()
		self.assertEqual(product.qr_code, "VALID-001")
		product.delete()
