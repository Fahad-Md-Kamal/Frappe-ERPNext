import frappe

def get_context(context):
    try:
        docname = frappe.form_dict.doctypename
        context.product = frappe.get_doc("AML Products", docname)
        context.product_vendor = frappe.get_doc("Vendor", context.product.vendor)
        print(f"\n\n\n{context.product_vendor}\n\n\n")

    except:
        print(f"Product Name Not Found")
    return context