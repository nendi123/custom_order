# -*- coding: utf-8 -*-

from odoo import models, fields # Mandatory


class Category(models.Model):
    _name = 'custom_order.category' # name_of_module.name_of_class 
    _description = 'Category' # Some note of table

    # Header
    name = fields.Char(required=1, string="Nama Category")
    produk_ids = fields.One2many(comodel_name='custom_order.produk', inverse_name='category_id')