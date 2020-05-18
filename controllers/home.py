
'''
Preset controller by torn for / route
'''
from .modules import *
__UPLOADS__="uploads"

class Upload(tornado.web.RequestHandler):
    def get(self):
        self.write("""<form 
                    enctype="multipart/form-data" action="/upload" method="POST"> 
                    <input type='file' name="f">
                    <button type"submit >send</button>""")
        
    def post(self):
        FileInfo=self.request.files['f'][0]
        FileName=FileInfo["filename"]
        with open(__UPLOADS__+'/'+FileName,'wb') as file:
            file.write(FileInfo['body'])

class Download(tornado.web.RequestHandler):
        def get(self,name):
                if name:
                    FileName=name.replace('/','')
                    self.set_header('Content-Type','appliacation/force-download')
                    self.set_header(f'Content-Disposition','attachment;filename={FileName}')
                    with open(__UPLOADS__+'/'+FileName,'rb') as file:
                            self.write(file.read())
                else:
                    self.write('[Wrong entry point argument]: Pass file_name in requested url ( /download/file_name )')
           