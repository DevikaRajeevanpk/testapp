# Copyright (c) 2026, devika and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestProduct(FrappeTestCase):
	def test_qr_code_defaults_to_product_code(self):
		doc = frappe.get_doc(
			{
				"doctype": "Product",
				"product_name": "Widget",
				"product_code": "WID-001",
				"price": 10,
			}
		).insert()
		self.assertEqual(doc.qr_code, "WID-001")
		doc.delete()

	def test_invalid_product_code_is_rejected(self):
		doc = frappe.get_doc(
			{
				"doctype": "Product",
				"product_name": "Bad Code",
				"product_code": "WID 001",
				"price": 10,
			}
		)
		self.assertRaises(frappe.ValidationError, doc.insert)

	def test_explicit_qr_code_is_preserved(self):
		doc = frappe.get_doc(
			{
				"doctype": "Product",
				"product_name": "Custom QR",
				"product_code": "WID-002",
				"price": 5,
				"qr_code": "custom-qr",
			}
		).insert()
		self.assertEqual(doc.qr_code, "custom-qr")
		doc.delete()
