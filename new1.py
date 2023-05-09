from netmiko import ConnectHandler
from jinja2 import Template
import os
print(os.getcwd())
os.chdir('C:\GNS3\Python\python_out')
print(os.getcwd())


template = ('new_test.j2')

cisco_router_1={
    'device_type':'cisco_ios',
    'host':'172.16.138.161',
    'username':'cisco',
    'password':'cisco',
    'secret':'cisco',
    'port':22
}

rendering_temp={
    'fast':'fast',
    'iface_name':'0/1',
    'ip_addr':'10.10.10.1. 255.255.255.0',
    'AS':'100',
    'neighbour_ip':'10.10.10.2',
    'neighbour_as':'200',
    'network_ip':'10.10.10.0',
    'subnet':'255.255.255.0'
}
ssh=ConnectHandler(**cisco_router_1)
ssh.enable()
with open(template) as temp:
    temp_out_1=Template(temp.read(),keep_trailing_newline=True)
temp_2 = temp_out_1.render(rendering_temp)
out = temp_2.split('\n')
print(out)
file=open('new_172.txt','w')
out_to=ssh.send_config_set(out)
file.write(out_to)


