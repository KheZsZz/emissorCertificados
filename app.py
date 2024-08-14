import os
import pandas as pd
from pdf import crated_pdf


corporates = pd.read_excel('./src/database/cadastro.xlsx', sheet_name='Cadastros')
listas = pd.read_excel('./src/database/Lote 4.xlsx', sheet_name='Listas')

listas['DATA_NASC'] = listas['DATA_NASC'].astype(str);


def for_in_array (sigla):
    try:
        crated_pdf(sigla, corporates, listas, data='31 de Agosto de 2024');
    except:
        print('ERROR AO EMITIR A DOCUMENTAÇÃO: ' + sigla);
# print(corporates['SIGLA'].loc[corporates["ESTADO"] == 'RS'])
corporates['SIGLA'].map( lambda sigla: for_in_array(sigla));     