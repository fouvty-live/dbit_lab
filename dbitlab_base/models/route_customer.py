# -*- coding: utf-8 -*-

from odoo import models, fields


class RouteCustomer(models.Model):
    _name = 'route.customer'
    _description = 'Route Customer'

    name = fields.Char(string="Name", required=True)
