from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Alesha Product")
			"icon": "octicon octicon-book",
            "items": [
                {
                    "type":"doctype",
                    "name":"Mart Product",
                    "label":_("Mart Product"),
                    "description":_("Mart Product"),
                    "onboard":1,
                }
            ]
		}
	]
