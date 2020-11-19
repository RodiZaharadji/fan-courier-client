# Fan Courier Python API Client Library

A client developed as a library, easy to integrate Fan Courier in Python projects

Official documentation: [https://cloud.mail.ru/public/3ki1/2X2QSMyA2](https://cloud.mail.ru/public/3ki1/2X2QSMyA2)

## Install:
```bash
pip install fan-courier-client
```

## Initialization

```python
import fan_courier_client

client = fan_courier_client.Client(client_id, username, password)
```

## Get client list

```python
client.list()
```

```python
[
  {
    "client_id": "7024738",
    "nume": "FAN Courier Corespondenta Pipera",
    "adresa": "Bucuresti, Ridicare din sediul FAN Pipera (Sediu), , Sos Fabrica de Glucoza 11 C, 020331"
  },
  {
    "client_id": "7032158",
    "nume": "FAN COURIER - cont test",
    "adresa": "Bucuresti, Fabrica de Glucoza (sosea), 11C, FAN, 020331"
  },
  ...
]
```

## Get addresses list

```python
# Optional fields: 'judet', 'localitate', 'language'
client.addresses.get()
```
```python
[
    OrderedDict([
        ('judet', 'Alba'),
        ('localitate', 'Abrud'),
        ('strada', ''),
        ('de_la', '1'),
        ('pana_la', 'T'),
        ('paritate', '2'),
        ('cod_postal', '515100'),
        ('tip', ''),
        ('cod_cartare', '6642'),
        ('numar_depozit', 'R3.23'),
        ('id_strada', '124795'),
        ('cod_sortare_vizual', '01-02'),
        ('litera_cartare', 'F'),
        ('agentie', 'Campeni')
    ]),
    OrderedDict([
        ('judet', 'Alba'),
        ('localitate', 'Abrud'),
        ('strada', '1 Decembrie 1918'),
        ('de_la', '1'),
        ('pana_la', 'T'),
        ('paritate', '2'),
        ('cod_postal', '515100'),
        ('tip', 'Strada'),
        ('cod_cartare', '6642'),
        ('numar_depozit', 'R3.23'),
        ('id_strada', '149847'),
        ('cod_sortare_vizual', '01-02'),
        ('litera_cartare', 'F'),
        ('agentie', 'Campeni')
    ]),
    ...
]
```

## Get cities list

```python
client.addresses.cities()
```
```python
[
    OrderedDict([
        ('judet', 'Alba'),
        ('localitate', 'Abrud'),
        ('agentie', 'Campeni'),
        ('km', '0'),
        ('cod_rutare', '6641'),
        ('id_localitate_fan', '10001'),
        ('litera_cartare', 'F'),
        ('dep_no', 'R3.23')
    ]),
    OrderedDict([
        ('judet', 'Alba'),
        ('localitate', 'Abrud-Sat'),
        ('agentie', 'Campeni'),
        ('km', '0'),
        ('cod_rutare', '6641'),
        ('id_localitate_fan', '21913'),
        ('litera_cartare', 'F'),
        ('dep_no', 'R3.23')
    ]),
    ...
]
```

## Get rates

```python
request_data = {
    'serviciu': 'Standard',
    'localitate_dest': 'Vrancea',
    'judet_dest': 'Test',
    'plicuri': 1,
    'colete': 1,
    'greutate': 20,
    'lungime': 10,
    'latime': 10,
    'inaltime': 10,
    'val_decl': 10,
    'plata_ramburs': 'destinatar',
    'optiuni': 'A'
}

client.rates.get(**request_data)
```

```python
81.90
```

## Get AWB in HTML

```python
client.awb.get(awb_id=2324000120066)
```
```python
# html text response
b'\r\n<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//E... 
```

## Create AWB

```python
request_data = {
    'tip_serviciu': 'Standard',
    'banca': 'Test',
    'iban': 'XXXXXXX',
    'nr_plicuri': 1,
    'nr_colete': 0,
    'greutate': 1,
    'plata_expeditie': 'ramburs',
    'rambursbani': 100,
    'plata_ramburs_la': 'destinatar',
    'valoare_declarata': 400,
    'persoana_contact_expeditor': 'Test User',
    'observatii': 'Lorem ipsum',
    'continut': 'Fragil',
    'nume_destinatar': 'Test',
    'persoana_contact': 'Test',
    'telefon': '123456789',
    'fax': '123456789',
    'email': 'example@example.com',
    'judet': 'Galati',
    'localitatea': 'Tecuci',
    'strada': 'Lorem',
    'nr': '2',
    'cod_postal': '123456',
    'bloc': '',
    'scara': '',
    'etaj': '',
    'apartament': '',
    'inaltime_pachet': '',
    'latime_pachet': '',
    'lungime_pachet': '',
    'restituire': '',
    'centru_cost': '',
    'optiuni': '',
    'packing': '',
    'date_personale': ''
}
client.awb.create(**request_data)
```

```python
[
    OrderedDict([
        ('number', '1'),
        ('success', '1'),
        ('awb_id', '2324000120066'),
        ('tariff', '')
    ])
]
```

## Export AWB in PDF

```python
client.awb.export(awb_id=2324000120066)
```
```python
b'%PDF-1.4\n1 0 obj\n<<\n/Title (\xfe\xff)\n/Creator (\xfe\xff)\n/Producer...
```

## Delete AWB

```python
client.awb.delete(awb_id=2324000120066)
```
```python
'2324000120066 DELETED'
```

## Track AWB

```python
client.awb.tracking(awb_id=2324000120066)
```
|  Code  | Result |
|:------:|:------|
|2|Livrat|
|3|Avizat|
|6|Refuz primire|
|7|Refuz plata transport|
|8|Livrare din sediul FAN Courier|
|9|Redirectionat|
|12|Contactat, livrare ulterioara|
|14|Restrictii acces la adresa|
|15|Refuz predare ramburs|
|38|AWB neexpediat|
|42|Adresa gresita|
|43|Retur|
|47|Predat partener extern|
```python
{
  'progressdetail': None
}
```

## Track AWB list

```python
client.awb.tracking_list(awb_list=[2324000120066, 2322000120004])
```
```python
[
    {
        'awb': None,
        'oras destinatar': '',
        'continut': '',
        'nume confirmare': '',
        'data confirmare': '',
        'ora confirmare': '',
        'awb retur': '',
        'ramburs': '',
        'data virament': '',
        '0': {
            'id': 0,
            'status': 'AWB-ul nu a fost predat catre FAN Courier',
            'data': '',
            'ora': '',
            'oras': '',
            'traseu': ''
        }
    }
]
```

```python
client.awb.download(awb_id=2322000120004)  # text
client.awb.download_scan(awb_id=2322000120004)  # text
client.awb.errors()  # dict list
```

## Get services list

```python
client.services.get()
```
```python
[
    'Standard',
    'RedCode',
    'Caiet Sarcini',
    'Express Loco 1H',
    'Express Loco 2H',
    'Express Loco 4H',
    'Express Loco 6H',
    'Cont Colector',
    'Express Loco 1H-Cont Colector',
    'Express Loco 2H-Cont Colector',
    'Express Loco 4H-Cont Colector',
    'Express Loco 6H-Cont Colector',
    'Red code-Cont Colector',
    'Export',
    'Export-Cont Colector',
    'Produse Albe',
    'Produse Albe-Cont Colector',
    'Transport Marfa',
    'Transport Marfa-Cont Colector',
    'Transport Marfa Produse Albe',
    'Transport Marfa Produse Albe-Cont Colector'
]
```

## Get remarks list

Remarks
```python
client.remarks.get()
```
```python
[
    'Livrare urgenta',
    'Livrare Luni',
    'Livrare Luni-Apel telefonic inainte',
    'A se contacta telefonic',
    'Atentie-FRAGIL',
    'Livrare cu stampila si semnatura',
    'Livrare dupa ora 16:00',
    'Livrare in intervalul 09:00 - 17:00',
    'Livrare personala cu CNP/serie CI'
]
```

## Get sheet by date

```python
client.sheets.get(data='17.11.2020')
```
```python
[
    OrderedDict([
        ('nr_crt', '1'),
        ('awb', '2322000120004'),
        ('client_dest', 'asdasd asdasda'),
        ('telefon_dest', '0748069725'),
        ('stradadestinatar', 'Strada Campia Libertatii, nr. 43, bl. MC3, sc. A, et. 2, ap. 13'),
        ('nrdestinatar', ''),
        ('blocdestinatar', ''),
        ('scaradestinatar', ''),
        ('etajdestinatar', ''),
        ('apdestinatar', ''),
        ('oras_dest', 'Bistrita'),
        ('orasel', 'Agrisu de Jos'),
        ('plic', '0'),
        ('colet', '1'),
        ('kg', '1.00'),
        ('continut', ''),
        ('plata_la', 'expeditor'),
        ('val_decl', ''),
        ('ramburs', '600.75'),
        ('obs', ''),
        ('persexpeditor', 'Alina Mircea'),
        ('persdest', 'asdasd asdasda'),
        ('depnr', '18-Bistrita'),
        ('kmextdest', '40'),
        ('data_awb', '17.11.2020'),
        ('ora_awb', '07:34:21'),
        ('ridicat', 'NU'),
        ('centru_cost', ''),
        ('status', 'Nepreluat'),
        ('data_confirmarii', ''),
        ('ora_confirmarii', ''),
        ('nume_confirmare', ''),
        ('client_exp', 'FAN COURIER - cont test'),
        ('restituire', ''),
        ('tip_serviciu', 'Cont Colector'),
        ('banca', 'RAIFFEISEN BANK ROMANA'),
        ('iban', 'RO53RZBR0000060009520959'),
        ('awb_retur', '')
    ]),
    OrderedDict([
        ('nr_crt', '2'),
        ('awb', '2322000120007'),
        ...
    ]),
    ...
]
```

## Export sheet in HTML

```python
client.sheets.export()
```
```python
b'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//E...
```

## Get transfers

```python
client.transfers.get(data='18.11.2020')
```
```python
[
    {
        'oras_destinatar': ...,
        'data_awb': ...,
        'suma_incasata': ...,
        'numar_awb': ...,
        'expeditor': ...,
        'destinatar': ...,
        'continut': ...,
        'persoanad': ...,
        'data_virament': ...,
        'persoanae': ...,
        'ramburs_la_awb': ...,
        'awb_retur': ...,
        'incasare_card': ...
    },
    ...
]
```

## Get orders

```python
client.orders.get(data='17.11.2020')
```
```python
[
    OrderedDict([
        ('nr_crt', '1'),
        ('data_ridicare_comanda', '17.11.2020'),
        ('ora_de_la', '12:30'),
        ('ora_pana_la', '16:45'),
        ('persoana_contact', 'DORU'),
        ('telefon', '0787787639'),
        ('email', 'it@fancourier.ro'),
        ('colete', '3'),
        ('plicuri', '0'),
        ('greutate', '45.00'),
        ('inaltime', '10.00'),
        ('latime', '10.00'),
        ('lungime', '10.00'),
        ('observatii', 'RIDICARE JIULUI NR 2'),
        ('strada', ''),
        ('nr', ''),
        ('bloc', ''),
        ('scara', ''),
        ('etaj', ''),
        ('ap', ''),
        ('localitate', ''),
        ('judet', ''),
        ('numar_comanda', ''),
        ('status', 'In asteptare')
    ])
]
```

## Create order

```python
request_data = {
    'pers_contact': 'pers_contact',
    'tel': 'tel',
    'email': 'email@mail.com',
    'greutate': 10,
    'inaltime': 1,
    'lungime': 1,
    'latime': 1,
    'ora_ridicare': '17:00'
}
client.orders.create(**request_data)
```
```python
'Inregistrarea comenzii este finalizata cu SUCCES. In intervalul specificat, FAN Courier va ridica expeditia din locatia indicata. Va multumim!'
```
