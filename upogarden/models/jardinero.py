# -*- coding: utf-8 -*-

from odoo import models, fields, api


class jardinero(models.Model):
    _name = 'upogarden.jardinero'
    _inherit = 'upogarden.trabajador'
    turno = fields.Char('Turno', size=64, required=True)
