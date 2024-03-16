from odoo import models,fields,api


class ResCompany(models.Model):
    _inherit = "res.company"

    default_creditlimit = fields.Float(string="Default Credit Limit")