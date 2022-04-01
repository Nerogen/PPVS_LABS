import xml.dom.minidom as minidom


class Writer:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.dom_tree = minidom.Document()
        self.rows = []

    def create_xml_client(self, data: tuple):
        client = self.dom_tree.createElement("client")

        for value in data:
            temp_child = self.dom_tree.createElement(value)
            client.appendChild(temp_child)

            node_text = self.dom_tree.createTextNode(data[value].strip())
            temp_child.appendChild(node_text)

        self.rows.append(client)

    def create_xml_file(self):
        pass_table = self.dom_tree.createElement("pass_table")

        for client in self.rows:
            pass_table.appendChild(client)

        self.dom_tree.appendChild(pass_table)

        self.dom_tree.writexml(open(self.file_name, 'w'),
                               indent="  ",
                               addindent="  ",
                               newl='\n')
        self.dom_tree.unlink()
