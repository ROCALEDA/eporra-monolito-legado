import os
import requests

class CarreraAPI():
    def __init__(self):
        self.base_url = os.getenv('URL_BASE')

    def get_carreras(self):
        url = self.base_url + 'races'
        response = requests.get(url)
        if response.status_code == 200:
            listaCarreras = response.json()
            carreras_adaptadas = []
            for carrera in listaCarreras:
                carreras_adaptadas.append({
                    'id': carrera['id'],
                    'nombre': carrera['nombre'],
                    'estaTerminada': carrera['estaTerminada']
                })
            return carreras_adaptadas
        else:
            print(f"Error al obtener las carreras: {response.status_code}")
            return None

    def get_carrera(self, id):
        url = self.base_url + f'races/{id}'
        response = requests.get(url)
        if response.status_code == 200:
            carrera = response.json()
            return {
                'id': carrera['id'],
                'nombre': carrera['nombre'],
                'estaTerminada': carrera['estaTerminada']
            }
        else:
            print(f"Error al obtener la carrera: {response.status_code}")
            return None
