import os
import requests

class BandClient:
    def __init__(self):
        self.api_key = os.getenv("BAND_API_KEY")
        self.room_id = os.getenv("BAND_ROOM_ID")
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def post_to_room(self, payload):
        if not self.room_id:
            print("❌ ERROR: BAND_ROOM_ID is not set in your .env file!")
            return None
            
        url = f"https://api.band.ai/v1/rooms/{self.room_id}/messages"
        print(f"📡 Debug: SecurityEngineer attempting to POST to: {url}")
        
        response = requests.post(url, json=payload, headers=self.headers)
        
        if response.status_code == 404:
            print(f"❌ 404 Client Error: The room ID '{self.room_id}' was not found by Band.ai.")
        
        response.raise_for_status()
        return response.json()