from odoo import models,fields,api

class ResPartner(models.Model):
    _inherit = "res.partner" 

    #Forma 1: usando el campo default_creditlimit de res.config.settings
    creditlimit = fields.Float(string="Credit Limit",default=10000)

    #Forma 2: usando el atributo related para relacionar el campo default_creditlimit con el campo def_creditlimit de res.config.settings
    #creditlimit = fields.Float(string="Credit Limit",default=lambda self:self.env.cr.company_id.default_creditlimit)