import frappe
from estate_app.utils import sendmail

def validate(doc, event):
    pass
    # print(f"\n\n\n {doc}, {event} \n\n\n")
    # frappe.msgprint(
    #     title='Notification',
    #     msg=f"Hook's doc event <b>{event}</b> Executed",
    # )

def on_update(doc, event):
    print(f"\n\n\n {doc}, {event} \n\n\n")
    frappe.msgprint(f"{doc.name} has been updated by <b>{doc.owner}</b>")

# Dynamically Document Creation based on an event
def after_insert(doc, event):
    # create note on property insert
    note= frappe.get_doc({
        'doctype':'Note',
        'title':f"Property {doc.name} Added",
        'public': True,
        'content': doc.description
    })
    note.insert()
    frappe.db.commit()
    frappe.msgprint(f"{note.title} has been created.")
    # send mail
    agent_email = frappe.get_doc('Agent', doc.agent)
    msg = f"Hello <b>{doc.agent_name}</b>, a property has been created on your behalf."
    attachments = [frappe.attach_print(doc.doctype, doc.name, file_name=doc.name),]
    sendmail(doc, [agent_email, 'test@mail.com'], msg, 'New Property', attachments=attachments)