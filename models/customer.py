# -*- coding: utf-8 -*-

from odoo import models, fields, api # Mandatory


class Customer(models.Model):
    _name = 'custom_order.customer' # name_of_module.name_of_class 
    _description = 'Customer Order' # Some note of table
    _rec_name = 'name'

    # Header
    name = fields.Char(string="Nama Customer")
    last_name = fields.Char()
    full_name = fields.Char(compute="_compute_full_name")
    email = fields.Char()
    whatsapp = fields.Char(string="No HP/Whatsapp", default="08")
    hp = fields.Integer()
    gender = fields.Selection([('M', 'Male'), ('F', 'Female')], default="M")
    title = fields.Char()
    photo_profile = fields.Binary()
    address = fields.Text()

    @api.onchange('name', 'last_name')
    def _compute_full_name(self):
        for record in self:
            if(record.name == False or record.last_name == False):
                record.full_name = ' '
            else:
                record.full_name = record.name + " " + record.last_name

    @api.onchange('gender')
    def _onchange_gender(self):
        if self.gender != False:
            if self.gender == "M":
                self.title = "Gentleman"
            else :
                self.title = "Ladies"