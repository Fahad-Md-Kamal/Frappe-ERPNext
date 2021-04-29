import frappe
from estate_app.utils import paginate

def get_context(context):
    # print(f"\n\n\n{frappe.form_dict}\n\n{frappe.form_dict.hello}\n")
    # context.properties = frappe.db.sql("""SELECT name, property_name, 
    #     status, address, grand_total, 
    #     image FROM `tabProperty` ORDER BY creation DESC;""", 
    #     as_dict=True)

    page = frappe.form_dict.page
    paginate_by = frappe.form_dict.paginate_by
    paginate_by = int(paginate_by) if paginate_by else 6
    pagination = paginate('Property', page, paginate_by)#paginate_by=paginate_by)
    context.properties = pagination.get('properties')
    context.prev = pagination.get('prev')
    context.next = pagination.get('next')
    context.paginate_by = pagination.get('paginate_by')
    return context