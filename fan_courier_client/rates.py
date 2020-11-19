import requests

from fan_courier_client.common import BaseObject
from fan_courier_client.constants import MAIN_URL
from fan_courier_client.decorators import validate
from fan_courier_client.services import Service


class Rate(BaseObject):
    rate_url = 'tarif.php'

    validation_fields = {
        'serviciu': {
            'type': str,
            'choices': Service().get(),
        },
        'localitate_dest': {
            'type': str
        },
        'judet_dest': {
            'type': str
        },
        'plicuri': {
            'type': int
        },
        'colete': {
            'type': int
        },
        'greutate': {
            'type': int
        },
        'lungime': {
            'type': int
        },
        'latime': {
            'type': int
        },
        'inaltime': {
            'type': int
        },
        'val_decl': {
            'type': int
        },
        'plata_ramburs': {
            'type': str,
            'choices': ['destinatar', 'expeditor']
        },
        'optiuni': {
            'type': str
        },
    }

    @validate(validation_fields)
    def get(self, **kwargs):
        kwargs.update(self.params)
        response = requests.post(f'{MAIN_URL}/{self.rate_url}', data=kwargs).text
        return int(response) if response.isdigit() else response
