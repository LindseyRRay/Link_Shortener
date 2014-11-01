from flask import *
import shorten_link as sl
import json

#Set up App
app = Flask(__name__)
app.debug = True

#Set up Link History Dictionary
short_url=""

shorten_dict = sl.LinkDict()
# Serving the home page.
@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

#Getting the URL to shorten
@app.route("/", methods=["POST"])
def URL_request():
	long_url=request.form['url_to_change']
	short_url = shorten_dict.return_URL(long_url)
	print(short_url)
	return short_url
	#return redirect(new)

@app.route('/test')
def index():
	#new=shorten_dict.link_dict[short_url]
	#print(new)
	return redirect(new, 304)


if __name__ == '__main__':
    app.run(port = 5000)