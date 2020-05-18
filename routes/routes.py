
from controllers import *
from tornado.web import url
route = [
		url(
			r"/upload",
			home.Upload
		),
		url(
			r"/download/"+r"(.*)",
			home.Download
		
		)
]
					