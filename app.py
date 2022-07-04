# import os
# import json
# #import helper functions for magiceden
# import magiceden
# #import helper functions for monkeylabs
# import monkelabs


from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def home():
     return render_template('index.html')


@app.route('/hello/')
@app.route('/mint')

def mint():

    def getConfig():
        configFile = open("config.json", 'r')
        return list(json.load(configFile).values())


    #gets config
    config = getConfig()

    #if windows True, else False (mac, linux)
    isWindows = True if os.name == 'nt' else False

    #if mint on magiceden.io
    if "magiceden.io" in config[0]:
        print("Found magiceden.io link")
        magiceden.mint(config, isWindows)
        
    #if mint on monkeylabs.io
    elif "monkelabs.io" in config[0]:
        print("Found monkelabs.io link")
        monkelabs.mint(config, isWindows)

    #if platform not supported
    else:
        print("Could not recognize link")

    return render_template('mint.html')

if __name__ == "__main__":
    app.run(debug=True)