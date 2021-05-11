# Copyright (c) 2021, Alesha Tech and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class AMLProducts(Document):

	def after_insert(self):
		"""This method will be executed after the product insertion to the database."""
		frappe.msgprint((f'Product <b>{self.name}</b> insertedd successfully'))


	def validate(self):
		"""This method validates product's validity."""
		try:
			frappe.db.sql("""SELECT title, price, old_price FROM `tabAML Products`;""")
		except Exception as e:
			error = frappe.log_error(frappe.get_traceback(), f"{e}")
			frappe.msgprint(f"An error occured see <a href='/app/error-log/{error.name}'> <b>{error.name}</b></a>")
			