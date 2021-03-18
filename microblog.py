from flask import Flask

app = Flask("microblog")

#
@app.route("/")
def index ():
    return "Ola, Mundo!"

app.run()    # executa todo o comando