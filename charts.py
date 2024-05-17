import matplotlib.pyplot as plt
import charts
colors = ['#98FB98', '#ADD8E6']

#Grafica para el porcentaje de registros que tienen y no tienen COVID.
def get_confirment_covid(ax, labels, values):
    ax.bar(labels, values, color = colors[:len(labels)])
    ax.set_xlabel('Clasificación')
    ax.set_ylabel('Porcentaje')
    

#Grafica para el porcentaje de las personas fallecidas y no fallecidas por tener COVID.
def get_dead_covid(ax, labels, values):
    ax.bar(labels, values, color = colors[:len(labels)])
    ax.set_xlabel('Condicion')
    ax.set_ylabel('Porcentaje')
    
#Grafica para el porcentaje de hombres y mujeres con COVID.
def get_boy_girl_covid(ax, labels, values):
    ax.bar(labels, values, color = colors[:len(labels)])
    ax.set_xlabel('Sexo')
    ax.set_ylabel('Porcentaje')
    
#Grafica para el porcentaje de personas que tienen COVID por provincia.
def get_province_covid(ax, labels, values): 
    sorted_data = sorted(zip(labels, values), key=lambda x: x[1])
    sorted_labels, sorted_values = zip(*sorted_data)
    ax.barh(sorted_labels, sorted_values, color=colors[:len(sorted_labels)])
    ax.set_xlabel('Provincia')
    ax.set_ylabel('Porcentaje')
    
    
#Grafica para sacar por rango de edades (0-18, 19-30, 31-45, 45-60, 60-75, mayor a 75) los porcentajes de personas con COVID.
def get_for_age(ax, labels, values):
    ax.bar(values, labels, color = colors[:len(labels)])
    ax.set_xlabel('Grupo de Edad')
    ax.set_ylabel('Porcentaje')
    ax.tick_params(axis='x', rotation=45)
    
#Funcion para indicar la cantidad de graficos que uno desea.
def generate_subgraphs(funciones):
    num_funciones = len(funciones)
    filas = num_funciones // 3
    if num_funciones % 3 != 0:
        filas += 1
        
    fig, axes = plt.subplots(nrows=filas, ncols=3, figsize=(26, 4 * filas))
    return fig, axes

#Funcion para dibujar los graficos
def draw_graphics(funciones, axes):
    for i, (funcion, args, title) in enumerate(funciones):
        labels, values = funcion(*args)
        charts_function = getattr(charts, funcion.__name__.replace("percentage_", "get_"))
        row = i // 3
        col = i % 3
        ax = axes[row, col]
        charts_function(ax, labels, values)
        ax.set_title(title)

    for i in range(len(funciones), axes.size):
        ax = axes.flatten()[i]
        ax.axis('off')

    plt.tight_layout()
    plt.show()