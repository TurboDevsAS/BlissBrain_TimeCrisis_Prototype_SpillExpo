# -*- coding: utf-8 -*-
##
## Importing functions from kivy
##
import kivy
kivy.require ( '1.0.6' )
from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.widget import Widget
##
## Importing the PyEpoc wrapper class in order to use the Emotiv SDK libraries 
##
from PyEpoc import *

##
## Importing ctypes and .dll for the usb-relay
## and also fetching id's for the device, and opening the device.
##

import ctypes
test = ctypes.cdll.LoadLibrary('C:\Program Files (x86)\Emotiv EPOC Control Panel v2.0.0.20\Applications\usb_relay_device.dll')
test.usb_relay_init()
x = None;
x = test.usb_relay_device_enumerate()
y = None;
id1 = x;
y = test.usb_relay_device_open(id1)
test.usb_relay_device_open(id1)

##
## Connecting to the Emotiv SDK libraries
##

EmotivEngine 	= EpocHandler ( )
choice			= str ( )
ee_handle		= EmotivEngine.EE_EmoEngineEventCreate ( )
s_handle		= EmotivEngine.EE_EmoStateCreate ( )

EmotivEngine.ES_Init ( s_handle )

##
## If emocomposer is to be used, set port to 1726
## If EPOC Control Panel with the EPOC EEG headset is to be used, set port to 3008 
##

#EmotivEngine.EE_EngineRemoteConnect ( '127.0.0.1', 1726 )
EmotivEngine.EE_EngineRemoteConnect ( '127.0.0.1', 3008 )

##
## Define a class for image handler. This class handles the image thats indicates the state of Emotiv.
##

class Imglayout ( FloatLayout ):
	def __init__ ( self, **args ):
		super ( Imglayout, self ).__init__ ( **args )

		with self.canvas.before:
			Color ( 1, 1, 1, 1 )
			self.rect	= Rectangle ( size=self.size, pos=self.pos )

		self.bind ( size=self.updates, pos=self.updates )

	def updates ( self, instance, value ):
		self.rect.size =instance.size
		self.rect.pos  =instance.pos

##
## In this class, we use the connection to the Emotiv SDK library to check which blissymbol the user thinks about
## If the user thinks about a blisssymbol, the window for blissymbols will be updated with the picture of the blissymbol.
##

class EEGBliss ( App ):

##
## We define a blank picture for when the user doesn't think about a blissymbol
##

	i_handle	= Image ( source = 'blank.png' )
	_state		= False

##
## Here kivy performs the building of the application from the classes and layouts we have defined.
##

	def build ( self ):
		i_layout	= Imglayout ( )
		i_layout.add_widget ( self.i_handle )
		b_layout	= BoxLayout ( orientation='vertical' )
		b_layout.add_widget ( i_layout )

##
## Here we define the time-interval between each check for which blissymbol the user is thinking about.
## The check has been instructed to run every 5 milliseconds.
##

		m = EEGBliss()
		Clock.schedule_interval ( m.update , .005 )

##
## Rules for displaying the image of the current blissymbol.
##

		self.i_handle.keep_ratio    = True
		self.i_handle.allow_stretch = False
		return b_layout;

##
## Callback function that's change the image.
##

	def callback ( self, i_source ):
		self.i_handle.source = i_source;
		self.i_handle.reload ( )

##
## Three wrapper for the callback function. The state of the emotiv decides
## which of the wrapper is triggered.
##

	def cb_negative ( self ):
		self.callback ( 'crouch.png' )

	def cb_neutral ( self ):
		self.callback ( 'stand.png' )

	def cb_positive ( self ):
		self.callback ( '' )

##
## Getter and setter for the _state property. The setter triggers the wrappers for the callback function.
##

	@property
	def state ( self ):
		return self._state

	@state.setter
	def state ( self, value ):
		self._state = value

##
## Here we perform if-tests for which blissymol the user is currently thinking about.
## We have defined tests against though-ID 1, 8 and 16 from the Emotiv SDK library-
## If the thought-ID 1, 8 or 16 is thought by the user, it will activate one of the triggers defined earlier.
## 

		
		if ( self._state == 16 ):
			self.cb_negative ( )
			print "State er negativ!"
			test.usb_relay_device_close_one_relay_channel(y,1)

		elif ( self._state == 8 ):
			self.cb_positive ( )
			print "State er positiv!"

		elif ( self._state == 1 ):
			self.cb_neutral ( )
			print "State er neutral!"
			test.usb_relay_device_open_one_relay_channel(y,1)

##
## We define a check that updates on a given interval to see if the user is thinking about a blissymbol.
##

	def update (self, t):
		e_status = EmotivEngine.EE_EngineGetNextEvent ( ee_handle )

##
## Checking for errors from the Emotiv SDK libraries.
##   

		if ( e_status == ERRCODE [ 'EDK_OK' ]):
				e_handle = EmotivEngine.EE_EmoEngineEventGetType ( ee_handle )
				e_user   = EmotivEngine.EE_EmoEngineEventGetUserId ( ee_handle )[ 1 ]
				
				if ( e_handle == EVENT [ 'EE_EmoStateUpdated' ]):
					EmotivEngine.EE_EmoEngineEventGetEmoState ( ee_handle, s_handle )
##
## Gets the current state of emotiv
##

					
		self.state  = EmotivEngine.ES_CognitivGetCurrentAction ( s_handle )
		
		EmotivEngine.ES_CognitivGetCurrentActionPower ( s_handle )

if ( __name__ == '__main__' ):
	EEGBliss ( ).run ( )
