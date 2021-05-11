import frappe

def get_context(contxt):
    contxt.products = frappe.get_list("AML Products", fields=["title", "price"])
    # contxt.users = frappe.get_list("User", fields=["first_name", "last_name"])