# Copyright (c) 2026, devika and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase
from frappe.utils import random_string


class TestProduct(FrappeTestCase):
	def setUp(self):
		self.created = []

	def tearDown(self):
		for name in self.created:
			frappe.delete_doc_if_exists("Product", name, force=1)
		self.created = []

	def _insert_product(self, **overrides):
		code = overrides.pop("product_code", None) or f"TEST-SKU-{random_string(8)}"
		values = {
			"doctype": "Product",
			"product_name": "Test Product",
			"product_code": code,
			"price": 10,
			"quantity": 1,
		}
		values.update(overrides)
		doc = frappe.get_doc(values).insert()
		self.created.append(doc.name)
		return doc

	def test_document_name_is_product_code(self):
		doc = self._insert_product()
		self.assertEqual(doc.name, doc.product_code)

	def test_qr_code_defaults_to_product_code(self):
		doc = self._insert_product(qr_code="")
		self.assertEqual(doc.qr_code, doc.product_code)

	def test_explicit_qr_code_is_preserved(self):
		custom_qr = f"CUSTOM-QR-{random_string(8)}"
		doc = self._insert_product(qr_code=custom_qr)
		self.assertEqual(doc.qr_code, custom_qr)
		self.assertNotEqual(doc.qr_code, doc.product_code)

	def test_negative_price_is_rejected(self):
		code = f"TEST-SKU-{random_string(8)}"
		doc = frappe.get_doc(
			{
				"doctype": "Product",
				"product_name": "Test Product",
				"product_code": code,
				"price": -1,
				"quantity": 1,
			}
		)
		self.assertRaises(frappe.NonNegativeError, doc.insert)

	def test_negative_quantity_is_rejected(self):
		code = f"TEST-SKU-{random_string(8)}"
		doc = frappe.get_doc(
			{
				"doctype": "Product",
				"product_name": "Test Product",
				"product_code": code,
				"price": 10,
				"quantity": -1,
			}
		)
		self.assertRaises(frappe.NonNegativeError, doc.insert)
