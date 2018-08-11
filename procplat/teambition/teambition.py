# -*- coding: utf-8 -*-
import requests

teambition_url = "https://account.teambition.com"

class OAuth():
	# default yangfan's app ploss.
	client_key = 'd3eabb20-9941-11e8-8b8f-bfa3423606b3'
	client_secret = '54e06982-8cc5-4075-81ad-a6957c2b8e6d'
	redirect_uri = 'http://118.24.212.138:80/teambition_redirect'

	def __init__(self, client_key, client_secret, redirect_uri):
		self.client_key = client_key
		self.client_secret = client_secret
		self.redirect_uri = redirect_uri

	def Authorize():
		uri = "/oauth2/authorize"
		r
