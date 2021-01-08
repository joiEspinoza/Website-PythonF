#inicializacion FrameWork

from flask import Flask, render_template
app = Flask( __name__ )

##--------------------------------->
#rutas


@app.route( "/" )
def home():
    return render_template( "index.html" )
    #renderiza html

##------------------------------------->


@app.route( "/about" )
def about():
    return render_template( "about.html" )

##------------------------------------->
#Establece el index como arranque (archivo ejecucion)

if __name__ == "__main__":
    app.run( debug = True )
    #debug = true --> pasa a dev - cambios en tiempo real
