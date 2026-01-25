import netmiko

from netmiko import ConnectHandler

# Device information   
device_info = {
    'device_type' : 'cisco_ios_telnet',
    'host': '10.82.1.2',
    'username': 'admin',
    'password': 'pass',
    'secret': 'pass',
    'port': 23
}

# Config
device_config = [
    'int loopback 1',
    'ip add 1.1.1.1 255.255.255.255',
    'end'
]

# Connecting to device
access_cli = ConnectHandler(**device_info)
access_cli.enable()
output = access_cli.send_config_set(device_config)
siib = access_cli.send_command('sh ip int br')
access_cli.disconnect()

print(output)
print(siib)

