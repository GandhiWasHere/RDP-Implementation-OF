
class os_classifier():
    def __init__(self):
        self.conf = {
            4:
                {8:
                     ["windows 7/ windows 2012/ windows 2012R2 / Windows 2008R2/ Windows2008"]},
            7:
                {8:
                     ["Windows2016"]},
            10:
                {8:
                     ["windows10"]}
        }

    def classifed_by_version(self, major, minor):
        return None




