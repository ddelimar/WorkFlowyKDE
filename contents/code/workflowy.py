#!/usr/bin/env python

import sys

from PyKDE4.kdecore import *
from PyKDE4.kdeui import *

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
from PyQt4.QtNetwork import *

## The CookieJar class inherits QNetworkCookieJar to make a couple of functions public. (http://thread.gmane.org/gmane.comp.python.pyqt-pykde/16606/focus=16608)
class CookieJar(QNetworkCookieJar):
	def __init__(self, parent=None):
		QNetworkCookieJar.__init__(self, parent)

	def allCookies(self):
		return QNetworkCookieJar.allCookies(self)
	
	def setAllCookies(self, cookieList):
		QNetworkCookieJar.setAllCookies(self, cookieList)

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


#############

#	def __init__(self, parent, model, attrs={}):
#	def __init__(self, parent=None):
#		AbstractFieldWidget.__init__(self, parent, model, attrs)
#		WebFieldWidgetUi.__init__(self)
#		self.setupUi( self )
		self.cookieJar = CookieJar()
		self.web.page().networkAccessManager().setCookieJar( self.cookieJar )

	def store(self):
		pass

	def clear( self ):
		self.web.setUrl(QUrl('http://workflowy.com/'))

	def showValue(self):
		self.web.setUrl(QUrl(self.record.value(self.name) or ''))

	def setReadOnly(self, value):
		# We always enable the browser so the user can use links.
		self.web.setEnabled( True )

#############

	def saveState(self):
		cookieList = self.cookieJar.allCookies()
		raw = []
		for cookie in cookieList:
			# We don't want to store session cookies
#			if cookie.isSessionCookie():
#				continue
			# Store cookies in a list as a dict would occupy
			# more space and we want to minimize network bandwidth
			raw.append( [
				str(cookie.name().toBase64()), 
				str(cookie.value().toBase64()), 
				str(cookie.path()),
				str(cookie.domain()),
				str(cookie.expirationDate().toString()),
				str(cookie.isHttpOnly()),
				str(cookie.isSecure()),
			])
		return QByteArray( str( raw ) )

	def restoreState(self, value):
		if not value:
			return
		raw = eval( str( value ) )
		cookieList = []
		for cookie in raw:
			name = QByteArray.fromBase64( cookie[0] )
			value = QByteArray.fromBase64( cookie[1] )
			networkCookie = QNetworkCookie( name, value )
			networkCookie.setPath( cookie[2] )
			networkCookie.setDomain( cookie[3] )
			networkCookie.setExpirationDate( QDateTime.fromString( cookie[4] ) )
			networkCookie.setHttpOnly( eval(cookie[5]) )
			networkCookie.setSecure( eval(cookie[6]) )
			cookieList.append( networkCookie )
		self.cookieJar.setAllCookies( cookieList )
		self.web.page().networkAccessManager().setCookieJar( self.cookieJar )



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
#FieldWidgetFactory.register( 'web', WebFieldWidget )

sys.exit(app.exec_())
