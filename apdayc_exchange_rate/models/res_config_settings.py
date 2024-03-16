from odoo import models,fields,api
from odoo.addons.apdayc_exchange_rate.services.apimigo import ApimigoService

class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"
    

    apimigo_access_token = fields.Char(string="Apimigo Access Token")

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res['apimigo_access_token'] = self.env['ir.config_parameter'].sudo().get_param('APIMIGO_ACCESS_KEY')
        return res
    
    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('APIMIGO_ACCESS_KEY', self.apimigo_access_token)


class ResCompany(models.Model):
    _inherit = "res.company"

    def instance_apimigo_service(self):
        return ApimigoService(self.env['ir.config_parameter'].sudo().get_param('APIMIGO_ACCESS_KEY'))