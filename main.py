from os import getcwd
from os.path import exists
from os.path import splitext
from base64 import b64encode
from json import dumps
import requests, json

import os
import io

import kivy

kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.network.urlrequest import UrlRequest
from plyer import camera


class ApiReconhecimentoObjeto:
    print("class------------")
    encoded_string = ''
    # # The name of the image file to annotate
    # file_name = os.path.join(
    #     os.path.dirname(__file__),
    #     './arroz.jpg')
    #
    # # Loads the image into memory
    # with io.open(file_name, 'rb') as image_file:
    #     content = image_file.read()
    #
    # top = content
    #
    # with open('./arroz.jpg', "rb") as image_file:
    #     encoded_string = base64.b64encode(image_file.read())
    #
    # print(encoded_string, encoded_string)

    def make_request(self):

        UrlRequest.get('http://0.0.0.0:5000/retor/', self.print_json)

    def print_json(self, req, result):
        for resultado in result:
            print resultado


class CameraDemo(FloatLayout):
    def __init__(self):
        super(CameraDemo, self).__init__()
        self.cwd = getcwd() + "/"
        # self.ids.path_label.text = self.cwd

    def tirarFoto(self):
        filepath = self.cwd + self.ids.filename_text.text
        ext = splitext(filepath)[-1].lower()

        if (exists(filepath)):
            popup = MsgPopup("Ja existe uma foto com este nome!")
            popup.open()
            return False

        try:
            camera.take_picture(filename=filepath,
                                on_complete=self.retornoCamera)
        except NotImplementedError:
            popup = MsgPopup(
                "nao tem suporte para esta plataforma")
            popup.open()

    def retornoCamera(self, filepath):
        if (exists(filepath)):
            popup = MsgPopup("Foto salva!")
            popup.open()
        else:
            popup = MsgPopup("nao foi possivel salvar" + filepath)
            popup.open()


class CameraDemoApp(App):

    def __init__(self):
        super(CameraDemoApp, self).__init__()
        self.demo = None

    def build(self):
        self.demo = CameraDemo()
        return self.demo

    def on_pause(self):
        return True

    def on_resume(self):
        pass


class MsgPopup(Popup):
    def __init__(self, msg):
        super(MsgPopup, self).__init__()


        #
        # # The name of the image file to annotate
        # file_name = os.path.join(
        #     os.path.dirname(__file__),
        #     './arroz.jpg')
        #
        # # Loads the image into memory
        # with io.open(file_name, 'rb') as image_file:
        #     imagem = image_file.read()

        ENCODING = 'utf-8'
        IMAGE_NAME = './urso.jpg'
        # JSON_NAME = 'output.json'

        # first: reading the binary stuff
        # note the 'rb' flag
        # result: bytes
        with open(IMAGE_NAME, 'rb') as open_file:
            byte_content = open_file.read()

        base64_bytes = b64encode(byte_content)

        base64_string = base64_bytes.decode(ENCODING)



        response = requests.post('http://0.0.0.0:5000/retornoApiGoogleVision', json={"img": base64_bytes})

        comments = json.loads(response.content)
        self.print_json(comments)

    def print_json(self, result):
        resultado = []
        tamanho = len(result)
        for response in result:
            resultado.append(response)

        if tamanho >= 1:
            self.ids.menssagem0.text = resultado[0]
        if tamanho >= 2:
            self.ids.menssagem1.text = resultado[1]
        if tamanho >= 3:
            self.ids.menssagem2.text = resultado[2]
        if tamanho >= 4:
            self.ids.menssagem3.text = resultado[3]
        if tamanho >= 5:
            self.ids.menssagem4.text = resultado[4]
        if tamanho >= 6:
            self.ids.menssagem5.text = resultado[5]
        if tamanho >= 7:
            self.ids.menssagem6.text = resultado[6]
        if tamanho >= 8:
            self.ids.menssagem7.text = resultado[7]
        if tamanho >= 9:
            self.ids.menssagem8.text = resultado[8]
        if tamanho >= 10:
            self.ids.menssagem9.text = resultado[9]



if __name__ == '__main__':
    CameraDemoApp().run()
