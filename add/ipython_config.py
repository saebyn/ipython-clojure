c = get_config()

# Disable authentication.
c.Session.key = b''
c.Session.keyfile = b''
