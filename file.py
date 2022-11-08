# import paramiko
# from scp import SCPClient

ip=['10.76.6', '10.76.6','10.76.6',]
servers = len(ip) - 1
# print(servers)
port=22
username='user'
password='pass'
idx = 0

# def createSSHClient(server, port, user, password):
#     client = paramiko.SSHClient()
#     client.load_system_host_keys()
#     client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     client.connect(server, port, user, password)
#     return client

# ssh = createSSHClient(server, port, user, password)
# scp = SCPClient(ssh.get_transport())


from paramiko import SSHClient
from scp import SCPClient

ssh = SSHClient()
ssh.load_system_host_keys()
ssh.connect(ip[idx],port,username,password)

# SCPCLient takes a paramiko transport as an argument
scp = SCPClient(ssh.get_transport())

# scp.put('mm.txt', 'test2.txt')
scp.get('server.server.py'.py')

# Uploading the 'test' directory with its content in the
# '/home/user/dump' remote directory
# scp.put('tt.txt', recursive=True, remote_path='C:\dev\model_archive\reports')

scp.close()