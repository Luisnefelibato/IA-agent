import requests

class DataCollector:
    def __init__(self, api_key):
        self.api_key = api_key  # Clave de API para autenticación

    def search_talent_on_platform(self, platform_url, query):
        """
        Busca talentos en una plataforma externa usando su API.
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        params = {"q": query}
        response = requests.get(platform_url, headers=headers, params=params)
        
        if response.status_code == 200:
            return response.json()  # Devuelve los datos en formato JSON
        else:
            raise Exception(f"Error fetching data from {platform_url}: {response.status_code}")

    def collect_data(self):
        """
        Recopila datos de múltiples plataformas.
        """
        print("Collecting data from institutions...")
        platforms = [
            {"url": "https://api.art-schools.com/talent", "query": "music"},
            {"url": "https://api.modeling-agencies.com/talent", "query": "modeling"},
        ]
        
        raw_data = []
        for platform in platforms:
            try:
                data = self.search_talent_on_platform(platform["url"], platform["query"])
                raw_data.extend(data)
            except Exception as e:
                print(f"Error: {e}")
        
        return raw_data
class DataCollector:
    def collect_data(self):
        # Simulate data collection from various sources
        print("Collecting data from institutions...")
        # Example: Scraping websites, APIs, databases, etc.
        raw_data = [
            {"name": "Luis Gomez ", "email": "luisgo@example.com", "phone": "123-456-7890", "talent": "music"},
            {"name": "Juanito perez", "email": "juanitope@example.com", "phone": "987-654-3210", "talent": "acting"},
        ]
        return raw_data