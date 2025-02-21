import requests



class APIClient:
    def   __init__(self, url, file_path):
        self.url = url
        self.file_path = file_path

    def fetch_data_from_api(self):
        try:
            r = requests.get(self.url)
            if r.status_code == 200:
                data = r.json()
                with open(self.file_path , 'w') as file:
                    for item in data: 
                        file.write('{}\n'.format(item))
                print('data fetched and saved to {}'.format(self.file_path))
            else:
                print('failed to fetch data: status code {}'.format(r.status_code))
        except:
            print('error')