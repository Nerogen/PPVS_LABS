import xml.sax


class Reader(xml.sax.ContentHandler):
    def __init__(self):
        super().__init__()
        self.data_table = []
        self.client_data = []
        self.parser = xml.sax.make_parser()

    def startElement(self, name, attrs):
        self.current = name
        if name == "client":
            pass

    def characters(self, content):
        if self.current == "name":
            self.name = content
        elif self.current == "account_number":
            self.account_number = content
        elif self.current == "address":
            self.address = content
        elif self.current == "mobile_phone":
            self.mobile_phone = content
        elif self.current == "home_phone":
            self.home_phone = content

    def endElement(self, name):
        if self.current == "name":
            self.client_data.append(self.name)
        elif self.current == "account_number":
            self.client_data.append(self.account_number)
        elif self.current == "address":
            self.client_data.append(self.address)
        elif self.current == "mobile_phone":
            self.client_data.append(self.mobile_phone)
        elif self.current == "home_phone":
            self.client_data.append(self.home_phone)

        if len(self.client_data) == 5:
            self.data_table.append(tuple(self.client_data))
            self.client_data = []

        self.current = ""
