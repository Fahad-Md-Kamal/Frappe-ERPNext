import frappe

def get_context(context):
    context.users = frappe.get_list("User")
    print(f"\n\n\n{context.users}\n\n\n")