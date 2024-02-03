from odoo import models,fields
import logging
_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = 'res.partner'

    count_inmuebles = fields.Integer('Inmuebles', compute='_compute_count_inmuebles')

    def _compute_count_inmuebles(self):
        self.count_inmuebles = self.env["inmueble"].search_count([('owner_id','=',self.id)])


    def action_open_list_inmuebles(self):
        return {
            "type": "ir.actions.act_window",
            "name":f"Inmuebles de {self.name}",
            "res_model": "inmueble",
            "view_mode":"tree,form",
            "target":"current",
            "domain":[("owner_id","=",self.id)]
        }