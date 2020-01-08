# -*- coding: utf-8 -*-

from odoo import models, fields, api


class trabajadorAjeno(models.Model):
    _name = 'upogarden.jardinero'
    _inherit = 'upogarden.trabajador'
    telefono = fields.Integer('Teléfono', required=True)
    disponibilidad = fields.Boolean('Disponibilidad', required=True)
    empresa = fields.Char('Empresa', size=64, required=True)
    experiencia = fields.Char('Experiencia', size=64, required=True)
    especialidad = fields.Char('Especialidad', size=64, required=True)
