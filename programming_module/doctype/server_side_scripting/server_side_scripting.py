# Copyright (c) 2024, my-site and contributors
# For license information, please see license.txt

# import frappe
# Copyright (c) 2024, my-site and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document

class ServerSideScripting(Document):
    pass
#server side call

    # @frappe.whitelist()
    # def frm_call(self,msg):
    #     import time
    #     time.sleep(5)
    #     # frappe.msgprint(msg)
    #     self.mob_no= 8748378742

        # return "Hi This Message from frm_call"

    # sql

    # frappe.db.sql(query, filters, as_dict)

        # def validate(self):
        #     self.sql()

        # def sql(self):
        #     data = frappe.db.sql("""
        #                             SELECT
        #                                 first_name,
        #                                 age
        #                             FROM
        #                                 `tabClient Side Scripting`
        #                             WHERE
        #                                 enable = 1
        #                         """, as_dict=1)
            
        #     for d in data:
        #         frappe.msgprint(_("The Parent First Name is {0} and age is {1}").format(d.first_name, d.age))


# count

# frappe.db.count(doctype, filters)

    # def validate(self):
    #     doc_count = frappe.db.count('Client Side Scripting', {'enable': 1})
    #     frappe.msgprint(_("The Enable Document Count is {0}").format(doc_count))

    # exists

    # frappe.db.exists(doctype, name)

    # def validate(self):
    #     if frappe.db.exists('Client Side Scripting', 'PR-0028'):
    #         frappe.msgprint(_("The Document is Exists in Database"))

    #     else:
    #         frappe.msgprint(_("The Document does not Exists in Database"))

    # set_value

# frappe.db.set_value(doctype, name, fieldname, value)

    # def validate(self):
    #     self.set_value()

    # def set_value(self):
    #     frappe.db.set_value('Client Side Scripting', 'PR_0012', 'age', 25)

    #     first_name, age = frappe.db.get_value('Client Side Scripting', 'PR-0012', ['first_name', 'age'])
    #     frappe.msgprint("The Parent First Name is {0} and new age is {1}".format(first_name,age))



    # get_value

    # frappe.db.get_value(doctype, name, fieldname) or frappe.db.get_value(doctype, filters, fieldname )

    # def validate(self):
    #     self.get_value()

    # def get_value(self):
        # first_name, age = frappe.db.get_value('Client Side Scripting', 'PR-0012', ['first_name', 'age'])
        # frappe.msgprint(_("The Parent Name is {0} and age is {1}").format(first_name,age))

# get_list

# frappe.db.get_list(doctype, filters, or_filters, fields, order_by, group_by, start, page_length)

    # def validate(self):
    #     self.get_list()

    # def get_list(self):
    #     doc = frappe.db.get_list('Client Side Scripting',
    #                          filters={
    #                              'enable' : 1
    #                          },
    #                          fields=['first_name','age']
    #                          )
    #     for d in doc:
    #         frappe.msgprint(_("The Parent First Name is {0} and age is {1}").format(d.first_name,d.age))

    # def validate(self):
    #     self.save_document()

    # def save_document(self):
    #         doc = frappe.new_doc('Client Side Scripting')
    #         doc.first_name = 'Jake'
    #         doc.last_name = 'Jay'
    #         doc.age = 13
    #         doc.save()

    #         doc.save(
    #              ignore_permissions=True,
    #              ignore_version=True
    #         )


    # frappe.delete_doc( doctype, name )

    # def validate(self):
    #     frappe.delete_doc('Client Side Scripting', 'PR-0013')

# frappe.new_doc(doctype)

    # def validate(self):
    #     self.new_document()

    # def new_document(self):
    #         doc = frappe.new_doc('Client Side Scripting')
    #         doc.first_name = 'Jake'
    #         doc.last_name = 'Jay'
    #         doc.age = 13
    #         doc.append("family_members",{ "name1":"jain",
    #                                      "relation":"Sister",
    #                                      "age":14})

    #         doc.insert()

    # def get_document(self):
    #     doc = frappe.get_doc('Client Side Scripting', self.client_side_doc)
    #     frappe.msgprint("The First Name is {0} and Age is {1}".format(doc.first_name, doc.age))

    #     for row in doc.get("family_members"):
    #         frappe.msgprint("{0}. The family member name is '{1}' and relation is '{2}' ".format(row.idx,row.name1,row.relation))


    # def validate(self):
    #     frappe.msgprint(_("Hello My full name is '{0}' ").format(
    #         self.first_name + " " + self.middle_name + " " + self.last_name))

    # def validate(self):
        # for row in self.get("family_members"):
        #     frappe.msgprint(_(
        #         "{0}. The family member name is '{1}' and relation is '{2}' "
        #     ).format(
        #         row.idx,row.name1,row.relation
        #     ))
        

    # def before_submit(self):
    # 	frappe.msgprint("Hello")

    # def on_submit(self):
    # 	frappe.msgprint("Hello")

    # def validate(self):
        # frappe.msgprint("Hello")

# def before_save(self):
# 	frappe.msgprint("Hello")

    # def before_insert(self):
    # 	frappe.msgprint("Hello")


# def after_insert(self):
# 		frappe.msgprint("Hello")

    # 	def on_update(self):
    # 		frappe.msgprint("Hello")


# def on_cancel(self):
# 		frappe.msgprint("Hello")

# def on_trash(self):
# 		frappe.msgprint("Hello")
# def after_delete(self):
# 		frappe.msgprint("Hello")

