import os
import urllib.request as request 
from zipfile import ZipFile
from deepClassifier.entity import DataIngestionConfig
from deepClassifier import logger
from deepClassifier.utils import get_size
from tqdm import tqdm
from pathlib import Path

class DataIngestionComponent:
    def __init__(self, config: DataIngestionConfig):
        try:
            self.config = config
        except Exception as e:
            raise e 

    def download_file(self):
        logger.info(f'Downloading from - {self.config.source_URL}')
        try:
            if not os.path.exists(self.config.local_data_file):
                logger.info('Download Started...')
                filename, headers = request.urlretrieve(
                    url = self.config.source_URL,
                    filename=self.config.local_data_file
                )
                logger.info(f"{filename} downloaded with following info: \n{headers}")
            else:
                logger.info(f'File already exists of size: {get_size(Path(self.config.local_data_file))}')
        except Exception as e:
            raise e  
        
    def _get_updated_list_of_files(self,list_of_files):
        try:
            return [file for file in list_of_files if file.endswith(".jpg") and ('Cat' in file or 'Dog' in file)] 
        except Exception as e:
            raise e 
        
    def _preprocess(self, zf: ZipFile, file: str, working_dir):
        try:
            target_file_path = os.path.join(working_dir, file) 

            if not os.path.exists(target_file_path):
                zf.extract(file, working_dir)

            #remove file with size 0
            if os.path.getsize(target_file_path) == 0:
                logger.info(f'Removing file in: [{target_file_path}] of size: {get_size(Path(target_file_path))}')
                os.remove(target_file_path)
                
        except Exception as e:
            raise e

    def unzip_and_clean(self):
        logger.info('Unzipping file and removing unwanted files...')
        try:
            with ZipFile(file=self.config.local_data_file,mode = 'r') as zf:
                list_of_files = zf.namelist()
                updated_list_of_files = self._get_updated_list_of_files(list_of_files) 
                for file in tqdm(updated_list_of_files):
                    self._preprocess(zf, file, self.config.unzip_dir)
            
        except Exception as e:
            raise e  