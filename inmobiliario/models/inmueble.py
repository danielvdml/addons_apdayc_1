from odoo import models,fields

class Inmueble(models.Model):
    _name = "inmueble"
    _description = "Inmuebles"
    _inherit = ['mail.thread.cc','mail.activity.mixin','mail.thread.main.attachment']

    name = fields.Char(string="Nombre", required=True)  
    street = fields.Char(string="Dirección", required=True)
    type = fields.Selection([('casa', 'Casa'), 
                            ('departamento', 'Departamento')], 
                            string="Tipo")

    value = fields.Float(string="Valor", required=True)

    currency_id = fields.Many2one("res.currency",string="Moneda")
    owner_id = fields.Many2one("res.partner",string="Propietario")

    state = fields.Selection([('disponible', 'Disponible'),
                                ('alquilado', 'Alquilado'),
                                ('vendido', 'Vendido')] )
    
    image = fields.Binary(string="Imagen")

    description = fields.Text(string="Descripción")


    partner_ids = fields.Many2many("res.partner",string="Interesados")