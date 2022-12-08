from flask import Flask, render_template, request, Response, redirect, make_response
from flask_cors import CORS, cross_origin
from helpers import scrap_validate, http_return_error

app = Flask(__name__)


@app.route("/")
@cross_origin()
def index():

	return render_template("index.html")


@app.route("/get_scrap")
@cross_origin()
def get_scrap():

	if request.method == "GET":

		command = request.args.get('command')

		## INPUT VALIDATIONS
		if command:
			split_command = command.split()
		else:
			return http_return_error("User error: not input command")

		## DOCS
		if command == '/docs':
			with open('docs.html') as txt:
				return Response(txt.read(), mimetype="text/plain")

		## INPUT VALIDATIONS
		if split_command[0] in ['/scrap', '/export'] and (len(split_command) == 3 or len(split_command) == 4):

			# scrape
			attrs = scrap_validate(command, split_command, len(split_command))

		else:
			return http_return_error("User error: command failed <br>/docs")

		## LIST OF ATTRS
		try:
			list_of_text_attrs = [attr.text for attr in attrs]

		except:
			return http_return_error("User error: class or id failed")


		## EXPORT
		if split_command[0] == '/export':
			try:
				if len(list_of_text_attrs) != 0:
					# TODO...

					txt = "\n".join(list_of_text_attrs)
					return Response(txt, mimetype="text/plain", headers={"Content-Disposition":"attachment; filename=export.txt"})
				return http_return_error("User error: command failed")

			except:
				return http_return_error("HTTP Error")
				

		## Show into the web JS
		txt = "<br>".join(list_of_text_attrs)
		if txt == "":
			return http_return_error("User error: missing commands<br>Check /docs")

		return Response(txt, mimetype="text/html")

if __name__ == "__main__":
	app.run(debug=True, port=8000)