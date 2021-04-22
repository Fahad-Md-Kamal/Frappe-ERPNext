# Copyright (c) 2013, Fahad Md Kamal and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from frappe import _
import frappe

def execute(filters=None):
	return get_columns(), get_data(filters)


def get_data(filters):
	print(f"\n\n\n{filters}\n\n\n")
	
	_from, to = filters.get('from'), filters.get('to') # Date Range
	# Conditions
	conditions = " AND 1=1 "
	if(filters.get('property')):conditions += f" AND name LIKE '%{filters.get('property')}%' "
	if(filters.get('agent')):conditions += f" AND agent='{filters.get('agent')}' "
	if(filters.get('status')):conditions += f" AND status='{filters.get('status')}' "

	print(f"\n\n\n{conditions}\n\n\n")
	
	data = frappe.db.sql(f"""SELECT name, property_name, address, property_type,
		status, property_price, discount, grand_total, agent, agent_name FROM
		`tabProperty` WHERE (creation BETWEEN '{_from}' AND '{to}') {conditions};""")
	
	return data


def get_columns():
	return [
		"Property SKU:Link/Property:150",
		"Property Name:Data:150",
		"Address:Data:150",
		"Property Type:Data:100",
		"Property Status:Data:80",
		"Property Price:Currency:100",
		"Discount:Percent:20",
		"Grand Total:Currency:50",
		"Agent:Data:100",
		"Agent Name:Data:150",
	]