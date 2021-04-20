// Copyright (c) 2021, Fahad Md Kamal and contributors
// For license information, please see license.txt

frappe.ui.form.on('Property', {
	// setup: function(frm){
	// 	console.log(frm);
	// 	console.log(frm.selected_doc['name']);
	// 	console.log(frm.selected_doc.amenities);
	// },

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

		frm.add_custom_button('Check Property Types', () => {
			let property_type = frm.doc.property_type;

			// make ajax call
	 		frappe.call({
				 method: "estate_app.estate_app.doctype.property.api.check_property_types",
				 args: {'property_type': property_type},
				 callback: function(r) {
					// frappe.show_alert(`This property is of type: <b>${r.message[0]['property_type']}</b>`, 10);
					if (r.message.length>0){

						let header = `<h3>Below properties are of type ${property_type}</h3>`;
						let body = ``;
						r.message.forEach(d => {
							let cont = `<p>Name: ${d.name}: <a href="/app/property/${d.name}">Visit</a></p>`;
							body = body + cont;
						});
						let all = header + body;
						// show message
						frappe.msgprint(__(all));
					}
				 }
			 })


		})[0].classList.replace('btn-default','btn-warning');

	},
	
});
