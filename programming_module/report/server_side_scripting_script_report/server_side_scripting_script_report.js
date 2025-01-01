// Copyright (c) 2024, my-site and contributors
// For license information, please see license.txt

frappe.query_reports["Server Side Scripting Script Report"] = {
    "filters": [
        {
            "fieldname": "name",
            "label": _("Server Side Scripting"),
            "Fieldtype": "Link",
            "options": "Server Side Scripting"
        },
        {
            "fieldname": "dob",
            "label": _("DOB"),
            "fieldtype": "Date",
        },
        {
            "fieldname": "age",
            "label": _("Age"),
            "fieldtype": "Int",
        }

    ]
};
