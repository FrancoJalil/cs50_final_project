from flask import Flask, render_template, request, Response, redirect, make_response
from bs4 import BeautifulSoup
from flask_cors import CORS, cross_origin
import requests

app = Flask(__name__)

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

@app.route("/", methods=["GET", "POST"])
@cross_origin()
def index():

	return render_template("index.html")


@app.route("/get_scrap", methods=["GET", "POST"])
@cross_origin()
def get_scrap():

	if request.method == "GET":

		command = request.args.get('command')

		if command:
			split_command = command.split()
		else:
			return Response("User error: command failed", status=404, mimetype="text/html")

		if command == '/docs':
			with open('docs.html') as txt:
				return Response(txt.read(), mimetype="text/html")

		export_re = 'export="'

		if split_command[0] in ['/scrap', '/export'] and (len(split_command) == 3 or len(split_command) == 4):
			attrs = scrap_validate(command, split_command, len(split_command))

		else:
			return Response("User error: command failed", status=404, mimetype="text/html")

		try:
			list_of_text_attrs = [attr.text for attr in attrs]
		except:
			return Response("User error: class or id failed", mimetype="text/html")

		if split_command[0] == '/export':
			try:
				if len(list_of_text_attrs) != 0:			
					txt = "\n".join(list_of_text_attrs)
					return Response(txt, mimetype="text/plain", headers={"Content-Disposition":"attachment; filename=export.txt"})
				return Response("User error: command failed", status=404, mimetype="text/html")
			except:
				return Response("HTTP Error", status=404, mimetype="text/plain", headers={"Content-Disposition":"attachment; filename=export.txt"})

		# Show into the web JS
		txt = "<br>".join(list_of_text_attrs)
		if txt == "":
			return Response("User error: missing commands<br>Check /docs", status=404, mimetype="text/plain", headers={"Content-Disposition":"attachment; filename=export.txt"})

		return Response(txt, mimetype="text/html")

if __name__ == "__main__":
	app.run(debug=True, port=8000)