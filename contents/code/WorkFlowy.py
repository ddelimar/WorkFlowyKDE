#!/usr/bin/env python

import sys

from PyKDE4.kdecore import *
from PyKDE4.kdeui import *

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

class WorkFlowyWeb(object):
	def __init__(self):
		self.window = KMainWindow()
		self.widget = QWidget()
		self.window.setCentralWidget(self.widget)

		layout = QVBoxLayout(self.widget)
		
		self.web = QWebView(self.widget)
		self.web.load(QUrl("http://workflowy.com/"))
		layout.addWidget(self.web)
		self.window.show()

appName = "workflowy"
catalog = ""
programName = ki18n("WorkFlowy - Organize your brain.")
version = "1.0"
description = ki18n("A Qt WebKit view of workflowy.com")
license = KAboutData.License_GPL
copyright = ki18n("(c) 2013 Dom Delimar")
text = ki18n("none")
homePage = "domdelimar.com"
bugEmail = "workflowybugs@domdelimar.com"

aboutData = KAboutData (appName, catalog, programName, version, description,
license, copyright, text, homePage, bugEmail)

KCmdLineArgs.init(sys.argv, aboutData)

app = KApplication()
workflowyweb = WorkFlowyWeb()

sys.exit(app.exec_())
