// Copyright (c) 2024, my-site and contributors
// For license information, please see license.txt

frappe.ui.form.on('Client Side Scripting', {

    // validate: function (frm) {
    //     frappe.throw("Hello")
    // }

    // refresh: function (frm) {
    //     frappe.throw("Hello")
    // }




    // refresh(frm) {
    //     frm.set_intro("Now you  can create a new client side sripting doctype");
    //     // if (frm.is_new()) {
    //     //     frm.set_intro("Now you  can create a new client side sripting doctype")
    //     // }
    //     frappe.throw("Hello 'after_save' event");
    // },

    // validate:function(frm){

    // //     frm.set_value('full_name',frm.doc.first_name + " " + frm.doc.middle_name + " " + frm.doc.last_name)
    // let row = frm.add_child('family_members',{
    //     name1: 'john jose',
    //     relation: 'Father',
    //     age:56,
    // })
    // }


    // after_save: function(frm){
    //     frappe.throw("Hello 'after_save' event");

    // }

    // after_save:function(frm){
    //     frappe.msgprint(_("The Full Name is '{0}' ",[frm.doc.first_name + "" + frm.doc.middle_name + "" + frm.doc.last_name ]))

    //     for(let row of frm.doc.family_members){
    //         frappe.msgprint(_("{0}. The family member name is '{1}' and relation is '{2}' ", [row.idx, row.name1, row.relation]))
    //     }
    // }

    // enable:function(frm){
    //     // frm.set_df_property('first_name','reqd',1)

    //     // frm.set_df_property('middle_name','reqd',1)

    //     frm.toggle_reqd('age', true)
    // }

    // refresh: function (frm) {
    //     frm.add_custom_button('Click Me Button', () => {
    //         frappe.msgprint('You Clicked Me!!');
    //     })

    //     frm.add_custom_button('clicke Me1', () => {
    //         frappe.msgprint('you clicked 1 !!');
    //     }, 'click me')

    //     frm.add_custom_button('click Me2', () => {
    //         frappe.msgprint(' you clicked 2 !!');
    //     }, 'click me')
    // }

});
