# -*- coding: utf-8 -*-

from odoo import models, fields # Mandatory


class Customer(models.Model):
    _name = 'custome_order.customer' # name_of_module.name_of_class 
    _description = 'Customer Order' # Some note of table

    # Header
    name = fields.Char(required=1, string="Nama Customer")
    email = fields.Char()
    whatsapp = fields.Char(string="No HP/Whatsapp")