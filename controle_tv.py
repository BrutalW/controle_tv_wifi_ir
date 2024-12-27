import time
import os
import sys

# Se for usar IR, instale e configure a biblioteca apropriada, exemplo:
# from gpiozero import LED
# ir = LED(17)  # GPIO que controla o IR
# Exemplo de controle IR (precisa do hardware correspondente)
def controlar_tv_ir():
    print("Enviando sinal IR para a TV...")
    # Enviar código IR para a TV (substitua isso com o código IR correto)
    # ir.on()  # Ligar o sinal IR
    time.sleep(1)
    # ir.off()  # Desligar o sinal IR

# Para controle via Wi-Fi, você precisará de uma rede configurada
def controlar_tv_wifi():
    print("Conectando à TV via Wi-Fi...")
    # Use uma biblioteca como "wifi" ou "requests" para controlar a TV pela rede
    # Exemplo de comando HTTP para controle de TV (modifique conforme necessário)
    import requests
    url = "http://ip_da_tv:porta_comando"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Comando enviado com sucesso!")
        else:
            print("Falha ao enviar o comando.")
    except Exception as e:
        print(f"Erro ao tentar conectar com a TV: {e}")

# Função principal para controle
def main():
    print("Controle de TV - Selecione a opção:")
    print("1 - Controle via IR")
    print("2 - Controle via Wi-Fi")
    escolha = input("Escolha a opção (1/2): ")

    if escolha == '1':
        controlar_tv_ir()
    elif escolha == '2':
        controlar_tv_wifi()
    else:
        print("Opção inválida!")
        sys.exit(1)

if __name__ == "__main__":
    main()
