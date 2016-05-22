'''
SSH Connection client and methods for parsing
of Cisco prompts and return values
'''

import paramiko
import time
import socket

class SSHConnection(object):
    """
    Defines methods of establishing SSH connection
    """

    def __init__(self, hostname='', username='', password='', connection=''):

        #connection parameters
        self.hostname = hostname
        self.username = username
        self.password = password

        #convert to dictionary
        self.conn_parm = {
            'hostname' : hostname,
            'username' : username,
            'password' : password
            }
        
        #calls function to esatblish connection once the object is instansiated
        #self.connection = self.establish_connection()

    def establish_connection(self):
        """
        Establishes SSH connection and gets into Enable-Mode
        """

        #creates SSH connection and adds SSH key to .known_hosts
        self.ssh_conn = paramiko.SSHClient()
        self.ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            self.ssh_conn.connect(**self.conn_parm)
            print "Connected to %s" % self.conn_parm['hostname']
            #testing:  self.ssh_conn.close()
        except socket.error:
            print "Connection Failed on device %s" % self.conn_parm['hostname']

        #find prompt
        open_session = self.ssh_conn.invoke_shell()
        output = open_session.recv(1000)

        #testing:  print output

        #go into Enable-Mode if not already in it
        if '#' not in output:
            open_session.send('enable\n')
            time.sleep(1)
            open_session.send(self.password)
            open_session.send('\n')
        else:
            print "In Enable-Mode"

        #turn off paging
        open_session.send('terminal length 0\n')
        time.sleep(3)
        
        return open_session

    def determine_device_type(self):

        connection = self.establish_connection()
        connection.send('show version\n')
        output = connection.recv(1000)
        print output

    def send_command(self, command):
        """
        Method for sending commands to the device
        """

        connection = self.establish_connection()
        connection.send(command + '\n')
        print command
        output = connection.recv(1000)
        return output





       
            
  




