import Base
from datetime import datetime
import requests

class DerivID (Base.BaseClient):
    params = None
    def __init__(self, u, m):
        self.BASE_URL = u
        self.method = m

    def generate_url(self, method):
        return '{0}/{1}'.format(self.BASE_URL, method)

    def _get_data(self, method, http_method):
        response = requests.get(self.generate_url(self.method), self.params)
        return self.response_handler(response)

    def find_id(self,ss):

        id = ''
        for i in range(len(ss)):
            if (ss[i] == 'u' and ss[i + 1] == 'i' and ss[i + 2] == 'd'):
                for j in range(len(ss)):
                    if ss[i + j + 5] == ',':
                        break
                    id = id + ss[i + j + 5]
                break
        return id



class DerivFriends(Base.BaseClient):
    params = None

    def __init__(self, u, m):
        self.BASE_URL = u
        self.method = m

    def generate_url(self, method):
        return '{0}/{1}'.format(self.BASE_URL, method)

    def _get_data(self, method, http_method):
        response = requests.get(self.generate_url(self.method), self.params)

        return self.response_handler(response)

    def build_gist(self, ss):
        a = ss.json()
        dict_age = {0: 0}

        for bdate in a.get("response"):
            date_str = str(bdate.get("bdate"))
            if (not (bdate.get("bdate")) == None) and (len(date_str) > 7):
                dt = datetime.strptime(date_str, "%d.%m.%Y")
                delta_date = str(datetime.now() - dt)
                i = int(delta_date.split()[0])
                val = i // 365
                if dict_age.get(val) == None:
                    dict_age[val] = '#'
                else:
                    dict_age[val] = str(dict_age.get(val)) + '#'
            else:
                dict_age[0] = int(dict_age.get(0)) + 1
        self.print_gist(dict_age)

    def print_gist(self, dict_age):
        print()
        sum = 0
        for key in sorted(dict_age):
            if key == 0:
                sum += int(dict_age[0])
                print("Не указан возраст: ", dict_age[0])
            else:
                sum += int(len(str((dict_age[key]))))
                print("%3d %s" % (key, dict_age[key]))
        print("Друзья: ", sum)