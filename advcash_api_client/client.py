from hashlib import sha256
from datetime import datetime
from zeep.client import Client


class AvdCashAPIClient:
    wsdl = 'https://wallet.advcash.com/wsm/merchantWebService?wsdl'

    def __init__(self, api_name: str, api_secret: str, account_email: str):
        self.api_name = api_name
        self.api_secret = api_secret
        self.account_email = account_email
        self.client = Client(self.wsdl)

    def make_auth_token(self) -> str:
        """
        Makes sha256 from API Password:Date UTC in YYYYMMDD format:Time UTC in HH format (only hours, not minutes)
        like Merchant API required
        :return: str
        """
        now_str = datetime.utcnow().strftime('%Y%m%d:%H')
        encoded_string = '{}:{}'.format(self.api_secret, now_str).encode('utf8')
        return sha256(encoded_string).hexdigest().upper()

    def make_auth_params(self) -> dict:
        return {
            'apiName': self.api_name,
            'authenticationToken': self.make_auth_token(),
            'accountEmail': self.account_email
        }

    def make_request(self, action_name: str, params: dict=None):
        action = getattr(self.client.service, action_name)
        return action(self.make_auth_params())

    def get_balances(self):
        response = self.make_request('getBalances')
        return {i['id']: i['amount'] for i in response}
