# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime as dt


class contratacion(models.Model):
    _name = 'upogarden.contratacion'
    
    _rec_name="id_contratacion"
    id_contratacion = fields.Char('ID', size=64, required=True)
    fecha_Inicio = fields.Date('Desde',required=True,autodate = True)
    fecha_Fin = fields.Date('Hasta',required=True, autodate = True)
    lugar = fields.Char('Lugar', size=64, required=True)
    servicios_ids = fields.Many2many('upogarden.servicio',string="Servicios")
    cliente_id = fields.Many2one("upogarden.cliente","Cliente")
    tiempo_Total = fields.Float('Tiempo total', compute="calcula_tiempo_total", store=True)
    
    state = fields.Selection([('creada','Creada'),
                              ('enproceso','En proceso'),
                              ('finalizado','Finalizado'),],
                              'Estado',
                              default='creada')
    @api.one
    def btn_submit_to_enproceso(self):
        self.write({'state':'enproceso'})
        
    @api.one
    def btn_submit_to_finalizado(self):
        self.write({'state':'finalizado'})
    
    @api.one
    @api.constrains('state','servicios_ids','cliente_id')
    def check_state(self):
        if self.state == 'creada' and (len(self.servicios_ids) == 0 or len(self.cliente_id) == 0):
            raise models.ValidationError('La contratación debe tener asignado un servicio y un cliente para pasar a estar en proceso.')
        
    @api.depends('fecha_Inicio','fecha_Fin')
    def calcula_tiempo_total(self):
        self.tiempo_Total = (dt.strptime(self.fecha_Fin,'%Y-%m-%d') - dt.strptime(self.fecha_Inicio,'%Y-%m-%d')).days
        
    _sql_constraints = [
        ('id_contratacion', 'UNIQUE (id_contratacion)',  'No se pueden crear dos contrataciones con el mismo id.')
    ]
        
        