# -*- coding: utf-8 -*-
# Copyright (c) 2021, Fahad Md Kamal and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Property(Document):
	
	def validate(self):
		if (self.property_type == "Flat"):
			pass

			# SQL
			# amenity = frappe.db.sql(f"""SELECT amenity FROM `tabProperty Amenity Detail` WHERE parent="{self.name}" AND parenttype="Property" AND amenity="Outdoor Kitchen";""", as_dict=True)
			# print(f"\n\n\n{amenity}\n\n\n")
			# if amenity:
			# 	frappe.throw(f"Property of type <b>Flat</b> Should not have amenity <b>{amenity[0]['amenity']}</b>")
