from Lab2.View.view import View
from Lab2.Parsers.write import Writer
from Lab2.Parsers.read import Reader


class Model(View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_base = []
        self.logger = []

    def build(self):
        return self.screen

    def upload(self):
        handler = Reader()
        handler.parser.setContentHandler(handler)
        handler.parser.parse(f"D:/PPVS_LABS/Lab2/Parsers/examples/input.xml")

        for data in handler.data_table:
            self.user_base.append(list(data))

        self.logger.append('Upload base!')
        self.update_view_menu()

    def save(self):
        dom = Writer(f"D:/PPVS_LABS/Lab2/Parsers/examples/output.xml")
        data_dict = {}
        for row in self.user_base:
            data_dict["name"] = row[0]
            data_dict["account_number"] = row[1]
            data_dict["address"] = row[2]
            data_dict["mobile_phone"] = row[3]
            data_dict["home_phone"] = row[4]

            dom.create_xml_client(data_dict)
        dom.create_xml_file()
        self.logger.append('Save base!')
        self.update_view_menu()

    def color_theme(self):
        self.theme()

    def update_user_base(self):
        """Get all info from fields and update two - dimensional list, update label info"""
        box = [
            self.screen.ids.name.text[:],
            self.screen.ids.account_number.text[:],
            self.screen.ids.address.text[:],
            self.screen.ids.mobile_phone.text[:],
            self.screen.ids.home_phone.text[:]
        ]

        self.user_base.append(box)
        self.logger.append(f'Add user {box[0]} successful!')
        self.update_view_menu()

    def search_user_info(self, search=True):
        """Search info from box with all fields, return place of user in data base"""

        indexes = []
        if search:
            box = [
                self.screen.ids.name_for_search.text[:],
                self.screen.ids.account_number_for_search.text[:],
                self.screen.ids.address_for_search.text[:],
                self.screen.ids.mobile_phone_for_search.text[:],
                self.screen.ids.home_phone_for_search.text[:]
            ]

        else:
            box = [
                self.screen.ids.name_for_delete.text[:],
                self.screen.ids.account_number_for_delete.text[:],
                self.screen.ids.address_for_delete.text[:],
                self.screen.ids.mobile_phone_for_delete.text[:],
                self.screen.ids.home_phone_for_delete.text[:]
            ]

        for i in range(len(self.user_base)):
            for j in box:
                if j in self.user_base[i]:
                    indexes.append(i)

        if indexes is None:
            self.logger.append(f'User {box[0]} not found!')
        else:
            self.logger.append(f'Number of user with this info: {len(indexes)}!')
            for i in indexes:
                self.logger.append(
                    f'Name: {self.user_base[i][0]} Account number: {self.user_base[i][1]} '
                    f'Address: {self.user_base[i][2]} Mobile phone: {self.user_base[i][3]} '
                    f'Home phone: {self.user_base[i][4]}')

                self.update_view_menu()

        return indexes

    def delete_user_info(self):
        """Use function for get place of user and then delete from data base"""
        place = self.search_user_info(False)
        if place is None:
            self.update_view_menu()
        else:
            count = 0
            for i in place:
                del self.user_base[i - count]
                count += 1
            self.logger.append(f'Number of deleted users: {len(place)}!')
            self.update_view_menu()
