import frappe
from estate_app.utils import paginate

def get_context(context):
    page = frappe.form_dict.page
    conditions = None
    type, status, city = frappe.form_dict.type, frappe.form_dict.status, frappe.form_dict.city
    
    if type and status and city:
        conditions = f"""
            WHERE property_type='{type}' 
            AND city='{city}' 
            AND status='{status}' """
        
        context.type = type
        context.status = status
        context.city = city

    paginate_by = frappe.form_dict.paginate_by
    paginate_by = int(paginate_by) if paginate_by else 6
    
    pagination = paginate(doctype='Property', page=page, conditions=conditions, paginate_by=paginate_by)#paginate_by=paginate_by)
    
    context.types = frappe.db.sql("""SELECT name FROM `tabProperty Type`;""", as_dict=True)
    context.cities = frappe.db.sql("""SELECT name FROM `tabCity`;""", as_dict=True)
    context.properties = pagination.get('properties')
    context.search = pagination.get('search')
    context.prev = pagination.get('prev')
    context.next = pagination.get('next')
    context.paginate_by = pagination.get('paginate_by')

    return context