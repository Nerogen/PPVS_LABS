from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window

Window.size = 890, 500
Window.clearcolor = 1, 0, 0, 1


class Container(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_base = []

    label_widget = ObjectProperty()
    initials = ObjectProperty()
    account = ObjectProperty()
    address = ObjectProperty()
    mobile_phone = ObjectProperty()
    home_phone = ObjectProperty()

    def update_user_base(self):
        """Get all info from fields and update two - dimensional list, update label info"""
        box = [self.initials.text[:], self.account.text[:], self.address.text[:], self.mobile_phone.text[:],
               self.home_phone.text[:]]
        self.user_base.append(box)
        self.clear_fields()
        self.label_widget.text = 'Successful!'

    def search_user_info(self):
        """Search info from box with all fields, return place of user in data base"""
        box = [self.initials.text[:], self.account.text[:], self.address.text[:], self.mobile_phone.text[:],
               self.home_phone.text[:]]
        for i in range(len(self.user_base)):
            for j in box:
                if j in self.user_base[i]:
                    self.label_widget.text = f'Name: {self.user_base[i][0]}\n' \
                                             f'Account number: {self.user_base[i][1]}\n' \
                                             f'Address: {self.user_base[i][2]}\n' \
                                             f'Mobile phone: {self.user_base[i][3]}\n' \
                                             f'Home phone: {self.user_base[i][4]}'
                    self.clear_fields()
                    return i
        else:
            self.label_widget.text = 'User not found!'

    def delete_user_info(self):
        """Use function for get place of user and then delete from data base"""
        place = self.search_user_info()
        if place is None:
            self.label_widget.text = 'User not found!'
        else:
            del self.user_base[place]
            self.label_widget.text = 'User successful deleted!'

    def view_all_info(self):
        box = []
        for i in self.user_base:
            box.append(f'Name: {i[0]} | Account number: {i[1]}')
        self.label_widget.text = '\n'.join(box)

    def clear_fields(self):
        """Clear all fields for updating info"""
        self.initials.text = ''
        self.account.text = ''
        self.address.text = ''
        self.mobile_phone.text = ''
        self.home_phone.text = ''

    def clear_search_info(self):
        """Clear label"""
        self.label_widget.text = ''


class ClientBaseApp(App):
    def build(self):
        return Container()


if __name__ == '__main__':
    ClientBaseApp().run()
