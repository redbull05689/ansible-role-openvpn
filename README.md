openvpn
=======

[![Build Status](https://travis-ci.org/sedovandrew/ansible-role-openvpn.svg?branch=master)](https://travis-ci.org/sedovandrew/ansible-role-openvpn)

Config openVPN network.

Requirements
------------

- pyOpenSSL

Role Variables
--------------

- `openvpn_role: client` - this parameter can have only two values: server or client
- `openvpn_server_ip: XXX.XXX.XXX.XXX` - server ip
- `openvpn_host_cn: first-client` - Common Name
- `openvpn_key_size: 4096` - size of the keys
- `openvpn_network: 10.8.0.0` - VPN subnet
- `openvpn_netmask: 255.255.255.0` - VPN netmask
- `openvpn_local_key_path: keys` - path to the local directory for CA keys.
- `openvpn_port: 1194` - server port to connect
- `openvpn_proto: udp` - TCP or UDP protocol
- `openvpn_dev: tun` - tun (routed IP tunnel) or tap (ethernet tunnel)
- `openvpn_options: ["keepalive 10 120", "tls-auth ta.key 0"]` - list of additional params

All params you can see in [defaults/main.yml](https://github.com/sedovandrew/ansible-role-openvpn/blob/master/defaults/main.yml)

Example Playbook
----------------

```yaml
- hosts: server
  roles:
  - role: sedovandrew.openvpn
    openvpn_role: server
    openvpn_host_cn: server
    openvpn_options:
    - "keepalive 10 120"

- hosts: client1
  roles:
  - role: sedovandrew.openvpn
    openvpn_role: client
    openvpn_host_cn: client1
    openvpn_server_ip: XXX.XXX.XXX.XXX
```

Testing
-------

Install [Molecule](https://molecule.readthedocs.io/en/latest/installation.html) and [Testinfra](https://testinfra.readthedocs.io/en/latest/#quick-start) for local testing role.

Install pyOpenSSL:

```bash
pip install pyOpenSSL
```

Run test:

```bash
molecule test
```

License
-------

BSD

Author Information
------------------

Andrey Sedov - sedoy80@gmail.com
