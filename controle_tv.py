import os
import subprocess
import requests
import time

# Função para verificar se um dispositivo está respondendo ao ping
def ping_ip(ip):
    try:
        output = subprocess.check_output(['ping', '-c', '1', ip], stderr=subprocess.STDOUT, universal_newlines=True)
        if "1 packets transmitted, 1 received" in output:
            return True
        else:
            return False
    except subprocess.CalledProcessError:
        return False

# Função para escanear a rede e descobrir dispositivos conectados
def descobrir_tv_ip():
    # Substitua pelo intervalo de IPs da sua rede local (por exemplo, 192.168.1.0/24)
    ips_para_tentar = [f"192.168.1.{i}" for i in range(1, 255)]
    ips_encontrados = []

    for ip in ips_para_tentar:
        if ping_ip(ip):
            print(f"Dispositivo encontrado: {ip}")
            # Adicionando um simples filtro para detectar dispositivos específicos
            # (Aqui você pode adicionar mais condições conforme necessário)
            if "Samsung" in ip or "LG" in ip:
                ips_encontrados.append(ip)

    return ips_encontrados

# Função para controlar TV via Wi-Fi (Simulação)
def controlar_tv_wifi(ip):
    try:
        print(f"Controlando TV via Wi-Fi no IP: {ip}")
        # Exemplo de código para enviar um comando via API (aqui é só uma simulação)
        response = requests.post(f"http://{ip}/api/command", data={"command": "volume_up"})
        if response.status_code == 200:
            print(f"Comando enviado para a TV em {ip}")
        else:
            print(f"Erro ao enviar comando para a TV em {ip}")
    except requests.exceptions.RequestException as e:
        print(f"Erro na comunicação com a TV: {e}")

# Função para controlar TV via IR (Simulação)
def controlar_tv_ir():
    print("Controlando TV via IR...")
    # Implementação para controle IR via hardware no Termux
    # Usaria uma biblioteca como a LIRC, mas em Termux sem root é complicado
    # Você precisaria de um adaptador IR USB compatível para isso funcionar
    print("Comando IR enviado")

# Função principal para encontrar e controlar TVs
def controlar_tvs():
    print("Buscando TVs na rede...")
    tv_ips = descobrir_tv_ip()

    if not tv_ips:
        print("Nenhuma TV encontrada na rede.")
        return

    for ip in tv_ips:
        print(f"Controlando a TV com IP {ip}...")
        
        # Exemplo de controle via Wi-Fi
        controlar_tv_wifi(ip)
        
        # Exemplo de controle via IR (mesmo sem identificar o IP)
        controlar_tv_ir()
        
        time.sleep(1)  # Pausa entre os comandos

# Executando o script
if __name__ == "__main__":
    controlar_tvs()
