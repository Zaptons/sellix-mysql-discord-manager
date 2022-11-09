import requests
import json



class SellixApi():

    def __init__(self, api_key):
        self.api_key = 'YOURAPIKEY'

    def authorize(self, order_id):
        res = requests.get('https://dev.sellix.io/v1/orders/{}'.format(order_id), headers={
            'Authorization': 'Bearer {}'.format(self.api_key)
        })

        if res.status_code == 200:

            # lets get the json response
            json_data = json.loads(res.text)

            # we have to define status codes like this because sellix api is so fucking retarded
            if json_data['status'] == 400 or json_data['status'] == 404 or json_data['status'] == 500:
                return 'error'

            if json_data['data']['order']['status'] != 'COMPLETED':
                return 'pending'

            # this is how we get the product id string
            if json_data['data']['order']['product_id'] == 'PRODUCTID':
                cfg = 'beta'
            elif json_data['data']['order']['product_id'] == 'PRODUCTID':
                cfg = 'live'
            elif json_data['data']['order']['product_id'] == 'PRODUCTID':
                cfg = 'upgrade'
            return cfg

        else:
            return 'error'