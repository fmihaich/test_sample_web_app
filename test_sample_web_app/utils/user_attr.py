class UserAttr(object):
    USERNAME = 'username'
    NAME = 'name'
    SURNAME = 'surname'
    EMAIL = 'email'
    BIRTHDAY = 'birthday'
    ADDRESS = 'address'

    def get_all(self):
        return [self.USERNAME, self.NAME, self.SURNAME, self.EMAIL, self.BIRTHDAY, self.ADDRESS]
