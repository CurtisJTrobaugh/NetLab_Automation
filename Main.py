from NetworkDevices import NetworkDevices
from SSHConnection import SSHConnection
import time


def config_two_switch(device):
   
    conn_device = SSHConnection(device.hostname, device.username, device.password)

    #conn_device_connect = conn_device.establish_connection()
    #conn_device_connect.send('show version\n')
    #time.sleep(1)
    #output = conn_device_connect.recv(1000)

    conn_device.determine_device_type()
    output = conn_device.send_command('show version')

    print output

device = NetworkDevices(hostname = '10.0.1.2', username = 'cisco', password = 'cisco')



config_two_switch(device)

