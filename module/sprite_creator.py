import os
import shutil

SPRITES = ['player', 'enemy', 'bullet', 'enemy_bullet']

def CREATE_FOLDER(path, name):
    path = os.path.join(path, name)

    # Создание новой папки
    os.makedirs(path)

    # Создание подпапок внутри новой папки
    sec_fol = ['img', 'script', 'sound']
    for sf in sec_fol:
        path_second_folder = os.path.join(path, sf)
        os.makedirs(path_second_folder)

        if sf == 'script':
            script_file_path = os.path.join(path_second_folder, name + '.py')
            with open(script_file_path, 'w') as script_file:
                script_file.write(f'''
from module.behaviors import*

class {name.upper()}(BEHAVIORS):
    def __init__(self):
        self.size = (64, 64)
        self.color = RED 
        self.rect = p.Rect(
                        SCREENSIZE[0]/2,
                        SCREENSIZE[1]/2,
                        self.size[0],
                        self.size[1]
                        )
        self.image = image_load(os.path.dirname(__file__))
        self.image = p.transform.scale(self.image[0], (self.size[0], self.size[1]))

{name} = {name.upper()}()
''')

        elif sf == 'img':
            # Получение абсолютного пути к файлу 'zaglushka.png'
            current_file_directory = os.path.dirname(__file__)
            img_file_path = os.path.join(current_file_directory, 'zaglushka.png')

            # Копирование изображения в папку 'img'
            shutil.copyfile(img_file_path, os.path.join(path_second_folder, name+'.png'))

    print(f'Папка "{name}" создана в пути: {path}')

# Пример использования функции
FOLDERS = os.listdir(os.path.join(os.path.dirname(__file__), '..', 'obj'))
print(FOLDERS)
for obj in SPRITES:
    if obj in FOLDERS:
        print('yes')
    else:
        CREATE_FOLDER(os.path.join(os.path.dirname(__file__), '..', 'obj'), obj)



script_file_path = os.path.join(os.path.dirname(__file__), '..', 'imports.py')
with open(script_file_path, 'w') as script_file:
    for name in SPRITES:
     script_file.write(f'from obj.{name}.script.{name} import*\n' )