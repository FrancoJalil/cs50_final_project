from flask import Flask, render_template, request, Response, redirect, make_response
from bs4 import BeautifulSoup
from io import StringIO
import requests

app = Flask(__name__)


def extract_next(word, command):

	for l in word:
		word = ""
		first = False

		if l == '"' and first == False:
			word += l

		elif first == True:
			return word

	# error, tmp
	print("Missing class or id")
	return redirect('/')

def scrap_validate(command, length):
	
	url = command[1]
		
	html_attr = command[2]

	try:
		result = requests.get(url)
	except:
		print("URL FAIL")
		return redirect('/')

	content = result.text

	soup = BeautifulSoup(content, 'lxml')

	if length == 4:
		has_class = ' class="' in command
		has_id = ' id="' in command

		# if class
		if has_class:
			html_class = extract_next(command[3])
			attrs = soup.find_all(html_attr, class_=html_class)
			return attrs

		# if id
		elif has_id:
			html_id = extract_next(command[3])
			attrs = soup.find_all(html_attr, id=html_id)
			return attrs

		else:
			print("Error class or id")
			return

	# if just attrs
	attrs = soup.find_all(html_attr)
	return attrs

@app.route("/", methods=["GET", "POST"])
def index():

	return render_template("index.html")


@app.route("/get_scrap", methods=["GET", "POST"])
def get_scrap():

	if request.method == "GET":

		command = request.args.get('command')

		command = command.split()

		if command[0] == '/scrap' and (len(command) == 3 or len(command) == 4):
			attrs = scrap_validate(command, len(command))

		else:
			print("3 or 4 command-words")
			return redirect('/')

		try:
			list_of_text_attrs = [attr.text for attr in attrs]
		except:
			print("Error x")
			return redirect('/')

		txt = '\n'.join(list_of_text_attrs)
		print(txt)

		return Response(txt, mimetype="text/plain")


if __name__ == "__main__":
	app.run(debug=True, port=8000)