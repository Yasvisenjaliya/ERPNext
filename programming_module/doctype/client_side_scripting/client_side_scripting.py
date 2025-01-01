# # Copyright (c) 2024, my-site and contributors
# # For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ClientSideScripting(Document):
		pass

# @frappe.whitelist()
# def frappe_call(self,msg):
#         import time
#         time.sleep(5)
#         # frappe.msgprint(msg)
#         self.mob_no= 8748378742
#         self.save()

#         return "Hi This Message from frappe_call"