# Copyright (c) 2026, devika and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt


class Product(Document):
	def validate(self):
		self.validate_price()

	def validate_price(self):
		if flt(self.price) <= 0:
			frappe.throw(_("Price must be greater than zero"))

	def before_save(self):
		if not self.qr_code and self.product_code:
			self.qr_code = self.product_code
