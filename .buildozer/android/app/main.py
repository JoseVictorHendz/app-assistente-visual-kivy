#coding: utf-8
'''
Basic camera example
Default picture is saved as
/sdcard/org.test.cameraexample/enter_file_name_here.jpg
'''

from os import getcwd
from os.path import exists
from os.path import splitext

import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from plyer import camera

#google api

import io
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="apikey.json"
# from google.cloud import vision
# from google.cloud.vision import types


class ReconheceObjeto():
    def __init__(self, caminho):
        self.caminho = caminho
    def reconhecerObjeto(self):
        # Instantiates a client
        client = vision.ImageAnnotatorClient()

        # The name of the image file to annotate
        file_name = os.path.join(
            os.path.dirname(__file__),
            self.caminho)

        # Loads the image into memory
        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)

        # Performs label detection on the image file
        response = client.label_detection(image=image)
        labels = response.label_annotations

        print('Labels:')
        for label in labels:
            print(label.description)


class CameraDemo(FloatLayout):
    def __init__(self):
        super(CameraDemo, self).__init__()
        self.cwd = getcwd() + "/"
        # self.ids.path_label.text = self.cwd

    def tirarFoto(self):
        filepath = self.cwd + self.ids.filename_text.text
        ext = splitext(filepath)[-1].lower()

        if(exists(filepath)):
            popup = MsgPopup("Ja existe uma foto com este nome!")
            popup.open()
            return False

        try:
            print("top------------")
            camera.take_picture(filename=filepath,
                                on_complete=self.retornoCamera)
        except NotImplementedError:
            popup = MsgPopup(
                "nao tem suporte para esta plataforma")
            popup.open()

    def retornoCamera(self, filepath):
        if(exists(filepath)):
            popup = MsgPopup("Foto salva!")
            popup.open()
        else:
            popup = MsgPopup("nao foi possivel salvar" + filepath)
            popup.open()


class CameraDemoApp(App):
    print("-------------------------", )
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
        self.ids.menssagem.text = msg


if __name__ == '__main__':
    CameraDemoApp().run()
























# from kivy.app import App
# from kivy.uix.label import Label
#
#
# def build():
#     return Label(text = 'Ola mundo')
#
# hello_horld = App()
# hello_horld.build = build
# hello_horld.run()