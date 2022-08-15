# import os
# import json
# #import helper functions for magiceden
# import magiceden
# #import helper functions for monkeylabs
# import monkelabs
import subprocess


from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def home():
     return render_template('index.html')


@app.route('/hello/')
@app.route('/mass')

def mass():

    def to_list(txt_file):
        with open(txt_file,'r') as f:
            listl=[]
            for line in f:
                strip_lines=line.strip()
                # listli=line.split()
                print(strip_lines)
                m=listl.append(strip_lines)
            print(listl)
        return listl

    list1 = to_list('airdrop.txt')

    list2 = to_list('tokens.txt')

    for i in range(len(list1) - 1):
        print("spl-token transfer " + list2[i] + " 0.019 " + list1[i] + " --fund-recipient")
        list_files = subprocess.Popen(
            ["spl-token", "transfer", list2[i], "0.019" , list1[i], "--fund-recipient"])
        list_files.wait()

    return render_template('mass.html')

if __name__ == "__main__":
    app.run(debug=True)