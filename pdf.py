import os
import reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, PageBreak, SimpleDocTemplate
from datetime import date


import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

textos = []
versoBA = "Objetivos do curso e o brigadista – conhecer os objetivos do curso, responsabilidade e comportamento do brigadista;Teoria do Fogo – Conhecer a combustão, seus elementos, funções, pontos de temperatura e ração em cadeia;Propagação do fogo – Conhecer os processos de propagação do fogo através do calor (condução, convecção e irradiação);Classes de incêndio, A, B, C e D;Prevenção de incêndio – conhecer as técnicas de prevenção para avaliação dos riscos potencial;Conhecer os métodos de extinção e suas aplicações – Isolamento, abafamento, resfriamento e quebra da reação em cadeia;Conhecer os agentes extintores, suas características, aplicações e manuseio Co2. Pqs, Água, EPM e outros;Conhecer os equipamentos de proteção individual para os riscos expostos da emergência;Conhecer os equipamentos de combate a incêndio, extintores, hidrantes, mangueiras e acessórios;Conhecer os meios mais comuns de sistema e manuseio dos equipamentos de detecção;Conhecer as técnicas de abandono de área, saída organizada, pontos de encontro, chamada e controle de pânico;Descrever as técnicas de abordagem, cuidados e condução de acordo com o plano de emergência;da planta para pessoas com mobilidade reduzida;Discutir os riscos específicos e o plano de emergência contra incêndio da planta;Psicologia em emergência - Conhecer a reação das pessoas em situações de emergência."
verso2BA = "Avaliação inicial – Conhecer os riscos iminentes do cenário, os mecanismos da lesão, número de vítimas e o exame físico destas; Vias aéreas – Conhecer os sinais e sintomas de obstrução em adultos, crianças e bebês consciente e inconsciente;Desobstrução das vias aéreas – Elevação queixo (desmaio), Obstrução total - Manobra de Heimlich em adultos, crianças e bebês; RCP – Conhecer as técnicas de reanimação cardiopulmonar para adultos, crianças e bebês (protocolo AHA 2015);Hemorragia - Descrever as técnicas de hemostasia – pressão direta no ferimento, pontos de compressão, estado de choque; Posição de recuperação."
verso3BA = "Extintores Portáteis: Dióxido de Carbono 6 kg / Pó Químico 4 kg / Água 10l; Hidrantes, mangueiras, esguichos, chaves storz e acessórios;P.E.B – Ponto de encontro da Brigada – Recursos e acessórios para atendimento as emergências internas;Prancha rígida de madeira, bolsa de primeiros socorros com acessórios para atendimento e resgate (demonstração em sala); Simulador Torso e bebê Litlle Anne para manobras de Heimlich e RCP em sala de aula."


def mm2p (milimetros):
    return milimetros / 0.352777


def crated_pdf(sigla, corporates, lists, data):

    font_folder = os.path.join(os.path.dirname(reportlab.__file__), "fonts")
    image_folder = os.path.join(os.path.dirname(__file__), "public");
    WorkSans_Bold = os.path.join(font_folder, "WorkSans-Bold.ttf")
    WorkSans = os.path.join(font_folder, "WorkSans-Regular.ttf")
    logo_treinnar = os.path.join(image_folder, 'logo_treinnar.jpg')
    logo_conecta = os.path.join(image_folder, 'logo_conecta.jpg')
    assinatura = os.path.join(image_folder, 'assinatura.jpeg')
    
    # print(A4)
    peoples = lists[['NOME', 'RG', 'CPF', 'DATA_NASC', 'TREINAMENTO', 'HORAS']].loc[lists['SIGLA'] == sigla].values.tolist()
    coluns = lists[['NOME', 'RG', 'CPF', 'DATA_NASC', 'TREINAMENTO', 'HORAS']].loc[lists['SIGLA'] == sigla].columns.values.tolist()
    widthTable = [mm2p(4), mm2p(80), mm2p(110), mm2p(140), mm2p(165), mm2p(195)]
    razaoSocial = corporates[['NOME', 'ENDERECO','CNPJ', 'SIGLA', 'CIDADE', 'ESTADO','CEP', 'LUGAR',]].loc[corporates['SIGLA'] == sigla].values.tolist()
    
    if len(peoples) > 0:
        # === Configurações === 
        # doc = SimpleDocTemplate('./PDF/' + sigla + '.pdf', pagesize=A4)
        cnv = canvas.Canvas('./PDF/' + sigla + '.pdf', pagesize=A4, lang='PT-BR');
        pdfmetrics.registerFont(TTFont('Work Sans', WorkSans));
        pdfmetrics.registerFont(TTFont('Work Sans - Bold', WorkSans_Bold));
        
        # === Header ===
        cnv.drawImage(image="./public/logo_treinnar.jpg", width=180, height=80, x=mm2p(8), y=mm2p(297-35));
                
        # === Footer ===
        cnv.setFont ( 'Work Sans - Bold' , 12 );
        cnv.drawCentredString(text= razaoSocial[0][7] + ", " + data + ".",x=mm2p(210/2),y=mm2p(90));
        
        # === Empresa === 
        cnv.setFont ( 'Work Sans - Bold' , 10 ); 
        cnv.drawString(x= 10, y=mm2p(220+3), text='Empresa: ');
        cnv.drawString(x= 10, y=mm2p(215+3), text='Endereço: ');
        cnv.drawString(x= 10, y=mm2p(210+3), text='CNPJ: ');
        
        cnv.setFont ( 'Work Sans' , 10 ); 
        cnv.drawString(x= 80, y=mm2p(220+3), text = razaoSocial[0][0] + " (" + razaoSocial[0][3]+")");
        cnv.drawString(x= 80, y=mm2p(215+3), text = str(razaoSocial[0][1]) + " - " + str(razaoSocial[0][4]) + " - "  + str(razaoSocial[0][5]) + " - " + str(razaoSocial[0][6]));
        cnv.drawString(x= 80, y=mm2p(210+3), text = razaoSocial[0][2]);
        
        # === Tabela ===        
        cnv.setFont ( 'Work Sans - Bold' , 10 ); 
        for index, label in enumerate(coluns):
            cnv.drawString(x=widthTable[index], y=mm2p(205), text=str(label))
            
        cnv.setFont ( 'Work Sans' , 8);    
        for index, item in enumerate(peoples):
            for i, dados in enumerate(item):
                cnv.drawString(x=widthTable[i], y=mm2p(200-5 * index + 1), text=str(dados))
        
        # === Assinatura ===
        cnv.drawImage(image=assinatura, width=150, height=50, x=mm2p((210/2)-(150/6)), y=mm2p(90-25));
        
        cnv.setFont ( 'Work Sans - Bold' , 12 );
        cnv.drawCentredString(text="POLYANE OLIVEIRA CIVIRINO",x=mm2p(210/2), y=mm2p(90-30));
        
        cnv.setFont ( 'Work Sans' , 10 );
        cnv.drawCentredString(text="Instrutor/Resp. Técnico.",x=mm2p(210/2),y=mm2p(90-34));
        cnv.drawCentredString(text="320.827.408-46 | CBO n° 351605",x=mm2p(210/2),y=mm2p(90-38));
        
        # === Dados treinnar ===
        cnv.setLineWidth(5)
        cnv.line(x1=mm2p(10), x2=mm2p(200), y1=mm2p(90-50), y2=mm2p(90-50));
        cnv.line(x1=mm2p(10), x2=mm2p(200), y1=mm2p(90-80), y2=mm2p(90-80));

        initY = 32
        
        cnv.setFont ( 'Work Sans' , 8 );
        cnv.drawString(text="TREINNAR SERVIÇOS E EQUIPAMENTOS CONTRA INCENDIO LTDA - CNPJ/MF n° 02.837.835/0001-26",x=mm2p(10), y=mm2p(initY - 3));
        cnv.drawString(text="End. Correspondência: Rua Caramuru, n° 515 - Vila Conceção, Diadema, São Paulo/SP - 09911-510",x=mm2p(10), y=mm2p(initY - 6));
        cnv.drawString(text="End. CT: Rua Dolomita, n° 1346 - Bairro Mikail II, Guarulhos - São Paulo/SP - 07145-020",x=mm2p(10), y=mm2p(initY - 9));
        cnv.drawString(text="Telefone: +55 (11) 3382-8100",x=mm2p(10), y=mm2p(initY - 12));
        cnv.drawImage(image=logo_conecta, width=150, height=35,x=mm2p(150), y=mm2p(90-70));
        
        match razaoSocial[0][5]:
            case 'BA':
                print('Unidade da Bahia: ' + sigla );
                
                # === Titulo ===
                cnv.setFont ( 'Work Sans - Bold' , 16 );
                cnv.drawCentredString(x=mm2p(210/2), y=mm2p((297-35-5)), charSpace=2, text="ATESTADO DE BRIGADA");
                
                cnv.setFont ( 'Work Sans' , 14);
                describe = Paragraph(
                "A empresa Treinnar Serviços e Equipamentos Contra Incendio LTDA, CNPJ 02.837.835/0002-07, " + 
                "Número de Registro CCR Nº 481/2024 , atesta para os devidos fins que as pessoas abaixo relacionadas participaram com bom aproveitamento do treinamento de "+
                '"BRIGADA DE INCÊNDIO – NÍVEL I", referente à edificação localizada na ' +
                str(razaoSocial[0][1]) + " - " + str(razaoSocial[0][4]) + " - "  + str(razaoSocial[0][5]) + " - " + str(razaoSocial[0][6]) +
                " e estão aptas ao manuseio dos equipamentos de prevenção e combate a incêndio.");

                describe.wrapOn(cnv, aW=580, aH=None);
                describe.drawOn(cnv, x=10, y=mm2p((232)));
                
                cnv.setFont ( 'Work Sans' , size=10);
                cnv.drawString(text="Nota 1: Conforme Tabela B.2, da IT 17/2016.", x=mm2p(10), y=mm2p(110));
                cnv.drawString(text="Nota 2: Conforme item 5.9, da IT 05/2021.", x=mm2p(10), y=mm2p(105));
                cnv.drawString(text="Nota 3: Conforme item 6.1.2.2, da IT 05/2021.", x=mm2p(10), y=mm2p(100));
                cnv.drawCentredString(text="Registro CCIBI n° 286/2024",x=mm2p(210/2),y=mm2p(90-38-4));


                cnv.showPage();
                # === VERSO ===
                cnv.setFont ( 'Work Sans - Bold' , 16 );
                cnv.drawCentredString(text="TEÓRICO DE COMBATE A INCÊNDIO", x=mm2p(210/2), y=mm2p(280));

                cnv.setFont ( 'Work Sans' , 10);
                textos = versoBA.split(';');
                i = 1;
                
                for item in textos:
                    text = Paragraph(item)
                    text.wrapOn(cnv, aW=580, aH=None);
                    text.drawOn(cnv, x=10, y=mm2p(275 - (5*i)));
                    i = i+1
                cnv.setFont ( 'Work Sans - Bold' , 12 );
                cnv.drawCentredString(text="TEÓRICO DE PRIMEIRO SOCORROS", x=mm2p(210/2), y=mm2p(275 - (5*(i+1))));
                i = i+1
                cnv.setFont ( 'Work Sans' , 10);
                textos = verso2BA.split(';');

                for item in textos:
                    text = Paragraph(item)
                    text.wrapOn(cnv, aW=580, aH=None);
                    text.drawOn(cnv, x=10, y=mm2p(275 - (5*(i+1))));
                    i = i+1

                cnv.setFont ( 'Work Sans - Bold' , 12 );
                cnv.drawCentredString(text="EQUIPAMENTOS UTILIZADOS PARA DEMONSTRAÇÃO", x=mm2p(210/2), y=mm2p(275 - (5*(i+1))));
                i = i+1
                cnv.setFont ( 'Work Sans' , 10);
                textos = verso3BA.split(';');
                i = i+1
                for item in textos:
                    text = Paragraph(item)
                    text.wrapOn(cnv, aW=580, aH=None);
                    text.drawOn(cnv, x=10, y=mm2p(275 - (5*(i+1))));
                    i = i+1

                

                # === Dados treinnar ===
                cnv.setLineWidth(5)
                cnv.line(x1=mm2p(10), x2=mm2p(200), y1=mm2p(90-50), y2=mm2p(90-50));
                cnv.line(x1=mm2p(10), x2=mm2p(200), y1=mm2p(90-80), y2=mm2p(90-80));

                initY = 32
                
                cnv.setFont ( 'Work Sans' , 8 );
                cnv.drawString(text="TREINNAR SERVIÇOS E EQUIPAMENTOS CONTRA INCENDIO LTDA - CNPJ/MF n° 02.837.835/0001-26",x=mm2p(10), y=mm2p(initY - 3));
                cnv.drawString(text="End. Correspondência: Rua Caramuru, n° 515 - Vila Conceção, Diadema, São Paulo/SP - 09911-510",x=mm2p(10), y=mm2p(initY - 6));
                cnv.drawString(text="End. CT: Rua Dolomita, n° 1346 - Bairro Mikail II, Guarulhos - São Paulo/SP - 07145-020",x=mm2p(10), y=mm2p(initY - 9));
                cnv.drawString(text="Telefone: +55 (11) 3382-8100",x=mm2p(10), y=mm2p(initY - 12));
                cnv.drawImage(image=logo_conecta, width=150, height=35,x=mm2p(150), y=mm2p(90-70));
            case 'RS':
                print('Unidade de Rio do Sul: '  + sigla);

                cnv.setFont ( 'Work Sans - Bold' , 16 );
                cnv.drawCentredString(x=mm2p(210/2), y=mm2p((297-35-5)), charSpace=2, text="CERTIFICADO DE TREINAMENTO");
                cnv.setFont ( 'Work Sans' , 14);
                describe = Paragraph(
                    'Certificamos para os devidos fins que os funcionários abaixo relacionados participaram com bom aproveitamento do treinamento de "Prevenção e Combate a Incêndio e Primeiros Socorros", na data ' +
                    data + 
                    ', conforme programa constante no verso, com 05 (cinco) horas aula, em atendimento as exigências da Resolução Técnica N° 014/BM-CCB/2009, sendo considerado(s) apto(s)'
                );

                describe.wrapOn(cnv, aW=580, aH=None);
                describe.drawOn(cnv, x=10, y=mm2p((232)));
                
                cnv.showPage();
                # === VERSO ===
                cnv.setFont ( 'Work Sans - Bold' , 16 );
                cnv.drawString(text="TREINAMENTO DE COMBATE A INCÊNDIO/PRIMEIROS SOCORROS", x=mm2p(10), y=mm2p(280));

                cnv.setFont ( 'Work Sans' , 14);
                cnv.drawString(text="RESOLUÇÃO TÉCNICA - RT14/2009", x=mm2p(10), y=mm2p(275));
                
                cnv.setFont ( 'Work Sans - Bold' , 12 );
                cnv.drawString(text="Matéria", x=mm2p(10), y=mm2p(265));
                cnv.drawString(text="Carga horário", x=mm2p(10), y=mm2p(260));
                cnv.drawString(text="Teoria", x=mm2p(10), y=mm2p(255));
                cnv.drawString(text="Prevenção e combate a incêndio", x=mm2p(10), y=mm2p(250));
                
                cnv.setFont ( 'Work Sans' , 12);
                cnv.drawString(text="- Teoria do fogo", x=mm2p(10), y=mm2p(245));
                cnv.drawString(text="- Propagação do fogo", x=mm2p(10), y=mm2p(240));
                
                cnv.setFont ( 'Work Sans - Bold' , 12 );
                cnv.drawString(text="Classes de incêndio", x=mm2p(10), y=mm2p(235));
                
                cnv.setFont ( 'Work Sans' , 12);
                cnv.drawString(text="- Método de extinção", x=mm2p(10), y=mm2p(230));
                cnv.drawString(text="- Agentes extintores", x=mm2p(10), y=mm2p(225));
                cnv.drawString(text="- Equipamentos de combate a incêndio", x=mm2p(10), y=mm2p(220));
                cnv.drawString(text="- Equipamentos de detecção, alarme e comunicação", x=mm2p(10), y=mm2p(215));
                cnv.drawString(text="- 02 horas aula", x=mm2p(10), y=mm2p(210));
                
                cnv.setFont ( 'Work Sans - Bold' , 12 );
                cnv.drawString(text="Primeiro socorros", x=mm2p(10), y=mm2p(205));
                cnv.drawString(text="Parada cárdio-respiratória: procedimento de RCP", x=mm2p(10), y=mm2p(200));
                
                cnv.setFont ( 'Work Sans' , 12);
                cnv.drawString(text="- OVACE - Obstrução das Vias Aéreas por Corpos Estranhos: Procedimento de desobstrução", x=mm2p(10), y=mm2p(195));
                cnv.drawString(text="- 01 hora aula.", x=mm2p(10), y=mm2p(190));
                
                cnv.setFont ( 'Work Sans - Bold' , 12 );
                cnv.drawString(text="Prática", x=mm2p(10), y=mm2p(185));
                
                cnv.setFont ( 'Work Sans' , 12);
                cnv.drawString(text="- Combate a incêndio - Primeiros socorros", x=mm2p(10), y=mm2p(180));
                cnv.drawString(text="- 02 horas aula.", x=mm2p(10), y=mm2p(175));
                
                cnv.setFont ( 'Work Sans - Bold' , 12 );
                cnv.drawString(text="Total", x=mm2p(10), y=mm2p(170));
                
                cnv.setFont ( 'Work Sans' , 12);
                cnv.drawString(text="- 05 horas aula", x=mm2p(10), y=mm2p(165));
                
                # === Dados treinnar ===
                cnv.setLineWidth(5)
                cnv.line(x1=mm2p(10), x2=mm2p(200), y1=mm2p(90-50), y2=mm2p(90-50));
                cnv.line(x1=mm2p(10), x2=mm2p(200), y1=mm2p(90-80), y2=mm2p(90-80));

                initY = 32
                
                cnv.setFont ( 'Work Sans' , 8 );
                cnv.drawString(text="TREINNAR SERVIÇOS E EQUIPAMENTOS CONTRA INCENDIO LTDA - CNPJ/MF n° 02.837.835/0001-26",x=mm2p(10), y=mm2p(initY - 3));
                cnv.drawString(text="End. Correspondência: Rua Caramuru, n° 515 - Vila Conceção, Diadema, São Paulo/SP - 09911-510",x=mm2p(10), y=mm2p(initY - 6));
                cnv.drawString(text="End. CT: Rua Dolomita, n° 1346 - Bairro Mikail II, Guarulhos - São Paulo/SP - 07145-020",x=mm2p(10), y=mm2p(initY - 9));
                cnv.drawString(text="Telefone: +55 (11) 3382-8100",x=mm2p(10), y=mm2p(initY - 12));
                cnv.drawImage(image=logo_conecta, width=150, height=35,x=mm2p(150), y=mm2p(90-70));
            case _:
                print('Unidade da '  + razaoSocial[0][7] +': '+ sigla );
                # === Titulo ===
                cnv.setFont ( 'Work Sans - Bold' , 16 );
                cnv.drawCentredString(
                    x=mm2p(210/2), 
                    y=mm2p((297-35-10)), 
                    charSpace=2, 
                    text="ATESTADO DE BRIGADA"
                );
                
                # === Disseres ===
                describe = Paragraph("Atesto para os devidos fins, que as pessoas abaixo relacionadas participaram com bom aproveitamento do treinamento de 'Brigada de Incêndio - Prevenção e Combate a Incêndio e Primeiros Socorros', e estão aptas ao manuseio dos equipamentos de prevenção e combate a incêndio da edificação.");
                cnv.setFont ( 'Work Sans' , size=12 );
                cnv.drawString(text="Conforme a tabela B.2 da IT 17.", x=mm2p(10), y=mm2p(100));
                describe.wrapOn(cnv, aW=580, aH=None);
                describe.drawOn(cnv, x=10, y=mm2p((232)));
        
        cnv.save()