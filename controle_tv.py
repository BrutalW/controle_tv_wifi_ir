import os
import requests

# Funções para Controle IR
def ligar_tv_ir(tv):
    os.system(f"irsend SEND_ONCE {tv}_power")

def desligar_tv_ir(tv):
    os.system(f"irsend SEND_ONCE {tv}_power_off")

def aumentar_volume_ir(tv):
    os.system(f"irsend SEND_ONCE {tv}_volume_up")

def diminuir_volume_ir(tv):
    os.system(f"irsend SEND_ONCE {tv}_volume_down")

def mudar_canal_ir(tv, canal):
    os.system(f"irsend SEND_ONCE {tv}_channel_{canal}")

def mute_ir(tv):
    os.system(f"irsend SEND_ONCE {tv}_mute")


# Funções para Controle de TV via Wi-Fi

# Funções para Samsung TV via Wi-Fi (SmartThings API)
def ligar_tv_samsung(ip, token):
    url = f"https://api.smartthings.com/v1/devices/{ip}/commands"
    payload = {
        "commands": [{
            "component": "main",
            "capability": "switch",
            "command": "on"
        }]
    }
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print("Samsung TV ligada com sucesso!")
    else:
        print(f"Erro ao ligar TV: {response.status_code}")

def desligar_tv_samsung(ip, token):
    url = f"https://api.smartthings.com/v1/devices/{ip}/commands"
    payload = {
        "commands": [{
            "component": "main",
            "capability": "switch",
            "command": "off"
        }]
    }
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print("Samsung TV desligada com sucesso!")
    else:
        print(f"Erro ao desligar TV: {response.status_code}")


# Funções para LG TV via Wi-Fi (WebOS API)
def ligar_tv_lg(ip):
    url = f"http://{ip}:3000/ir/rc"
    payload = {
        "type": "ir",
        "data": {
            "function": "power_on"
        }
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("LG TV ligada com sucesso!")
    else:
        print(f"Erro ao ligar TV: {response.status_code}")

def desligar_tv_lg(ip):
    url = f"http://{ip}:3000/ir/rc"
    payload = {
        "type": "ir",
        "data": {
            "function": "power_off"
        }
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("LG TV desligada com sucesso!")
    else:
        print(f"Erro ao desligar TV: {response.status_code}")


# Funções para Sony TV via Wi-Fi (Bravia API)
def ligar_tv_sony(ip, token):
    url = f"http://{ip}/sony/system"
    payload = {
        "method": "setPowerStatus",
        "params": ["on"],
        "id": 1,
        "version": "1.0"
    }
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print("Sony TV ligada com sucesso!")
    else:
        print(f"Erro ao ligar TV: {response.status_code}")

def desligar_tv_sony(ip, token):
    url = f"http://{ip}/sony/system"
    payload = {
        "method": "setPowerStatus",
        "params": ["off"],
        "id": 1,
        "version": "1.0"
    }
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print("Sony TV desligada com sucesso!")
    else:
        print(f"Erro ao desligar TV: {response.status_code}")
