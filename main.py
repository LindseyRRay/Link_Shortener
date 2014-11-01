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
	#return short_url
	return redirect('/short_url/'+short_url)

@app.route('/short_url/<redirect_url>')
def index(redirect_url):
	new=shorten_dict.link_dict[redirect_url]
	#Account for fact that URL might not exist
	print(new)
	print(redirect_url)

	return render_template("index.html", long_url = "http://"+new, short_url=redirect_url )

@app.route('/redirect/<redirect_url>')
def redirect_URL(redirect_url):
	new=shorten_dict.link_dict[redirect_url]
	#Account for fact that URL might not exist
	print(new)
	print(redirect_url)
	return redirect("http://"+new)



if __name__ == '__main__':
    app.run(port = 5000)