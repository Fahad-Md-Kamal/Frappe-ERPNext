import frappe

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