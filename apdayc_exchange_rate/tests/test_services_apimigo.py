from odoo.tests.common import TransactionCase
from odoo.tests import tagged
from ..services.apimigo import ApimigoService

import logging
_logger = logging.getLogger(__name__)



class TestServicesAPIMigo(TransactionCase):

    @classmethod
    def setUpClass(self):
        super().setUpClass()
        self.ACCESS_KEY = self.env["ir.config_parameter"].get_param("APIMIGO_ACCESS_KEY")

    def test_request_exchange_date_200(self):
        """
        La función request_exchange date debe devolver una estructura diccionario que contenga (success,fecha,moneda,precio_compra,precio_venta )
        """
        service = ApimigoService(self.ACCESS_KEY)
        exchange_date = service.request_exchange_date("2024-01-05")
        if exchange_date.get("success"):
            self.assertTrue("fecha" in exchange_date)
            self.assertTrue("precio_compra" in exchange_date)
            self.assertTrue("precio_venta" in exchange_date)
            self.assertTrue(type(exchange_date.get("precio_venta",0)) == float)
            self.assertTrue(type(exchange_date.get("precio_compra",0)) == float)
        
    def test_request_exchange_date_400(self):
        """
        La función request_exchange date debe devolver una estructura diccionario que contenga (success,fecha,moneda,precio_compra,precio_venta )
        """
        service = ApimigoService(self.ACCESS_KEY)
        exchange_date = service.request_exchange_date("2024-01-01")
        if exchange_date.get("success"):
            self.assertTrue("fecha" in exchange_date)
            self.assertTrue("precio_compra" in exchange_date)
            self.assertTrue("precio_venta" in exchange_date)


    def test_request_exchange_latest(self):
        service = ApimigoService(self.ACCESS_KEY)
        exchange_date = service.request_exchange_latest()
        if exchange_date.get("success"):
            self.assertTrue("fecha" in exchange_date)
            self.assertTrue("precio_compra" in exchange_date)
            self.assertTrue("precio_venta" in exchange_date)
            self.assertTrue(type(exchange_date.get("precio_venta",0)) == float)
            self.assertTrue(type(exchange_date.get("precio_compra",0)) == float)


    def test_action_cron_update_exchange_rate_pen_usd_1(self):
        result = self.env["res.currency"].action_cron_update_exchange_rate_pen_usd()

    
    def test_request_exchange_1(self):
        service = ApimigoService(self.ACCESS_KEY)
        exchanges_date = service.request_exchange("2024-01-01","2024-01-31")
        _logger.info(exchanges_date)

    def test_request_exchange_2(self):
        service = ApimigoService(self.ACCESS_KEY)
        exchanges_date = service.request_exchange("2024-04-01","2024-04-31")
        _logger.info(exchanges_date)