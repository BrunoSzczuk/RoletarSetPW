import pytesseract as ocr
from PIL import Image
import PIL
import ctypes
import pytesseract #screenshot
import PIL.ImageOps
import time
import pyautogui #Biblioteca automação
import re
import function as f
from string import punctuation

tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
ocr.pytesseract.tesseract_cmd=tesseract

def main(): 

    Quant = int(input("Qual o mínimo de int que vc quer?\n"))
    QuantRolete = 500000#input("Quantas Escultura da Reforja você possui?\n")

    rolete = int(QuantRolete)/2
    finalizador = 0

    #f.ShowWindow() #Abre a Janela do pw

    pyautogui.keyDown('alt')
    time.sleep(.2)
    pyautogui.press('tab')
    time.sleep(.2)
    
    pyautogui.keyUp('alt')
    time.sleep(.2)
    #BotaoReproduzir = f.LocateButton() #Localiza as coordenadas X e Y do botao reproduzir
    BotaoReproduzir = pyautogui.locateOnScreen('C:\projetos\Roletar set\\btnReforja.png', confidence=.9)
    #print(BotaoReproduzir)
    if (BotaoReproduzir is None):
        print('Não foi encontrado o botão REFORJA na tela aberta, Tente novamente')
        exit()
    BotaoReproduzir = [BotaoReproduzir[0]+15,BotaoReproduzir[1]+5]
    #AreaAdds_X, AreaAdds_Y = {}, {}


    #o 2° parametro tem que ter 50px a mais
    #AreaAdds_X[0], AreaAdds_X[1] = int(BotaoReproduzir[0]+400), int(BotaoReproduzir[0]+340) #calcula a area do adds
    #o 2° parametro temq ue ter 115px a mais
    #AreaAdds_Y[0], AreaAdds_Y[1] = int(BotaoReproduzir[1]+200), int(BotaoReproduzir[1]+430)

    while(finalizador <= rolete):

        
        pyautogui.click(BotaoReproduzir[0], BotaoReproduzir[1]); #CLica no botao Reproduzir
        pyautogui.moveTo(BotaoReproduzir[0]+65,BotaoReproduzir[1]-215)
        time.sleep(1.2) #Espera 0.5 segundo para forjar o item

        #imagem = pyautogui.screenshot(r'testeSet.png')
        imagem = pyautogui.screenshot()
        areaAdds = pyautogui.locateOnScreen('C:\projetos\Roletar set\\destreza.png', confidence=.9);
        if (not areaAdds is None):
            #area = (AreaAdds_X[0], AreaAdds_Y[0], AreaAdds_X[1], AreaAdds_Y[1]) #Defino o tamanho e o local da area a ser corada na imagem
            cropped_img = imagem.crop((areaAdds.left +areaAdds.width/2, areaAdds.top, areaAdds.left + areaAdds.width, areaAdds.top +  areaAdds.height)) #Corta a area na imagem onde ficam os adds
            #cropped_img.show() #Mostra a imagem cortada
            img_op = PIL.ImageOps.invert(cropped_img) #Inverte as cores para facilitar a leitura dos adds
            #img_op.show()
            txt_adds = ocr.image_to_string(img_op) #Extrai o texto da imagem e coloca na variavel
            #print(txt_adds)
            
            adds = re.split(r'[^0-9]+',txt_adds) #Separa os palavras em lista
            print(adds)
        
            seis = adds.count("6") * 6
            sete = adds.count("7") * 7; oito = adds.count("8") * 8
            nove = adds.count("9") * 9; dez = (adds.count("40") + adds.count("10")) *10;onze = (adds.count("41")  + adds.count("11")) *11; doze = (adds.count("42")+ adds.count("12")) *12; 

            TotalNum = seis + sete + oito + nove + dez + onze + doze
            print('total: ', TotalNum)
            
            if TotalNum >= Quant:
                #pyautogui.click(BotaoReproduzir[0]+155,BotaoReproduzir[1]-15) #CLica em segurar o novo add
                pyautogui.alert('Parabéns, conseguimos uma parte do set com '+ str(TotalNum) +' de dex ','Gideon','OK')
                exit() #fecha o programa
          #  else:
          #     pyautogui.click(BotaoReproduzir[0]-170,BotaoReproduzir[1]-15) #Clica em manter o antigo add
          #      time.sleep(1.5)

main()