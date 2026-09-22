# Copyright (c) 2026, devika and Contributors
# See license.txt

from unittest import TestCase

from .product_utils import (
	default_qr_code,
	is_valid_product_code,
	normalize_product_code,
)


class TestProductCode(TestCase):
	def test_normalize_strips_whitespace(self):
		self.assertEqual(normalize_product_code("  WID-001  "), "WID-001")
		self.assertEqual(normalize_product_code(None), "")

	def test_valid_product_codes(self):
		for code in ("A", "WID-001", "sku.9", "Code_1"):
			self.assertTrue(is_valid_product_code(code), code)

	def test_invalid_product_codes(self):
		for code in ("", " WID", "WID 001", "-start", "bad/code", "has space"):
			self.assertFalse(is_valid_product_code(code), code)

	def test_qr_defaults_to_product_code(self):
		self.assertEqual(default_qr_code(None, "WID-001"), "WID-001")
		self.assertEqual(default_qr_code("  ", "WID-001"), "WID-001")

	def test_qr_keeps_explicit_value(self):
		self.assertEqual(default_qr_code("custom-qr", "WID-001"), "custom-qr")
