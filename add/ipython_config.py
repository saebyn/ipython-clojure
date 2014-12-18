c = get_config()
c.KernelManager.kernel_cmd = ["/d/git/ipython-clojure/bin/ipython-clojure","{connection_file}"]

# Disable authentication.
c.Session.key = b''
c.Session.keyfile = b''
