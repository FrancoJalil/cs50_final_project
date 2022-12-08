from flask import Response
from bs4 import BeautifulSoup
import requests

def scrap_validate(command, split_command, length):
	
	url = split_command[1]

	if not "https://" in url:
		url = "https://" + url
		
	html_attr = split_command[2]

	try:
		result = requests.get(url)

	except:
		return Response("User error: URL FAIL", status=404, mimetype="text/html")

	content = result.text

	soup = BeautifulSoup(content, 'lxml')

	if length == 4:
		has_class = 'class="' in command
		has_id = 'id="' in command

		# if class
		if has_class:
			html_class = split_command[3][7:-1]
			attrs = soup.find_all(html_attr, class_=html_class)
			return attrs

		# if id
		elif has_id:
			html_id = split_command[3][4:-1]
			attrs = soup.find_all(html_attr, id=html_id)
			return attrs

		else:
			return Response("User error: class or id", status=404, mimetype="text/html")

	# if just attrs
	attrs = soup.find_all(html_attr)
	return attrs


def http_return_error(error, status_code=404):
	
	return Response(error, status=status_code, mimetype="text/html")