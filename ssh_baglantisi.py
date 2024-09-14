import paramiko

hostname = 'ip_adresi'
port = 22
username = 'kullanici_adi'
password = 'sifre'

def ssh_baglantisi(hostname, port, username, password):
    try:
        sshclient = paramiko.SSHClient()
        sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        sshclient.connect(hostname=hostname, port=port, username=username, password=password)
        print("Bağlantı kuruldu")
        sshclient.close()

    except paramiko.AuthenticationException:
        print("Bağlantı kurulamadı: Bilgiler hatalı")
    except paramiko.SSHException as sshException:
        print(f"Bağlantı kurulamadı: SSH Hatası {sshException}")
    except Exception as e:
        print(f"Bağlantı kurulamadı: {e}")

ssh_baglantisi(hostname, port, username, password)


