from odoo import models,fields
import logging
_logger = logging.getLogger(__name__)

class WizardInmuebles(models.TransientModel):
    _name = 'apdayc.inmuebles.wizard'
    _description = 'Wizard para seleccionar inmuebles'

    type = fields.Selection([('casa', 'Casa'), 
                            ('departamento', 'Departamento')], 
                            string="Tipo")


    def action_print_report(self):
        inmuebles = self.env["inmueble"].search([("type","=",self.type)])
        _logger.info("Imprimir reportes")
        _logger.info(inmuebles)
        #report_obj = self.env["ir.actions.report"].search([("report_name","=","inmobiliario.report_inmueble")])
        report_obj = self.env.ref("inmobiliario.action_reporte_inmobiliario")
        _logger.info(report_obj)    

        return report_obj.report_action(inmuebles.ids)