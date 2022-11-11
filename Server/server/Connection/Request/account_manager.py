from server.password_encoder import passwEncode

class AccountManager:
    def __init__(self, password):
        self.password = password

        self.newEmail = None
        self.newUsername = None
        self.newPassword = None
        self.newPicture = None

        self.deleteAccount = False


    def change_email(self, newEmail):
        self.newEmail = newEmail

    def change_username(self, username):
        self.newUsername = username

    def change_password(self, newPassword):
        self.newPassword = passwEncode(newPassword)

    def change_picture(self, picture):
        self.newPicture = picture

    def delete_account(self):
        self.deleteAccount = True
    