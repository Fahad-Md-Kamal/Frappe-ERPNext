import frappe

def validate(doc, event):
    print(f"\n\n\n {doc}, {event} \n\n\n")
    frappe.msgprint(
        title='Notification',
        msg=f"Hook's doc event <b>{event}</b> Executed",
    )