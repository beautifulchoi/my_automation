import gdown
from requests import get  # to make GET request


def download(url, file_name=None, is_gdrive=False):
    if not file_name:
        file_name = url.split('/')[-1]

    if is_gdrive:
        gdown.download(id=url, output=file_name, quiet=False)  # url in here should be file id(extracted)
    
    else:
        with open(file_name, "wb") as file:   # open in binary mode
            response = get(url)               # get request
            file.write(response.content)      # write to file


if __name__ == '__main__':
    url = "1_1o7Pk7jOD0WxHiFU5YxMymukP0ty3BD"
    download(url, file_name='bouet.zip', is_gdrive=True)