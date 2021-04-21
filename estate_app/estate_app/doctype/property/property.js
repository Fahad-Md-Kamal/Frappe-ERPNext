// Copyright (c) 2021, Fahad Md Kamal and contributors
// For license information, please see license.txt

frappe.ui.form.on('Property', {
	setup: function(frm){
		frm.check_amenities_duplicate = function(frm, row){
			frm.doc.amenities.forEach (item => {
				if(row.amenity == '' || row.idx == item.idx){

				}
				else {
					if(row.amenity == item.amenity) {
						row.amenity = '';
						frappe.throw(__(`${item.amenity} already exists row ${item.idx}`));
						frm.refresh_field('amenities');
					}
				}
			})
		}

		frm.check_flat_against_outdoor_kitchen = function(frm, row){
			if(row.amenity == "Outdoor Kitchen" && frm.doc.property_type=="Flat"){
				let amenity = row.amenity
				row.amenity = '';
				frappe.throw(__(`${amenity} cannot exist in a flat`));
				frm.refresh_field('amenities');
			}
		}

		// Compute property price
		frm.compute_total = function(frm){
			let total = 0;
			// loop through the child table
			frm.doc.amenities.forEach(d => {
				total = total + d.amenity_price
			})
			// new_total
			let new_total = frm.doc.property_price + total;
			if (frm.doc.discount){
				new_total = new_total - (new_total * (frm.doc.discount/100))
			}
			console.log(new_total)
			// set grand_total value
			frm.set_value('grand_total', new_total)
		},

		// Copy discount to amenities
		frm.copy_discount = function(frm){
			frm.doc.amenities.forEach(d=> {
				d.discount = frm.doc.discount;
			});
			frm.refresh_field('amenities');
		}

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
	
	property_price: function(frm){
		frm.compute_total(frm);
	},
	discount: function(frm){
		frm.compute_total(frm);
		frm.copy_discount(frm);
	}
});


frappe.ui.form.on('Property Amenity Detail', {
	amenity: function(frm, cdt, cdn){
		let row = locals[cdt][cdn];
		frm.check_flat_against_outdoor_kitchen(frm, row);
		frm.check_amenities_duplicate(frm, row, row.amenity);
		frm.compute_total(frm);
	},
	amenities_remove: function(frm, cdt, cdn) {
		console.log('Removed')
	}
})