import frappe

# /api/method/estate_app.estate_app.doctype.property.api.check_property_types
@frappe.whitelist()
def check_property_types(property_type=None):
    return frappe.db.sql(f"""SELECT name, property_type FROM `tabProperty` WHERE property_type='{property_type}';""", as_dict=True)

