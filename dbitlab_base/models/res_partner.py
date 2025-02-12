# -*- coding: utf-8 -*-


from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    code = fields.Char(string="Code")
    alias = fields.Char(string="Alias")
    customer_class = fields.Char(string="Customer Class")
    ledger_id = fields.Integer(string="Ledger ID")
    route_id = fields.Many2one('route.customer', string="Route")
