frappe.ui.form.on('Expense Claim', {
    refresh(frm){
        // your code here
        // console.log(frm)
    }
})


frappe.ui.form.on('Expense Claim Detail', {
    refresh(frm){
        console.log(frm);
    },
    expenses_add(frm, cdt, cdn){
        // console.log(row);
        let row = locals[cdt][cdn];
        if(frm.doc.posting_date){
            row.expense_date = frm.doc.posting_date;
            frm.refresh_field('expenses');
        }
    }
})