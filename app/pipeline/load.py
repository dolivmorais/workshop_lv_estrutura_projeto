import os

import pandas as pd

""""
receber um dartaframe e salvar em um arquivo excel
args: dataframe, path (str) caminho para salvar o arquivo excel
output_path: str caminho para salvar o arquivo excel
file_name: str nome do arquivo excel

return "arquivo salvo"
"""


def load_excel(
    dataframe: pd.DataFrame, output_path: str, file_name: str
) -> str:
    """se não existe o diretório, cria-o"""
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    dataframe.to_excel(os.path.join(output_path, file_name), index=False)
    return f'Arquivo {file_name} salvo em {output_path}'
