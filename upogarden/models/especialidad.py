# -*- coding: utf-8 -*-

from odoo import models, fields, api


class especialidad(models.Model):
    _name = 'upogarden.especialidad'
    
    _rec_name="id_especialidad"
    id_especialidad=fields.Char("ID", size=64, required=True)
    descripcion=fields.Char("Descripcion", size=64, required=True)
    