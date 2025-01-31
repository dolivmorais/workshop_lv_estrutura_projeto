import os
import glob
import pandas as pd
from typing import List
import openpyxl
"""
função para ler os arquivos de uma pasta de data/input e retornar um lista de dataframes
arhs: input_path (str) caminho da pasta dos arquivos de entrada
return uma lista de dataframes
"""

def estract_from_excel(path: str) -> List[pd.DataFrame]:
    all_files = glob.glob(os.path.join(path, "*.xlsx"))
    data_frame_list = []
    for file in all_files:
        data_frame_list.append(pd.read_excel(file))
    return data_frame_list


if __name__ == "__main__":
    print(estract_from_excel("data/input"))