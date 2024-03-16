from odoo import models,fields,api

class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    #Forma 1: usando el campo default_creditlimit de res.config.settings
    default_creditlimit = fields.Float(string="Default Credit Limit",default_model="res.partner")

    #Forma 2: usando el atributo related para relacionar el campo default_creditlimit con el campo def_creditlimit de res.config.settings
    def_creditlimit = fields.Float(string="Default Credit Limit",related="company_id.default_creditlimit",readonly=False)
