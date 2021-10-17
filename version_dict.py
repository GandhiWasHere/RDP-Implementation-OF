class os_classifier():
    def __init__(self):
        self.conf_rdp = {
            4:
                {8:
                     ["windows7", "windows2008", "windows2008R2", "windows2012", "windows2012R2"]},
            7:
                {8:
                     ["windows2016"]},
            10:
                {8:
                     ["windows10"]}
        }

        self.conf_ntlm = {
            6:
                {2:
                    {
                        9200: ["windows2012"]
                    },
                    3: {
                        9600: ["windows2012R2"]
                    }
                },
            10:
                {
                    0: {
                        14393: ["windows2016"],
                        17763: ["windows2019"],
                        19041: ["windows10"]
                    }

                }
        }

        self.window_size = {
            8192: ["windows7"],
            64000: ["windows2012", "windows2012R2", "windows2016", "windows2008R2", "windows2019","windows10"],
            64240: ["windows2012", "windows2012R2", "windows2016", "windows2008R2", "windows2019"]
        }
        self.all_os = ["windows7", "windows10", "windows2012", "windows2012R2", "windows2016", "windows2008R2",
                       "windows2019"]

    def classifed_by_version(self, rdp_version, ntlm_version, window_size):
        if window_size:
            list1 = self.window_size[window_size]
        else:
            list1 = self.all_os
        if ntlm_version:
            if ntlm_version[0] in self.conf_ntlm.keys():
                list2 = self.conf_ntlm[ntlm_version[0]][ntlm_version[1]][ntlm_version[2]]
            else:
                list2 = self.all_os
        else:
            list2 = self.all_os
        if rdp_version:
            list3 = self.conf_rdp[rdp_version[0]][rdp_version[1]]
        else:
            list3 = self.all_os
        return set(list1) & (set(list2)) & set(list3)
