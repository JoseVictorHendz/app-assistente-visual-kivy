# coding: utf-8
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
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.network.urlrequest import UrlRequest
from plyer import camera


class ApiReconhecimentoObjeto:
    print("class------------")

    def make_request(self):
        print("make_request------------")

        UrlRequest('https://api-gcv-python.herokuapp.com/retornoApiGoogleVision', self.print_json)

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
        UrlRequest('https://api-gcv-python.herokuapp.com/retornoApiGoogleVision', self.print_json)

    def print_json(self, req, result):
        #
        # for resultado in result:
        #     self.ids.menssagem1.text = resultado
        #     print resultado

        self.ids.menssagem1.text = result[0]
        self.ids.menssagem2.text = result[1]
        self.ids.menssagem3.text = result[2]
        # self.ids.menssagem4.text = result[3]
        # self.ids.menssagem5.text = result[4]
        # self.ids.menssagem6.text = result[5]
        # self.ids.menssagem7.text = result[6]
        # self.ids.menssagem8.text = result[7]
        # if result[8]:
        #     print result[8]

        #     self.ids.menssagem9.text = result[8]
        # self.ids.menssagem10.text = result[9]



if __name__ == '__main__':
    CameraDemoApp().run()
