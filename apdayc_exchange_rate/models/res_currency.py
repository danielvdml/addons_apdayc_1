from odoo import models,api
from odoo.exceptions import UserError, ValidationError


from ..services.apimigo import ApimigoService

class ResCurrency(models.Model):
    _inherit = "res.currency"

    @api.model
    def action_cron_update_exchange_rate_pen_usd(self):
        #ACCESS_KEY = self.env["ir.config_parameter"].get_param("APIMIGO_ACCESS_KEY")
        #service = ApimigoService(ACCESS_KEY)

        service = self.env.user_id.company_id.instance_apimigo_service()

        exchange_latest = service.request_exchange_latest()

        currency_usd = self.env.ref("base.USD")
        
        if self.env.user.company_id.currency_id == self.env.ref("base.PEN"):
            if exchange_latest.get("success",False):
                date = exchange_latest.get("fecha")
                if not self.env["res.currency.rate"].search([("name","=",date),("currency_id","=",currency_usd.id)]).exists():
                    self.env['res.currency.rate'].create({
                        'currency_id': currency_usd.id,
                        'name': date,
                        'inverse_company_rate': exchange_latest.get("precio_compra"),
                        'company_rate': 1/exchange_latest.get("precio_compra"),
                    })
                    return True
        return False

    def action_update_exchange_rate_pen_usd(self):
        self.ensure_one()
        currency_usd = self.env.ref("base.USD")
        if currency_usd != self:
            raise UserError("Este método solo es para la moneda USD")
        
        #ACCESS_KEY = self.env["ir.config_parameter"].get_param("APIMIGO_ACCESS_KEY")
        #service = ApimigoService(ACCESS_KEY)
        
        service = self.env.user_id.company_id.instance_apimigo_service()

        result_exchanges_date = service.request_exchange('2023-01-01','2023-05-31')

        if result_exchanges_date.get("success",False):
            exchanges_date = result_exchanges_date.get("data",[])
            #{'fecha': '2024-01-04', 'moneda': 'USD', 'precio_compra': '3.726', 'precio_venta': '3.738'}

            #Filtro todos los registros que ya existan
            exchanges_date = [r for r in exchanges_date 
                                            if not self.env["res.currency.rate"].search([("name","=",r.get("fecha")),("currency_id","=",currency_usd.id)]).exists()]
            #Preparo los registros(tipos de cambio y fecha) para ser insertados
            vals_exchanges_date = list(map(lambda r:{'currency_id':currency_usd.id,
                                                    'name':r.get("fecha"),
                                                    'inverse_company_rate':float(r.get('precio_compra')),
                                                    'company_rate':1/float(r.get('precio_compra'))},exchanges_date))
            #Creo los registros
            self.env['res.currency.rate'].create(vals_exchanges_date)