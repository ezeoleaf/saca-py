import config

class Row:
    def setData(self, data):
        columns = config.columns[0]

        self.type = data[columns['TIPO']]
        date = data[columns['FECHA']]
        splitedDate = date.split('/')
        self.day = splitedDate[0]
        if self.type == config.types['RETENCIONES']:
            self.number = data[columns['SUCURSAL']]
        else:
            sucursal = data[columns['SUCURSAL']]
            self.character = sucursal[0:3]
            self.number = sucursal[2:]
        self.norm = data[columns['NORMA']]
        self.cuit = data[columns['CUIT']]
        self.net = data[columns['NETO']]
        self.amount = data[columns['IMPORTE']]
        self.aliquot = data[columns['ALICUOTA']]

