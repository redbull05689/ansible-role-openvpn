import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_openvpn_is_installed(host):
    openvpn = host.package("openvpn")
    assert openvpn.is_installed
