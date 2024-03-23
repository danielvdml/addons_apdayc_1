from odoo import models,fields,api,tools

class InmuebleReport(models.Model):
    _name = 'inmueble.report'
    _description = 'Inmueble Report'
    _auto = False

    name = fields.Char(string='Nombre', required=True)
    type = fields.Selection([('venta', 'Venta'),('alquiler', 'Alquiler')])
    parent_owner_id = fields.Many2one('res.partner', string='Propietario Padre')
    owner_id = fields.Many2one('res.partner', string='Propietario Hijo')
    street = fields.Char(string='Dirección')
    value = fields.Float("Valor")
    currency_id = fields.Many2one('res.currency', string='Moneda')

    partner_id = fields.Many2one("res.partner",string="Interesado")

    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)

        self._cr.execute("""
            CREATE OR REPLACE VIEW %s AS (
                select ROW_NUMBER() OVER (ORDER BY i.id asc) id,
                        i.name,
                        rp1.id owner_id,
                        rp2.id parent_owner_id,
                        i.type,
                        i.street,
                        i.value,
                        i.currency_id,
                        irprel.res_partner_id as partner_id
                    from inmueble i
                    left join res_partner rp1 on rp1.id = i.owner_id 
                    left join res_partner rp2 on rp2.id = rp1.parent_id
                    left join inmueble_res_partner_rel  irprel on irprel.inmueble_id = i.id
                    where irprel.res_partner_id  is not null
            )
        """ % self._table)