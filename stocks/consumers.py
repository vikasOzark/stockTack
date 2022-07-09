import json
from channels.generic.websocket import WebsocketConsumer

class StockUpdate(WebsocketConsumer):
    def connect(self):
        print('connected to the page it self')
        self.accept()

    def disconnect(self, close_code):
        print('disconnect!')
        

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': 'hello from the other side'
        }))