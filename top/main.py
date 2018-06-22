from kivy.network.urlrequest import UrlRequest
from kivy.app import App
from kivy.uix.button import Button



class reqApp(App):
    def build(self):
        bt =  Button(text='Pegar Json do Bitcoin')
        bt.bind(on_press=self.make_request)
        return bt

    def make_request(self, instance):
        UrlRequest('https://api-gcv-python.herokuapp.com/retornoApiGoogleVision', self.print_json)

    def print_json(self, req, result):
        for resultado in result:
            print resultado

if __name__ == '__main__':
    reqApp().run()