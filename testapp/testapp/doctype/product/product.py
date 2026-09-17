# Copyright (c) 2026, devika and contributors
# For license information, please see license.txt

from frappe.model.document import Document


class Product(Document):
	def before_save(self):
		if not self.qr_code and self.product_code:
			self.qr_code = self.product_code
