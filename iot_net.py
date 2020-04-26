import paramiko
from sshtunnel import SSHTunnelForwarder
import logging
from scp import SCPClient


client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.20.201', 22, username='root', password='123456')
a,b,c = client.exec_command('git clone http://gitlab.wh.zjrealtech.com/dev/idi/tree/idi_new/idi_iot_daemon')
print(b.read())
client.close()

# with SSHTunnelForwarder(
#     ('192.168.20.201', 22),
#     ssh_username="root",
#     ssh_password='123456',
#     remote_bind_address=('192.168.32.222', 22),
#     local_bind_address=('0.0.0.0', 18882),
# ) as tunnel:
#     client = paramiko.SSHClient()
#     client.load_system_host_keys()
#     client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     client.connect('127.0.0.1', 18882, username='root', password='123456')
#     a,b,c = client.exec_command('git --help')
#     print(b.read())
#     client.close()


class CustomClient:
    ssh_client = None
    scp_client = None
    ssh_springboard_client = None

    def __init__(self, target_ip, target_port, target_username, target_password,
                 springboard_ip='192.168.20.201', springboard_port=22,springboard_username='root',
                 springboard_password='123456'
                 ):
        self.target_ip = target_ip
        self.target_port = target_port
        self.target_username = target_username
        self.target_password = target_password
        self.springboard_ip = springboard_ip
        self.springboard_port = springboard_port
        self.springboard_username = springboard_username
        self.springboard_password = springboard_password

    def get_ssh_client(self):
        """与目标机器建立ssh连接"""
        if CustomClient.ssh_client is None:
            with SSHTunnelForwarder(
                (self.springboard_ip, self.springboard_port),
                ssh_username=self.springboard_username,
                ssh_password=self.springboard_password,
                remote_bind_address=(self.target_ip, self.target_port),
                local_bind_address=('0.0.0.0', 18882),
            ) as tunnel:
                client = paramiko.SSHClient()
                client.load_system_host_keys()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect('127.0.0.1', 18882, username=self.target_username, password=self.target_port)
                CustomClient.ssh_client = client
                return CustomClient.ssh_client
        else:
            return CustomClient.ssh_client

    def get_springboard_client(self):
        """
        得到跳板机连接，进行git上传
        :return:
        """
        if CustomClient.ssh_springboard_client is None:
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(self.springboard_ip, self.springboard_port, username=self.springboard_username, password=self.springboard_password)
            CustomClient.ssh_springboard_client = client
            return CustomClient.ssh_springboard_client
        else:
            return CustomClient.ssh_springboard_client

    def get_scp_client(self):
        """建立scp连接"""
        if CustomClient.scp_client is None:
            ssh_client = self.get_ssh_client()
            scp = SCPClient(ssh_client.get_transport(), socket_timeout=5.0)
            CustomClient.scp_client = scp
            return CustomClient.scp_client
        else:
            return CustomClient.scp_client



# 跳板机传送
# with SSHTunnelForwarder(
#     ('192.168.20.201', 22),
#     ssh_username="root",
#     ssh_password='123456',
#     remote_bind_address=('192.168.32.222', 22),
#     local_bind_address=('0.0.0.0', 18882),
# ) as tunnel:
#     client = paramiko.SSHClient()
#     client.load_system_host_keys()
#     client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     client.connect('127.0.0.1', 18882, username='root', password='123456')
#     scp = SCPClient(client.get_transport(), socket_timeout=5.0)
#     scp.put('abc.txt', '/home/root')
#     # do some operations with client session
#     client.close()
#
# print('FINISH!')