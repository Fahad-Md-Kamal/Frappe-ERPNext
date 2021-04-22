// Copyright (c) 2016, Fahad Md Kamal and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Property"] = {
	"filters": [
		{
			"fieldname": "property",
			"lable": __("Property Name"),
			"fieldtype": "Data",
			"width":100,
			"reqd":0,
		},
		{
			"fieldname": "from",
			"lable": __("From Date"),
			"fieldtype": "Date",
			"width":80,
			"reqd":1,
			"default":dateutil.year_start()
		},
		{
			"fieldname": "to",
			"lable": __("To Date"),
			"fieldtype": "Date",
			"width":80,
			"reqd":1,
			"default":dateutil.year_end()
		},
		{
			"fieldname": "agent",
			"lable": __("Agent Name"),
			"fieldtype": "Link",
			"options":"Agent",
			"width":100,
			"reqd":0,
		},
		{
			"fieldname": "status",
			"lable": __("Status"),
			"fieldtype": "Select",
			"default":"",
			"options":["", "Sale", "Rent", "Lease"],
			"width":100,
			"reqd":0,
		},
	]
};
