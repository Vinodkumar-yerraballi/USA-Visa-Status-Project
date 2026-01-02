import os
from pathlib import Path

project_name ='USA_Visa'

files_path=[
    f'{project_name}/__init__.py',
    f'{project_name}/componets/__init__.py',
    f'{project_name}/componets/data_ingestion.py',
    f'{project_name}/componets/data_validation.py', 
    f'{project_name}/componets/data_transformation.py',
    f'{project_name}/componets/model_trainer.py',
    f'{project_name}/componets/model_evaluation.py',
    f'{project_name}/componets/model_pusher.py',  
    f'{project_name}/configuration/__init__.py',  
    f'{project_name}/constants/__init__.py',
    f'{project_name}/entity/__init__.py',
    f'{project_name}/entity/config_entity.py',
    f'{project_name}/entity/artifact_entity.py',
    f'{project_name}/exception/__init__.py',
    f'{project_name}/logger/__init__.py',
    f'{project_name}/pipline/__init__.py',
    f'{project_name}/pipline/traing_pipline.py',
    f'{project_name}/pipline/predict_pipeline.py',
    f'{project_name}/utils/__init__.py',
    f'{project_name}/utils/main_utils.py',
    'app.py',
    'requirements.txt', 
    'setup.py',
    'dockerfile',
    '.dockerignore',
    'demo.py',
    'config/model.yaml',
    'config/schema.yaml'
]

for files in files_path:
    filepath=Path(files)
    filedir, filename=os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        print(f"Creating directory: {filedir} for file: {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        print(f"Creating empty file: {filepath}")
    else:
        print(f"File already exists and is not empty: {filepath}")