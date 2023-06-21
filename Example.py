from UnifiAPIWrapper import Session

session = Session(ipadress="192.168.1.1", 
                  port="443", 
                  username="username", 
                  password="Password", 
                  device_type="udmp",
                  site="default")

session.Authenticate()

#health = session.Health()
#print(health)

#wlanconf = session.Wlanconf()
#print(wlanconf)

#sysinfo = session.Sysinfo()
#print(sysinfo)

#events = session.Events()
#print(events)

#networkconf = session.Networkconf()
#print(networkconf)

#settings = session.Settings()
#print(settings)

firewallgroup = session.Firewallgroup()
print(firewallgroup)

session.Logout()