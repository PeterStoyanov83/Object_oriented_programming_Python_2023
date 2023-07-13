class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail):
        return mail in self.mails

    def __is_domain_valid(self, domain):
        return domain in self.domains

    def validate(self, email):
        username, mail, domain = self.split_email(email)

        if not self.__is_name_valid(username):
            return False

        if not self.__is_mail_valid(mail):
            return False

        if not self.__is_domain_valid(domain):
            return False

        return True

    @staticmethod
    def split_email(email):
        parts = email.split("@")
        if len(parts) == 2:
            return parts[0], parts[1].split(".")[0], parts[1].split(".")[1]
        return "", "", ""
