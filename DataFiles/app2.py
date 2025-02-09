from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # Cargar el archivo CSV
    data = pd.read_csv('/workspaces/Tarea-Flask/DataFiles/Ejercicio1.csv')

    # Análisis simple: salario promedio por departamento
    salary_by_dept = data.groupby('Department')['Salary'].mean().reset_index()
    
    # Convertir a diccionario para pasarlo al HTML
    salary_data = salary_by_dept.to_dict(orient='records')

    return render_template('home.html', data=salary_data)

if __name__ == '__main__':
    app.run(debug=True)
