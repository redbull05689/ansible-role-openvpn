import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('server1')


def test_openvpn_service(host):
    openvpn = host.service('openvpn-server@server1')
    assert openvpn.is_running
    assert openvpn.is_enabled


def test_openvpn_config_file(host):
    config_file = host.file('/etc/openvpn/server/server1.conf')
    assert config_file.exists


def test_openvpn_key_file(host):
    key_file = host.file('/etc/openvpn/server/server1.key')
    assert key_file.exists
    assert key_file.mode == 0o600
    assert key_file.uid == 0


def test_openvpn_cert_file(host):
    cert_file = host.file('/etc/openvpn/server/server1.crt')
    assert cert_file.exists
    assert cert_file.uid == 0


def test_openvpn_ca_cert_file(host):
    ca_cert_file = host.file('/etc/openvpn/server/ca.crt')
    assert ca_cert_file.exists
    assert ca_cert_file.uid == 0


def test_openvpn_port_listening(host):
    assert host.socket("udp://0.0.0.0:1194").is_listening
