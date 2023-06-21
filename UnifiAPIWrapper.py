import requests
import json
import urllib3

# session = Session(ipadress, port, username, password, device_type)
class Session:
    def __init__(self, ipadress, port, username, password, device_type, site=None):
        urllib3.disable_warnings()
        self.authenticated = False
        self.ipadress = ipadress
        self.port = port
        self.username = username
        self.password = password
        if site is not None:
            self.site = site
            pass
        else:
            self.site = "default"
            pass
        if device_type == "udmp":
            self.baseURL = "https://" + str(self.ipadress) + ":" + str(self.port) + "/proxy/network"
            self.loginURL = "https://" + str(self.ipadress) + ":" + str(self.port) + "/api/auth/login"
            pass
        elif device_type == "other":
            self.baseURL = "https://" + str(self.ipadress) + ":" + str(self.port)
            self.loginURL = "https://" + str(self.ipadress) + ":" + str(self.port) + "/api/login"
            pass
        else:
            raise RuntimeError("No valid model")
        
        self.site_prefix = "/api/s/" + site
        self.baseURL = self.baseURL + self.site_prefix

        self.login_data = {
            "username": self.username,
            "password": self.password
        }

    def _getData(self, response):
        data_full = response.json()
        data = data_full["data"]
        return data
    
    def _make_request(self, method, endpoint):
        url = self.baseURL + endpoint
        response = self.session.request(method, url)
        if response.status_code == 200:
            return self._getData(response)
        else:
            error_message = f"Error occurred: {response.status_code} - {response.text}"
            print(error_message)
            raise RuntimeError(error_message)

    # session.Authenticate()
    # if self.authenticated:
    #      print("authenticated")
    def Authenticate(self):
        self.session = requests.session()
        self.session.verify = False
        response = self.session.post(self.loginURL, data=self.login_data)
        if response.status_code == 200:
            print("Authentication succesfull")
            self.authenticated = True
            csrf_token = response.headers.get('X-CSRF-Token')
            self.session.headers['X-CSRF-Token'] = csrf_token
            return
        else:
            raise RuntimeError("Authentication failed")

    # Destroys server side session
    # session.Logout()    
    def Logout(self):
        decorator = "/api/logout"
        logOutURL = self.baseURL + decorator 
        r = self.session.post(logOutURL)

        if r.status_code == 200:
            print("Logged out successfully")
            self.authenticated = False
        else:
            RuntimeWarning("Couldnt log out")
            pass

    # Returns list of dictonaries
    # health = session.Health()
    # print(health)

    def Health(self):
        endpoint = "/stat/health"
        return self._make_request("POST", endpoint)

    def Wlanconf(self):
        endpoint = "/rest/wlanconf"
        return self._make_request("GET", endpoint)

    def Sysinfo(self):
        endpoint = "/stat/sysinfo"
        return self._make_request("GET", endpoint)

    def Events(self):
        endpoint = "/stat/event"
        return self._make_request("GET", endpoint)
    
    def Networkconf(self):
        endpoint = "/rest/networkconf"
        return self._make_request("GET", endpoint)
    
    def Settings(self):
        endpoint = "/rest/setting"
        return self._make_request("GET", endpoint)
    
    def Firewallgroup(self):
        endpoint = "/rest/firewallgroup"
        return self._make_request("GET", endpoint)