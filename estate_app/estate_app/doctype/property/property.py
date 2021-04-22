# -*- coding: utf-8 -*-
# Copyright (c) 2021, Fahad Md Kamal and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Property(Document):

	def after_insert(self):
		print('\n\n\n ---------- \n\n\n')
		frappe.msgprint((f'Property <b>{self.name}</b> insertedd successfully'));


	def validate(self):
		try:
			frappe.db.sql("""SELECT name, tenant, friends FROM `tabProperty`;""")
		except Exception as e:
			error = frappe.log_error(frappe.get_traceback(), f"{e}")
			frappe.msgprint(f"An error occured see <a href='/app/error-log/{error.name}'> <b>{error.name}</b></a>");
			
			# print(e)
	# 	if (self.property_type == "Flat"):
	# 		for amenity in self.amenities:
	# 			if(amenity.amenity == "Outdoor Kitchen"):
	# 				frappe.throw(f"Property of type <b>Flat</b> should not have <b>{amenity.amenity}</b>")

			# SQL
			# amenity = frappe.db.sql(f"""SELECT amenity FROM `tabProperty Amenity Detail` WHERE parent="{self.name}" AND parenttype="Property" AND amenity="Outdoor Kitchen";""", as_dict=True)
			# print(f"\n\n\n{amenity}\n\n\n")
			# if amenity:
			# 	frappe.throw(f"Property of type <b>Flat</b> Should not have amenity <b>{amenity[0]['amenity']}</b>")

