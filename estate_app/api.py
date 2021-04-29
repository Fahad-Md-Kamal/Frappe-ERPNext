import frappe
from .utils import sendmail

# sendmail(doc, recipients, msg, title, attachments=None)

# email agent from property page
@frappe.whitelist()
def contact_agent(**kwargs):
    doc = frappe.get_doc("Property", kwargs.get('property_code'))
    msg = f"From: {kwargs.get('your_name')} <br> {kwargs.get('your_email')} <br> {kwargs.get('message')}"
    attachments = [frappe.attach_print(doc, doc.doctype, file_name=doc.name)]
    sendmail(doc, [kwargs.get('agent_email')], msg=msg, title="Property Enquiry", attachments=attachments)

    return "Message Sent to Agent, You'll be responded as soon as possible. <br>Thank you."

#     Hey There,
# I'm interested for this property.
# Please let me know when you could meet me for more information and a little discussion.

# Thank You.