# -*- coding: utf-8 -*-

from odoo import models, fields, api


class contratacion(models.Model):
    _name = 'upogarden.contratacion'
    
    _rec_name="id_contratacion"
    id_contratacion = fields.Char('ID', size=64, required=True)
    fecha_Inicio = fields.Datetime('Desde',required=True,autodate = True)
    fecha_Fin = fields.Datetime('Hasta',required=True, autodate = True)
    lugar = fields.Char('Lugar', size=64, required=True)
    servicios_ids = fields.Many2many('upogarden.servicio',string="Servicios")
    cliente_id = fields.Many2one("upogarden.cliente","Cliente")
    #tiempo_Total = fecha_Fin - fecha_Inicio
    #poner el tiempo_Total automatico