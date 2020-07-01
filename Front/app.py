from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify, make_response
import os
import sqlite3 as sql
from flask_login import LoginManager
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
import teste as ts
import arvore as arv

app = Flask(__name__)

maxBairro = ts.maximoBairro
maxsemana = ts.semanal
teste = ts.maior.index[0]
#t1= ts.turno1 
#t2= ts.turno2 
#t3= ts.turno3

rotulosTurno = [ 'Manha', 'Tarde','Noite']






#valores = [t1,t2, t3]
labels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
]

values = [
    967.67, 1190.89, 1079.75, 1349.19,
    2328.91, 2504.28, 2873.83, 4764.87,
    4349.29, 6458.30, 9907, 16297
]

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]




@app.route("/create-entry", methods=["POST"])
def create_entry():
    bar_labels = labels
    bar_values = values



    req = request.get_json()
    dia = req['valor3']
    turno = req['valor2']
    bairro = req['valor1']
    #print(dia,turno,bairro)
   # print(req)

    data = [[bairro,turno,dia,'perigoso'],]

    for row in data:
        result = arv.print_leaf(arv.classify(row, arv.my_tree))

       # print(result)
        #print("Actual: %s. Predicted: %s" %
        #      (row[-1], arv.print_leaf(arv.classify(row, arv.my_tree)))
        #      )

    return jsonify(result)
        #res = make_response(jsonify({"message": "OK"}), 200)

        #return res
       # return render_template('principal.html', maximoBairro=maxBairro, maxSemana=maxsemana, maximoTurno=ts.turn, max=17000, labels=bar_labels, values=bar_values,resultado = y )

@app.route('/bar')
def bar():
    bar_labels=labels
    bar_values=values
    return render_template('bar_chart.html', title='Bitcoin Monthly Price in USD', max=17000, labels=bar_labels, values=bar_values)








# Index
@app.route('/')
def index():
    bar_labels=labels
    bar_values=values


    return render_template('principal.html',maximoBairro = maxBairro, maxSemana = maxsemana, maximoTurno = ts.turn, max=17000, labels=bar_labels, values=bar_values)
        
    #return render_template('principal.html',maximoBairro = maxBairro, maxSemana = maxsemana, maximoTurno = ts.turn, max=17000, labels=bar_labels, values=bar_values)




# @app.route('/criar')
# def criar():
#     login_user(User(1))
#     return render_template('criar.html')


# @app.route('/usuario')
# def usuario():

#     return render_template('user.html')


# @app.route('/principal',methods = ['POST', 'GET'])
# def logi_n():
   
#     if request.method == 'POST':
#        user = request.form['username']
#        senha = request.form['password']
#        if user == 'admin' and senha == '123456' :
#         login_user(User(1))
#         return render_template('dashboard.html')
# #       print('post:', user)
# #       return render_template('login.html')
#     else:
#         user = request.args.get('username')
#         print('get:', user)
#         return render_template('login.html')

@app.route('/home')
@login_required
def dashboard():
    return render_template('dashboard.html',)

if __name__ == '__main__':

    app.run(debug=True)
