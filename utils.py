import pandas  as pd
import matplotlib.pyplot as plt

#Porcentaje de registros que tienen y no tienen COVID.
def percentage_confirment_covid(df, total):
    percentage_covid = (df['clasificacion_final'].value_counts() / total) * 100
    filter_covid = percentage_covid.loc[['DESCARTADO', 'CONFIRMADO']].round(2)
    labels = filter_covid.index
    values = filter_covid.values
    return labels, values
    
#Porcentaje de las personas fallecidas y no fallecidas por tener COVID.
def percentage_dead_covid(df, total):
    clasificaion = df[df['clasificacion_final'] == 'CONFIRMADO']
    percentage_dead = (clasificaion['condicion_final'].value_counts() / total) * 100
    labels = percentage_dead.index
    values = percentage_dead.values
    return labels, values

#Porcentaje de hombres y mujeres con COVID.
def percentage_boy_girl_covid(df, total):
    casos_covid = df[df['clasificacion_final'] == 'CONFIRMADO']
    porcentaje_hombres_covid = (casos_covid['sexo_paciente'].value_counts() / total) * 100
    labels = porcentaje_hombres_covid.index
    values = porcentaje_hombres_covid.values
    return labels, values
    
#Porcentajes de personas que tienen COVID por provincia.
def percentage_province_covid(df, total):
    casos_covid_province = df[(df['clasificacion_final'] == 'CONFIRMADO')]
    percentage_province_covid = (casos_covid_province['provincia_residencia'].value_counts() / total) * 100
    labels = percentage_province_covid.index
    values = percentage_province_covid.values
    return labels, values
    
#Sacar por rango de edades (0-18, 19-30, 31-45, 45-60, 60-75, mayor a 75) los porcentajes de personas con COVID.
def percentage_for_age(df, total):
    rangos_edad = [
        (0, 18),
        (19, 30),
        (31, 45),
        (46, 60),
        (61, 75),
        (76, float('inf'))  
    ]
    porcentajes = []
    etiquetas = []
    for inicio, fin in rangos_edad:
        casos_covid = df[(df['clasificacion_final'] == 'CONFIRMADO') & 
                         (df['edad_paciente'] >= inicio) & 
                         (df['edad_paciente'] <= fin)]
        porcentaje = (len(casos_covid) / total) * 100
        porcentajes.append(porcentaje)
        etiquetas.append(f"{inicio}-{fin}")
    labels = etiquetas
    values = porcentajes
    return labels, values

