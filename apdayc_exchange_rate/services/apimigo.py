import requests
import logging
_logger = logging.getLogger(__name__)

ENDPOINT = "https://api.migo.pe/api/v1"
API_EXCHANGE = f"{ENDPOINT}/exchange"
API_EXCHANGE_DATE = f"{ENDPOINT}/exchange/date"
API_EXCHANGE_LATEST = f"{ENDPOINT}/exchange/latest"
API_EXCHANGE_RUC= f"{ENDPOINT}/ruc"


class ApimigoService:
    
    def __init__(self,ACCESS_KEY):
        self.ACCESS_KEY = ACCESS_KEY

    def _post(self,api_url,args):
        headers = {
                "accept": "application/json",
                "content-type": "application/json"
            }
        payload = {
            "token": self.ACCESS_KEY,
        }
        payload.update(args)
        response = requests.post(api_url,json=payload,headers=headers)
        if response.status_code in (200,400):
            result = response.json()
        else:
            result = {}
        if not result.get("success",False):
                result = {}
        return result

    def request_exchange(self, date_start, date_end):
        """
        Devuelve json:  {'success': True, 
                        'data': [{'fecha': '2024-01-04', 'moneda': 'USD', 'precio_compra': '3.726', 'precio_venta': '3.738'}]}
        """
        result = self._post(API_EXCHANGE,{"fecha_inicio":date_start,"fecha_fin":date_end})
        return result
    
    def request_exchange_date(self, date):
        result = self._post(API_EXCHANGE_DATE,{"fecha":date})
        result["precio_venta"] = float(result.get("precio_venta",0))
        result["precio_compra"] = float(result.get("precio_compra",0))
        return result
        
    def request_exchange_latest(self):
        result = self._post(API_EXCHANGE_LATEST,{})
        result["precio_venta"] = float(result.get("precio_venta",0))
        result["precio_compra"] = float(result.get("precio_compra",0))
        return result
    
    def request_get_ruc(self,ruc):
        return self._post(API_EXCHANGE_RUC,{"ruc":ruc})