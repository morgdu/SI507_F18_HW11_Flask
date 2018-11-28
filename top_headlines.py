from hw11_secrets import api_key
import requests
import datetime

from flask import Flask, render_template
app = Flask(__name__)

# home page    
@app.route('/')
def index():    
	return '<h1>Welcome!</h1>'

# page for only user name provided
@app.route('/user/<name>')
def get_headlines(name):
    
    # get NY times data
    params = {"api-key": api_key}
    base_url = "https://api.nytimes.com/svc/topstories/v2/technology.json"
    results = requests.get(base_url, params).json()

    # top 5 articles results
    results_lst_of_dics = results["results"][:5]

    # accumulate list of article info
    articles_lst = []
    for d in results_lst_of_dics:
    	article_str = "{} ({})".format(d["title"], d["url"])
    	articles_lst.append(article_str)

    # check what time of day, set greeting accordingly
    time = datetime.datetime.now().time()
    if int(str(time)[:2]) < 12:
    	greet = "morning"
    elif int(str(time)[:2]) >= 12 and int(str(time)[:2]) <= 16:
    	greet = "afternoon"
    elif int(str(time)[:2]) >= 16 and int(str(time)[:2]) <= 20:
    	greet = "evening"
    else:
    	greet = "night"

    return render_template('list.html', name=name, greet=greet, my_list=articles_lst)

# page for user name and section name
@app.route('/user/<name>/<section>')
def get_headlines_section(name, section):

	# get NY Times data
    params = {"api-key": api_key}
    base_url = "https://api.nytimes.com/svc/topstories/v2/" + section + ".json"
    results = requests.get(base_url, params).json()

    # top 5 articles results
    results_lst_of_dics = results["results"][:5]

	# accumulate list of article info
    articles_lst = []
    for d in results_lst_of_dics:
    	article_str = "{} ({})".format(d["title"], d["url"])
    	articles_lst.append(article_str)
	
	# check what time of day, set greeting accordingly
    time = datetime.datetime.now().time()
    if int(str(time)[:2]) < 12:
    	greet = "morning"
    elif int(str(time)[:2]) >= 12 and int(str(time)[:2]) <= 16:
    	greet = "afternoon"
    elif int(str(time)[:2]) >= 16 and int(str(time)[:2]) <= 20:
    	greet = "evening"
    else:
    	greet = "night"

    return render_template('list2.html', name=name, section=section, my_list=articles_lst, greet = greet)


if __name__ == '__main__':  
	print('starting Flask app', app.name)  
	app.run(debug=True)
