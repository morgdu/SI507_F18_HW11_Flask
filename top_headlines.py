from hw11_secrets import api_key
import requests

from flask import Flask, render_template
app = Flask(__name__)
    
@app.route('/')
def index():    
	return '<h1>Welcome!</h1>'

@app.route('/user/<name>')
def get_headlines(name):
    params = {"api-key": api_key}
    base_url = "https://api.nytimes.com/svc/topstories/v2/technology.json"
    results = requests.get(base_url, params).json()

    # top 5 articles results
    results_lst_of_dics = results["results"][:5]

    articles_lst = []
    # accumulate list of article info
    for d in results_lst_of_dics:
    	article_str = "{} ({})".format(d["title"], d["url"])
    	articles_lst.append(article_str)

    return render_template('list.html', 
        title="Hello, " + name + "!", my_list=articles_lst)

@app.route('/user/<name>/<section>')
def get_headlines_section(name, section):
    params = {"api-key": api_key}
    base_url = "https://api.nytimes.com/svc/topstories/v2/" + section + ".json"
    results = requests.get(base_url, params).json()

    # top 5 articles results
    results_lst_of_dics = results["results"][:5]

    articles_lst = []
    # accumulate list of article info
    for d in results_lst_of_dics:
    	article_str = "{} ({})".format(d["title"], d["url"])
    	articles_lst.append(article_str)

    return render_template('list2.html', 
        title = "Hello, " + name + "!", section=section, my_list=articles_lst)


if __name__ == '__main__':  
	print('starting Flask app', app.name)  
	app.run(debug=True)










