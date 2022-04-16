import pandas as pd
import numpy as np
import datetime
from sklearn.impute import SimpleImputer

dados = pd.read_csv("./base_funcionarios.csv")

# Tratando as datas da coluna 'start date'
dados['start date'] = pd.to_datetime(dados['start date'])

# Tratando os registros da coluna 'location'
dados.loc[dados['location'] == 'CA', 'location'] = 'California'
dados.loc[dados['location'] == 'Calif.', 'location'] = 'California'
dados.loc[dados['location'] == 'NY', 'location'] = 'New York'

# Tratando os registros da coluna 'team matrix'
dados['team matrix'] = dados['team matrix'].str.replace(" ", "")

# Criando e tratando a coluna 'team code'
dados.insert(2, 'team code', dados['team matrix'].str.slice(0, 3))

# Criando e tratando a coluna 'team name'
dados.insert(3, 'team name', dados['team matrix'].str.slice(4,  15).str.lower())

# Concatenando as colunas 'team code' e 'team name', depois substituindo os registros da coluna 'team matrix'
dados['team matrix'] = dados['team code'].str.cat(dados['team name'], sep = '-')

# Tratando os registros da coluna 'employee'
dados['employee'] = dados['employee'].str.title()

# Tratando a coluna 'annual salary'
mean_imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
dataframe = pd.DataFrame(dados)
dataframe = mean_imputer.fit_transform(dataframe[['annual salary']])
dados['annual salary'] = dataframe

# Tratando a coluna 'performance level'
dataframe = pd.DataFrame(dados['performance level'])
dataframe = dataframe.fillna('NI', inplace = False)
dados['performance level'] = dataframe

dados