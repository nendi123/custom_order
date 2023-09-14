# -*- coding: utf-8 -*-

from odoo import models, fields # Mandatory
import webbrowser


class Produk(models.Model):
    _name = 'custom_order.produk' # name_of_module.name_of_class 
    _description = 'Produk Order' # Some note of table

    # Header
    name = fields.Char(required=1, string="Nama Produk")
    quantity = fields.Integer()
    desc = fields.Html()
    price = fields.Integer()
    category_id = fields.Many2one(comodel_name="custom_order.category")

    def set_kosong(self):
        self.quantity = 0
        webbrowser.open_new_tab('https://google.com')