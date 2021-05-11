import frappe

def get_context(context):
    context.products = frappe.db.sql("""SELECT * FROM `tabAML Products`;""", as_dict=True)
    return context