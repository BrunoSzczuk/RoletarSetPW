import re
import time

import PIL
import PIL.ImageOps
import pyautogui  # Biblioteca automação
import pytesseract as ocr

tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
ocr.pytesseract.tesseract_cmd = tesseract


def main():
    rolete = 500000  # input("Quantas Escultura da Reforja você possui?\n")

    finalizador = 0

    # f.ShowWindow() #Abre a Janela do pw

    pyautogui.keyDown('alt')
    time.sleep(.2)
    pyautogui.press('tab')
    time.sleep(.2)

    pyautogui.keyUp('alt')
    time.sleep(.2)
    # BotaoReproduzir = f.LocateButton() #Localiza as coordenadas X e Y do botao reproduzir
    BotaoReproduzir = pyautogui.locateOnScreen('C:\projetos\RoletarSetPW\\btnIniciarHoroscopo.png')
    # print(BotaoReproduzir)
    if (BotaoReproduzir is None):
        print('Não foi encontrado o botão na tela aberta, Tente novamente')
        exit()
    BotaoReproduzir = [BotaoReproduzir[0] + 15, BotaoReproduzir[1] + 5]
    # AreaAdds_X, AreaAdds_Y = {}, {}

    # o 2° parametro tem que ter 50px a mais
    # AreaAdds_X[0], AreaAdds_X[1] = int(BotaoReproduzir[0]+400), int(BotaoReproduzir[0]+340) #calcula a area do adds
    # o 2° parametro temq ue ter 115px a mais
    # AreaAdds_Y[0], AreaAdds_Y[1] = int(BotaoReproduzir[1]+200), int(BotaoReproduzir[1]+430)

    while finalizador <= rolete:
        pyautogui.click(BotaoReproduzir[0], BotaoReproduzir[1])  # CLica no botao Reproduzir
        pyautogui.moveTo(BotaoReproduzir[0] + 65, BotaoReproduzir[1] - 215)

        # imagem = pyautogui.screenshot(r'testeSet.png')
        imagem = pyautogui.screenshot()
        areaAstro = pyautogui.locateOnScreen('C:\projetos\RoletarSetPW\\areaAstro.png', confidence=0.5, grayscale=True)
        if areaAstro is None:
            print('Não foi a tela do astro, Tente novamente')
            exit()

        cropped_img = imagem.crop((areaAstro.left + 150 + areaAstro.width / 2, areaAstro.top + 85,
                                   areaAstro.left + areaAstro.width,
                                   areaAstro.top + areaAstro.height - 20))  # Corta a area na imagem onde ficam os adds
        # cropped_img.show() #Mostra a imagem cortada
        img_op = PIL.ImageOps.invert(cropped_img)  # Inverte as cores para facilitar a leitura dos adds

        txt_adds = ocr.image_to_string(img_op)  # Extrai o texto da imagem e coloca na variavel
        adds = re.split('\\n', txt_adds)  # Separa os palavras em lista
        qtdEspirios = [s for s in adds if "Espirito" in s]
        if len(qtdEspirios) < 2:
            continue
        qtdAtk = [s for s in adds if "Atq" in s]
        if len(qtdAtk) < 2:
            continue
        qtdDef = [s for s in adds if "Def" in s and (s.endswith("Def") or s.endswith("DefM"))]
        if len(qtdDef) < 2:
            continue
        qtdHp = [s for s in adds if "HP" in s]
        if len(qtdHp) < 2:
            continue
        qtdPen = [s for s in adds if "Penet" in s]
        if len(qtdPen) < 2:
            continue
        print("Espiritos: " + str(qtdEspirios) + " \\n")
        print("Ataque: " + str(qtdAtk) + " \\n")
        print("Defesa: " + str(qtdDef) + " \\n")
        print("HP: " + str(qtdHp) + " \\n")
        print("Penetração: " + str(qtdPen) + " \\n")
        exit()  # fecha o programa


main()
