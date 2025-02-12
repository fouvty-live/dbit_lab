# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    group_id = fields.Many2one('product.group', string="Product Group")
    brand_id = fields.Many2one('product.brand', string="Product Brand")