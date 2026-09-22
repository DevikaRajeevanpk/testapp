// Copyright (c) 2026, devika and contributors
// For license information, please see license.txt

frappe.ui.form.on("Product", {
	refresh(frm) {
		render_qr_code(frm);
	},
	validate(frm) {
		const code = (frm.doc.product_code || "").trim();
		if (!code) {
			return;
		}
		if (!/^[A-Za-z0-9][A-Za-z0-9._-]*$/.test(code)) {
			frappe.throw(
				__(
					"Product Code must start with a letter or digit and may only contain letters, digits, dots, hyphens, and underscores."
				)
			);
		}
	},
	qr_code(frm) {
		render_qr_code(frm);
	},
	product_code(frm) {
		const code = (frm.doc.product_code || "").trim();
		if (frm.doc.product_code && frm.doc.product_code !== code) {
			frm.set_value("product_code", code);
			return;
		}
		if (!frm.doc.qr_code && code) {
			frm.set_value("qr_code", code);
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
	const escaped_alt = frappe.utils.escape_html(__("Product QR Code"));
	field.$wrapper.html(
		`<img src="${src}" alt="${escaped_alt}" class="product-qr-preview" style="max-width: 160px; height: auto;" />`
	);
	field.$wrapper.find("img").on("error", function () {
		field.$wrapper.html(
			`<p class="text-muted">${__("QR preview could not be loaded. The QR Code value is still saved.")}</p>`
		);
	});
}
