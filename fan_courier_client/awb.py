import requests

from fan_courier_client.common import BaseObject
from fan_courier_client.constants import MAIN_URL
from fan_courier_client.decorators import validate
from fan_courier_client.utils import csv_to_json, json_to_csv_file


class Awb(BaseObject):
    get_awb_url = 'view_awb_integrat.php'
    export_awb_url = 'view_awb_integrat_pdf.php'
    create_awb_url = 'import_awb_integrat.php'
    delete_awb_url = 'delete_awb_integrat.php'
    download_awb_url = 'download_awb_scan_integrat.php'
    error_list_awb_url = 'export_lista_erori_imp_awb_integrat.php'
    download_awb_scan_url = 'download_awb_scan_integrat.php'
    tracking_awb_url = 'awb_tracking_integrat.php'
    tracking_awb_list_url = 'awb_tracking_list_integrat.php'

    def get(self, awb_id, **kwargs):
        kwargs.update(nr=awb_id)
        kwargs.update(self.params)
        response = requests.post(f'{MAIN_URL}/{self.get_awb_url}', data=kwargs)
        return response.content

    fields = {
        'tip_serviciu': {},
        'banca': {},
        'iban': {},
        'nr_plicuri': {},
        'nr_colete': {},
        'greutate': {},
        'plata_expeditie': {},
        'rambursbani': {},
        'plata_ramburs_la': {},
        'valoare_declarata': {},
        'persoana_contact_expeditor': {},
        'observatii': {},
        'continut': {},
        'nume_destinatar': {},
        'persoana_contact': {},
        'telefon': {},
        'fax': {},
        'email': {},
        'judet': {},
        'localitatea': {},
        'strada': {},
        'nr': {},
        'cod_postal': {},
        'bloc': {},
        'scara': {},
        'etaj': {},
        'apartament': {},
        'inaltime_pachet': {},
        'latime_pachet': {},
        'lungime_pachet': {},
        'restituire': {},
        'centru_cost': {},
        'optiuni': {},
        'packing': {},
        'date_personale': {},
    }

    nomenclatures = {
        'tip_serviciu': 'Tip serviciu',
        'banca': 'Banca',
        'iban': 'IBAN',
        'nr_plicuri': 'Nr. Plicuri',
        'nr_colete': 'Nr. Colete',
        'greutate': 'Greutate',
        'plata_expeditie': 'Plata expeditie',
        'rambursbani': 'Ramburs(bani)',
        'plata_ramburs_la': 'Plata ramburs la',
        'valoare_declarata': 'Valoare declarata',
        'persoana_contact_expeditor': 'Persoana contact expeditor',
        'observatii': 'Observatii',
        'continut': 'Continut',
        'nume_destinatar': 'Nume destinatar',
        'persoana_contact': 'Persoana contact',
        'telefon': 'Telefon',
        'fax': 'Fax',
        'email': 'Email',
        'judet': 'Judet',
        'localitatea': 'Localitatea',
        'strada': 'Strada',
        'nr': 'Nr',
        'cod_postal': 'Cod postal',
        'bloc': 'Bloc',
        'scara': 'Scara',
        'etaj': 'Etaj',
        'apartament': 'Apartament',
        'inaltime_pachet': 'Inaltime pachet',
        'latime_pachet': 'Latime pachet',
        'lungime_pachet': 'Lungime pachet',
        'restituire': 'Restituire',
        'centru_cost': 'Centru Cost',
        'optiuni': 'Optiuni',
        'packing': 'Packing',
        'date_personale': 'Date personale',
    }

    @validate(fields)
    def create(self, **kwargs):
        files = {'fisier': json_to_csv_file(kwargs, self.nomenclatures)}
        response = requests.post(f'{MAIN_URL}/{self.create_awb_url}', files=files, data=self.params)
        return csv_to_json(response.text, ['number', 'success', 'awb_id', 'tariff'])

    def export(self, awb_id, **kwargs):
        kwargs.update(nr=awb_id)
        kwargs.update(self.params)
        response = requests.post(f'{MAIN_URL}/{self.export_awb_url}', data=kwargs)
        return response.content

    def delete(self, awb_id):
        data = {'AWB': awb_id}
        data.update(self.params)
        response = requests.post(f'{MAIN_URL}/{self.delete_awb_url}', data=data)
        return response.text

    def tracking(self, awb_id, display_mode=5, **kwargs):
        kwargs.update(AWB=awb_id, display_mode=display_mode)
        kwargs.update(self.params)

        response = requests.post(f'{MAIN_URL}/{self.tracking_awb_url}', data=kwargs)
        return response.json() if display_mode == 5 else response.text

    def tracking_list(self, awb_list, **kwargs):
        kwargs.update(awburi=awb_list, standard=4, **self.params)
        response = requests.post(f'{MAIN_URL}/{self.tracking_awb_list_url}', data=kwargs)
        return response.json()

    def download(self, awb_id, **kwargs):
        kwargs.update(AWB=awb_id)
        kwargs.update(self.params)
        response = requests.post(f'{MAIN_URL}/{self.download_awb_url}', data=kwargs)
        return response.text

    def download_scan(self, awb_id, **kwargs):
        kwargs.update(AWB=awb_id)
        kwargs.update(self.params)
        response = requests.post(f'{MAIN_URL}/{self.download_awb_scan_url}', data=kwargs)
        return response.text

    def errors(self):
        response = requests.post(f'{MAIN_URL}/{self.error_list_awb_url}', data=self.params)
        return csv_to_json(response.text)
