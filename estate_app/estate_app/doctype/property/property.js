// Copyright (c) 2021, Fahad Md Kamal and contributors
// For license information, please see license.txt

frappe.ui.form.on('Property', {
	setup: function(frm){
		console.log(frm);
		console.log(frm.selected_doc['name']);
		console.log(frm.selected_doc.amenities);
	},

	refresh: function(frm) {

		let btn = frm.add_custom_button('Extra Button', () => {
			frappe.prompt('Address', ({ value }) => {
				if (value){
					frm.set_value('address', value);
					frm.refresh_field('address');
					frappe.show_alert(`Address field updated with the value ${value}`, 5);
				}
			})
		});

		// Change Color of the Button
		btn[0].classList.replace('btn-default','btn-info');
	},
	
});
