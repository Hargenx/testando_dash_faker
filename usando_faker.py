import pandas as pd
from faker import Faker
from datetime import datetime, timedelta
import random

# Configurar Faker
fake = Faker('pt-BR')

# Gerar dados fictícios
n_entries = 100
start_date = datetime(2023, 11, 17)  # Data para iniciar as consultas
data = []

for _ in range(n_entries):
    paciente = fake.name()
    data_consulta = start_date + timedelta(days=random.randint(1, 30))
    hora_consulta = fake.time()
    duracao = random.choice([30, 60])
    especialidade = fake.random_element(elements=('Cardiologia', 'Oftalmologia', 'Ginecologia', 'Dermatologia'))
    convenio = fake.random_element(elements=('Amil', 'Unimed', 'Bradesco Saúde', 'SulAmérica'))
    numero_consultas = random.randint(1, 3)

    data.append([paciente, data_consulta.strftime('%Y-%m-%d'), hora_consulta, duracao, especialidade, convenio, numero_consultas])

# Criar DataFrame
df = pd.DataFrame(data, columns=['paciente', 'data', 'hora', 'duracao', 'especialidade', 'convenio', 'numero_consultas'])

# Adicionar dados ao DataFrame existente
df.to_csv('dados_exemplo.csv', index=False)
