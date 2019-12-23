
from bs4 import BeautifulSoup
from twilio.rest import Client
from flask import request


url = 'https://www.amazon.ca/fire-tv-cube/dp/B07M5M7W4K/ref=sr_1_6?keywords=Amazon&qid=1577057615&smid=A3DWYIK6Y9EEQB&sr=8-6'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}


def check_price():

	page = requests.get(URL, headers=headers)

	soup = BeautifulSoup(page.content, 'html.parser')

	price = soup.find(id="priceblock_dealprice").get_text()
	converted_price = float(price[0:5])

	if(converted_price<1.00):
		send_sms()


def send_sms():


	account_sid = '[twilio id]' # Found on Twilio Console Dashboard
	auth_token = '[twilio token]' # Found on Twilio Console Dashboard

	myPhone = '[number]' # Phone number you used to verify your Twilio account
	TwilioNumber = '+12512946927' # Phone number given to you by Twilio

	client = Client(account_sid, auth_token)


	client.messages.create(
	to=myPhone,
	from_=TwilioNumber,
	body='Price has dropped for the Amazon Fire TV! Check the link: https://www.amazon.ca/fire-tv-cube/dp/B07M5M7W4K/ref=sr_1_6?keywords=Amazon&qid=1577057615&smid=A3DWYIK6Y9EEQB&sr=8-6')
