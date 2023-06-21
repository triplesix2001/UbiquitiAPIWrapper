
# Small library for the UniFi API

## PIP Installation

    pip install UnifiAPIWrapper

## Recommendations

I recommend just downloading the .py file and importing it that way.
Module requires requests.
Do NOT use backups features as this does not work properly.

## Usage

To first initate a session define a session object like this.
    session = Session(ipadress="192.168.1.1",
        port="443",
        username="username",
        password="Password",
        device_type="udmp",
        site="default")

    Site is "default" if not specified
    Device type can be "udmp" or "other", this is needed for URL prefix
    User has to be local superuser, not online account.

Then you have to authenticate, this will automaticly set the CSRF Token
to make it easier for custom requests.
    session.Authenticate()

When doing requests this will format the response to only contain the actual data. Warning: SSL and TLS is disabled.

## Examples

    session.Authenticate()

    health = session.Health()
    print(health)

    wlanconf = session.Wlanconf()
    print(wlanconf)

    sysinfo = session.Sysinfo()
    print(sysinfo)

    events = session.Events()
    print(events)

    networkconf = session.Networkconf()
    print(networkconf)

    settings = session.Settings()
    print(settings)

    firewallgroup = session.Firewallgroup()
    print(firewallgroup)

## Refrences / Sources

<https://ubntwiki.com/products/software/unifi-controller/api>

## Other projects to check out

PHP Client
<https://github.com/Art-of-WiFi/UniFi-API-client>