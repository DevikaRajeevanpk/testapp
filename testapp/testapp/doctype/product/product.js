// Copyright (c) 2026, devika and contributors
// For license information, please see license.txt

frappe.ui.form.on("Product", {
	refresh(frm) {
		render_qr_code(frm);
	},
	qr_code(frm) {
		render_qr_code(frm);
	},
	product_code(frm) {
		if (!frm.doc.qr_code && frm.doc.product_code) {
			frm.set_value("qr_code", frm.doc.product_code);
			return;
		}
		render_qr_code(frm);
	},
});

function render_qr_code(frm) {
	const field = frm.get_field("qr_code_preview");
	if (!field) {
		return;
	}

	const data = frm.doc.qr_code || frm.doc.product_code;
	if (!data) {
		field.$wrapper.html(
			`<p class="text-muted">${__("Enter a Product Code to generate the QR code.")}</p>`
		);
		return;
	}

	const src = `https://api.qrserver.com/v1/create-qr-code/?size=160x160&data=${encodeURIComponent(data)}`;
	field.$wrapper.html(
		`<img src="${src}" alt="${__("Product QR Code")}" style="max-width: 160px; height: auto;" />`
	);
}
