import paramiko
from sshtunnel import SSHTunnelForwarder
import os
from scp import SCPClient

# a = os.path.dirname(os.path.abspath(__file__))
# print(os.path.exists(os.path.join(a, 'idi')))
# a = os.system('git clone http://192.168.20.12/dev/idi/tree/idi_new/idi_iot_daemon')
# print(a)
# client = paramiko.SSHClient()
# client.load_system_host_keys()
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# client.connect('192.168.20.201', 22, username='root', password='123456')
# a,b,c = client.exec_command('git clone http://gitlab.wh.zjrealtech.com/dev/idi/tree/idi_new/idi_iot_daemon')
# print(b.read())
# client.close()

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
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
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

    def get_package_path(self, package_name):
        base_path = os.path.join(CustomClient.BASE_DIR, 'idi')
        if os.path.exists(base_path):
            return os.path.join(base_path, package_name)
        else:
            res = os.system('git clone -b idi_new http://wanyi:111111@gitlab.wh.zjrealtech.com/dev/idi.git')
            if res == 0:
                return os.path.join(base_path, package_name)
            else:
                pass

    def upload_package_target(self, package_name):
        with SSHTunnelForwarder(
                ('192.168.20.201', 22),
                ssh_username="root",
                ssh_password='123456',
                remote_bind_address=('192.168.32.222', 22),
                local_bind_address=('0.0.0.0', 18882),
        ) as tunnel:
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect('127.0.0.1', 18882, username='root', password='123456')
            scp = SCPClient(client.get_transport(), socket_timeout=5.0)
            scp.put(self.get_package_path(package_name), '/home/root/idi', recursive=True)
            print('FINISH!')

#
if __name__ == '__main__':
    a = CustomClient('192.168.32.222', 22, 'root', '123456')
    a.upload_package_target('idi_iot_daemon')
# base_path = os.path.join(CustomClient.BASE_DIR, 'idi')
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
#     print(os.path.join(base_path,'idi_iot_daemon'))
#     scp.put(os.path.join(base_path,'idi_iot_daemon'), '/home/root/idi', recursive=True)
#     # do some operations with client session
#     client.close()
#
# print('FINISH!')