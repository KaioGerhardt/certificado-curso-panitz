from PIL import Image,ImageDraw, ImageFont
from numpy import character

class GeradorCertificado:
    def __init__(self):
        self.nome_arquivo = ''
        self.lista_alunos = []
        self.lista_data = []
        self.lista_validade = []

    def ler_arquivo(self,arquivo):
        arquivo = open(arquivo,'r')
        return arquivo.read()
        

    def gerar_certificado(self):
        
        dados = self.ler_arquivo('font/alunos.txt')
        dadosdata = self.ler_arquivo('font/data')
        dadosvalidade = self.ler_arquivo('font/validade')

        for elemento in dados.split('\n'):
            self.lista_alunos.append(elemento)
        
        for elemento in dadosdata.split('\n'):
            self.lista_data.append(elemento)
            
        for elemento in dadosvalidade.split('\n'):
            self.lista_validade.append(elemento)

        for data in self.lista_data:    
            im = Image.open("certificado_modelo2.png").convert('RGBA')
            txt = Image.new('RGBA', im.size, (255,255,255,0))
            fnt_nome = ImageFont.truetype('font/Constantia/constantia.ttf', 60)
            fnt_descrição = ImageFont.truetype('font/Constantia/constantia.ttf', 78)
            fnt_bold = ImageFont.truetype('font/Constantia/constanb.ttf', 80)
            d = ImageDraw.Draw(txt)
        
        for validade in self.lista_validade:    
                im = Image.open("certificado_modelo2.png").convert('RGBA')
                txt = Image.new('RGBA', im.size, (255,255,255,0))
                fnt_nome = ImageFont.truetype('font/Lato/Lato-Regular.ttf', 60)
                fnt_descrição = ImageFont.truetype('font/Constantia/constantia.ttf', 78)
                fnt_bold = ImageFont.truetype('font/Baskerville/Baskerville Bold font.ttf', 80)
                d = ImageDraw.Draw(txt)
        
        #função por último    
        for aluno in self.lista_alunos:    
            im = Image.open("certificado_modelo2.png").convert('RGBA')
            txt = Image.new('RGBA', im.size, (255,255,255,0))
            fnt = ImageFont.truetype('font/Constantia/constantia.ttf', 200)
            d = ImageDraw.Draw(txt)
            fnt_bold = ImageFont.truetype('font/Constantia/constanb.ttf', 80)
            fnt_descrição = ImageFont.truetype('font/Constantia/constantia.ttf', 78)

            if len(aluno) <= 50:
                #gambiarra master
                cpf_invertido = aluno[::-1]
                cpf_num = cpf_invertido[0:14] #numero de caracteres do CPF
                cpf_final = cpf_num [::-1]
                #final da gambiarra master

                #gambiarra master master
                #remover = cpf_invertido[0:11]
                remover = cpf_final + aluno[0:3] 
                string = cpf_invertido
                characters = remover

                nome_final = ''.join( x for x in string if x not in characters)
                nome_final = nome_final[::-1]
                #final da gambiarra master master

                #INFORMAÇÕES DO CABEÇALHO
                d.text((650,130), f"PANITZ EQUIPAMENTOS CONTRA INCENDIO LTDA" , font=fnt_bold, fill=(0,0,0,255))
                d.text((550,270), f"TREINAMENTO DE PREVENCAO E COMBATE A INCÊNDIO" , font=fnt_bold, fill=(0,0,0,255))
                d.text((1200,500), f"Certificado n° {aluno[0:3]}/2022", font=fnt_bold, fill=(0,0,0,255))

                #INFORMAÇÕES DO CERTIFICADO
                d.text((350,800), f"Certifico que o (a) Sr. (a) {nome_final[0::]}, frequentou o Treinamento" , font=fnt_descrição, fill=(0,0,0,255))
                d.text((130,900), f"de Prevenção e Combate a Incêndio, conforme programa constante no verso, no dia {data[0:5]}" , font=fnt_descrição, fill=(0,0,0,255))
                d.text((130,1000), f"Janeiro de  2022 com 5 hora/aula, com 100% de frequência, sendo considerado(a) apto (a)." , font=fnt_descrição, fill=(0,0,0,255)) 
                d.text((130,1100), f"Corpo docente: RAFAEL ADOLPHO SILVA""", font=fnt_descrição, fill=(0,0,0,255))

                #INFORMAÇÕES DE DATA
                d.text((130,1300), f"Novo Hamburgo, {data} " , font=fnt_bold, fill=(0,0,0,255))

                #INFORMAÇÕES DO DOCENTE
                d.text((1850,1750), f"_________________________________" , font=fnt_bold, fill=(0,0,0,255))
                d.text((2150,1850), f"RAFAEL ADOLPHO SILVA" , font=fnt_bold, fill=(0,0,0,255))
                d.text((2050,1950), f"Registro no MTE/RS nº 001624-9" , font=fnt_descrição, fill=(0,0,0,255))
                d.text((1850,2050), f"REG. no 8º BBM-CBM-RS Nº 475/2020" , font=fnt_descrição, fill=(0,0,0,255))

                #INFORMAÇÕES DO ALUNO PARA ASSINATURA
                d.text((150,1750), f"_________________________________" , font=fnt_bold, fill=(0,0,0,255))
                d.text((180,1850), f"{nome_final[0::]}" , font=fnt_bold, fill=(0,0,0,255))
                d.text((180,1950), f"CPF: {cpf_final}" , font=fnt_descrição, fill=(0,0,0,255))
                #d.text((1850,2050), f"REG. no 8º BBM-CBM-RS Nº 475/2020" , font=fnt_descrição, fill=(0,0,0,255))

                #VALIDADE DO CERTIFICADO
                d.text((150,2250), f"Valido até: {validade}" , font=fnt_descrição, fill=(0,0,0,255))
                
                out = Image.alpha_composite(im, txt)
                nome_aluno = aluno.split()
                self.nome_arquivo = nome_aluno[0]
                out.save(f'./imgs/{self.nome_arquivo}.png')
                print(f'Foi gerado com sucesso o certificado do aluno: {aluno}')
            else:
                print('O nome do aluno Ultrapassou o valor de caracteres permitidos')
 
#FUNCAO TEMPORARIA
if __name__ == "__main__":
    
    gerador_certificado = GeradorCertificado()

    try:
        gerador_certificado.gerar_certificado()
    except Exception as ex:
        print(f'Algo deu errado {ex}')