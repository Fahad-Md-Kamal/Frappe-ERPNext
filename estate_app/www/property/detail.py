import frappe


def get_context(context):

    try:
        docname = frappe.form_dict.doctypename
        context.property = frappe.get_doc("Property", frappe.form_dict.doctypename)
        context.agent = frappe.get_doc("Agent", context.property.agent)
        context.related_properties = frappe.db.sql(f"""
            SELECT name, property_name, status, address, grand_total, 
            image FROM `tabProperty` WHERE property_type='{context.property.property_type}' 
            ORDER BY creation DESC LIMIT 3;
            """, as_dict=True)
    except Exception as e:
        frappe.local.flags.redirect_location = '/404'
        raise frappe.Redirect

    return context