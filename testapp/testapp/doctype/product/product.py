# Copyright (c) 2026, devika and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import cint, flt

from .product_utils import (
	default_qr_code,
	is_valid_product_code,
	normalize_product_code,
)


class Product(Document):
	def validate(self):
		self.product_code = normalize_product_code(self.product_code)
		if self.product_name:
			self.product_name = self.product_name.strip()

		if not is_valid_product_code(self.product_code):
			frappe.throw(
				_(
					"Product Code must start with a letter or digit and may only contain letters, digits, dots, hyphens, and underscores."
				)
			)

		if flt(self.price) < 0:
			frappe.throw(_("Price cannot be negative"))

		if cint(self.quantity) < 0:
			frappe.throw(_("Quantity cannot be negative"))

		self.qr_code = default_qr_code(self.qr_code, self.product_code)
