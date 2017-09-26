class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self):
        return "{} {}".format(self.firstname, self.lastname)

    def initials(self):
        return "{}. {}.".format(self.firstname[0], self.lastname[0])