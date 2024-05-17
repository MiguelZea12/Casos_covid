import pandas as pd
import utils
import charts

def app():
    df = pd.read_csv('MSP_cvd19_casos_20220403.csv', encoding='ISO-8859-1', delimiter=';')
    total = len(df)
    
    funciones = [
        (utils.percentage_confirment_covid, (df, total), 'Porcentaje de casos de COVID-19'),
        (utils.percentage_dead_covid, (df, total), 'Porcentaje de personas fallecidas'),
        (utils.percentage_boy_girl_covid, (df, total), 'Porcentaje de hombres y mujeres con COVID'),
        (utils.percentage_province_covid, (df, total), 'Porcentajes de personas que tienen COVID por provincia.'),
        (utils.percentage_for_age, (df, total), 'Porcentaje de casos de COVID-19 por grupo de edad')
    ]
    
    fig, axes = charts.generate_subgraphs(funciones)
    charts.draw_graphics(funciones, axes)

if __name__ == '__main__':
    app()


