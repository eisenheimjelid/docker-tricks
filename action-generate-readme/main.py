# -*- coding: utf-8 -*-

import glob
import json
import os


def update_readme_file(new_file_list, data_folder_path, readme_file_path):
    # Funcion interna
    def generate_content(content_data):

        name = content_data['name']  # Type: str
        desc = content_data['desc']  # Type: str
        code = content_data['code']  # Type: list<str>

        template = ["- ### {}".format(name),
                    "\n",
                    "{}".format(desc),
                    "\n\n",
                    "```console",
                    "\n"]

        for line in code:
            template.append(str(line))
            template.append("\n")

        template.append("```")
        template.append("\n")

        return template

    readme_content = []
    # Leer el contenido de cada archivo y agregarlo a la lista
    for file in new_file_list:
        file_path = os.path.join(data_folder_path, file)

        with open(file_path) as json_file:
            json_data = json.load(json_file)
            data = json_data['data'] if 'data' in json_data else None

        if data:
            readme_content += generate_content(data)

    with open(readme_file_path, 'a+') as f:
        print(readme_content)
        f.writelines(readme_content)

    return True

def update_metadata_file(file_list, metadata_file_path):
    file_list.sort()

    metadata = {}
    metadata.setdefault("files", file_list)
    # agregar al archivo
    with open(metadata_file_path, 'w+') as f:
        f.write(json.dumps(metadata, indent=1))

    return True

def get_data_files(data_folder_path):
    extension = '.json'

    # Si se define una carpeta vacia, inicia desde la carpeta actual
    files = [f for f in
             glob.glob(data_folder_path + "**/*" + extension, recursive=True)]
    file_list = []

    for file in files:
        # Construye el archivo json de la metadata
        filename = os.path.basename(file)
        file_list.append(filename)

    file_list.sort()
    return file_list


def get_current_files(metadata_file_path):
    with open(metadata_file_path) as json_file:
        data = json.load(json_file)
        return data['files']


if __name__ == '__main__':

    ## Algorithm
    # 1. Leer la informacion actual del metadata y la lista de archivos
    # 2. Leer todos los archivos de la carpeta `/tricks`
    # 3. Identificar los archivos nuevos
    # 4. Actualizar los necesarios en metadata (solo lo nuevo)
    # 5. Actualizar el nuevo contenido de README (solo no nuevo)

    # Constants
    DATA_FOLDER_PATH = 'tricks'
    README_FILE_PATH = 'README.md'
    METADATA_FILE_PATH = os.path.join(DATA_FOLDER_PATH, '000_metadata.json')

    # 1. Leer la informacion actual del metadata y la lista de archivos
    list_current_files = get_current_files(
        metadata_file_path=METADATA_FILE_PATH)
    print("Archivos actuales:" + str(list_current_files))

    # 2. Leer todos los archivos de la carpeta `/tricks`
    list_updated_files = get_data_files(data_folder_path=DATA_FOLDER_PATH)
    print("Actualizando archivos: " + str(list_updated_files))

    # 3. Identificar los archivos nuevos
    list_new_files = (list(set(list_updated_files) - set(list_current_files)))
    print("Nuevos archivos: " + str(list_new_files))

    # 4. Actualizar los necesarios en metadata (solo lo nuevo)
    if list_new_files:
        status = update_metadata_file(file_list=list_updated_files,
                             metadata_file_path=METADATA_FILE_PATH)
        print("Archivo de metadata actualizado: " + str(status))

    if list_new_files:
        # 5. Actualizar el nuevo contenido de README (solo no nuevo)
        status = update_readme_file(new_file_list=list_new_files,
                           data_folder_path=DATA_FOLDER_PATH,
                           readme_file_path=README_FILE_PATH)
        print("Archivo README actualizado: " + str(status))
