# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductGroup(models.Model):
    _name = 'product.group'
    _description = 'Product Group'

    name = fields.Char(string="Group Name", required=True)
