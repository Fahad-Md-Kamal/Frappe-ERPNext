import frappe

def sendmail(doc, recipients, msg, title, attachments=None):
    email_args = {
        'recipients': recipients,
        'message':msg,
        'subject': title,
        'reference_doctype': doc.doctype,
        'reference_name':doc.name,
    }
    if attachments:
        email_args['attachments']=attachments
    # Send mail
    frappe.enqueue(method=frappe.sendmail, queue='short', timeout=300, **email_args)


def paginate(doctype, page=0, conditions=None, paginate_by=6):
    # paginate_by = int(paginate_by)
    prev, next, search = 0, 0, False
    query = f"""SELECT 
        name, property_name, status, address, grand_total, image 
        FROM `tab{doctype}` {conditions} 
        ORDER BY creation DESC """
    
    if page:
        page = int(page)
        # This will multiply page number with for and deduct four from
        # as a result exact value could be found.
        properties = frappe.db.sql(query+f"""LIMIT {(page*paginate_by)-paginate_by}, {paginate_by};""", as_dict=True)
        
        # This will provide if there is next page available.
        next_set = frappe.db.sql(query+f"""LIMIT {page*paginate_by}, {paginate_by};""", as_dict=True)
        
        if next_set:
            # if there is no next page this code will set 
            # previous page number and next page number
            prev, next = page-1, page+1
        
        else:
            # If there is no next page it will set next page to zero(0)
            # while reducing 1 from the previous page.
            prev, next = page-1, 0

    else:
        # This will count total pagenatable size over data.
        count = frappe.db.sql(f"""SELECT COUNT(name) as count FROM `tab{doctype}` {conditions};""", as_dict=True)[0].count

        # if the data is more than 4 than the previous page will
        # be set to 0(zero) and next page will be set to 2
        if count > paginate_by:
            prev, next =0, 2
        else:
            pass
        
        # This will execute the query with initail LIMIT size of four.
        properties = frappe.db.sql(query+f"""LIMIT {paginate_by};""", as_dict=True)
    
    if conditions: 
        search=True

    return{
        'properties':properties,
        'prev': prev,
        'next': next,
        'search': search,
    }