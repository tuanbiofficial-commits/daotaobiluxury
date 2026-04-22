import frappe


def execute():
	"""Default the 'Send Welcome Email' checkbox on User form to OFF.

	BILUXURY onboards ~400 employees in bulk; the welcome email is noise for
	admin-created accounts. Admin can still tick the box manually per user.
	"""
	existing = frappe.db.exists(
		"Property Setter",
		{
			"doc_type": "User",
			"field_name": "send_welcome_email",
			"property": "default",
		},
	)

	if existing:
		frappe.db.set_value("Property Setter", existing, "value", "0")
	else:
		frappe.get_doc(
			{
				"doctype": "Property Setter",
				"doctype_or_field": "DocField",
				"doc_type": "User",
				"field_name": "send_welcome_email",
				"property": "default",
				"property_type": "Text",
				"value": "0",
			}
		).insert(ignore_permissions=True)

	frappe.clear_cache(doctype="User")
