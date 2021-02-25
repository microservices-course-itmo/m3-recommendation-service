import zipfile
import subprocess
import requests

def unpack(archive_path, path):
    with zipfile.ZipFile(archive_path, 'r') as zip_file:
        zip_file.extractall(path)
        root_folder = zip_file.filelist[0]
    return root_folder.filename



def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

if __name__ == "__main__":
    knn_id ='1XtTA2KJZcJ77gi1LcTRTh5mFTCoLVcQm'
    bert_id = '1rKcJzivRxZADGJLzOJxEEcGvg6dipXfH'

    download_file_from_google_drive(knn_id, '/code/ml/knn.zip')
    unpack('/code/ml/knn.zip', '/code/ml/')

    # download_file_from_google_drive(bert_id, '/code/ml/bert.zip')
    # unpack('/code/ml/bert.zip', '/code/ml/') 
    #TODO remove zips
# knn_id ='1XtTA2KJZcJ77gi1LcTRTh5mFTCoLVcQm'
# bert_id = '1rKcJzivRxZADGJLzOJxEEcGvg6dipXfH'