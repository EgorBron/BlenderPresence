import pypresence
import threading
import time
import bpy
import jinja2
import typing

VERSION = 'v0.0.1.fuck'
class BlenderPresence():
    def __init__(self, bpy, *, app_id = 922018802168889394):
        self.lastActivity = {'obj': '', 'objsel': ''}
        self.started = round(time.time())
        self.pypr = pypresence.Presence(app_id)
        self.details = "Working at \"{scene}\" scene with size {sceneSize}"
        self.state = 'Current object: {currentObject}'
        self.large_image_text = '{mode} mode'
        self.small_image_text = 'BlenderPresence {libVersion}'
        self.large_image = '{modeCode}'
        self.small_image = '{logoCode}'
        self.logo_code = '1'
        

#    def buildButtons(self):
#            buttons = []
#            if self.button1Text and self.button1URL:
#                buttons.append({"label": self.button1Text, "url": self.button1URL})
#            if self.button2Text and self.button2URL:
#                buttons.append({"label": self.button2Text, "url": self.button2URL})
#            buttons = buttons or None
#            return buttons

    def __mode_сode(self, mode: str):
        # потом сделать настройку этого через передачу функции:
#        def mode_filter(mode):
#            if mode == 'MODE':
#                return '0'
        return '3' if mode == 'OBJECT' else '4' if mode == 'EDIT_MESH' else '5' if mode == 'SCULPT' else '6' if mode == 'PAINT_VERTEX' else '7' if mode == 'PAINT_WEIGHT' else '8' if mode == 'POSE' else '0'

    def __render_text(self, text, **kwargs):
        return jinja2.Template(text, variable_start_string="{", variable_end_string="}").render(**kwargs)

    def config(self, *, details = None, state = None, large_image_text = None, small_image_text = None, large_image = None, small_image = None, mode_code_processor = None, logo_code = None):
        # ну чё народ, погнали нафиг! грёбаный рот!
        self.details = details or self.details
        self.state = state or self.state
        self.large_image_text = large_image_text or self.large_image_text
        self.small_image_text = small_image_text or self.small_image_text
        self.large_image = large_image or self.large_image
        self.small_image = small_image or self.small_image
        self.__code_processor = mode_code_processor or getattr(self, '_BlenderPresence__code_processor', None) or self.__mode_сode
        self.logo_code = logo_code or self.logo_code
        
    def updateRPC(self):
        # while 1:
        #     time.sleep(0.1)
        C = bpy.context
        D = bpy.data
        formatter = {
            'currentObject': C.selected_objects[0].data.name,
            'totalObjects': len(D.objects),
            'projectSize': C.scene.statistics(C.view_layer).split('|')[6].split(':')[1].strip(),
            'scene': C.scene.name,
            'workspace': C.workspace,
            'mode': " ".join(C.mode.capitalize().split('_')),
            'modeCode': self.__code_processor(C.mode),
            'libVersion': VERSION,
            'logoCode': self.logo_code
        }
        self.pypr.update(details=self.__render_text(self.details, **formatter), state=self.__render_text(self.state, **formatter), large_image=self.__render_text(self.large_image, **formatter), large_text=self.__render_text(self.large_image_text, **formatter), small_image=self.__render_text(self.small_image, **formatter), small_text=self.__render_text(self.small_image_text, **formatter), start=self.started, instance=False)
                
    def run(self):
#        time.sleep(10)
        self.pypr.connect()
        self.config()
        self.updateRPC()
        # threading.Thread(target = self.updateRPC).run()
        print('ready')



bpr = BlenderPresence(bpy)
bpr.config()
bpr.run()