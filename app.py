from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

@app.route('/')
def file():
   return render_template('index.html')
	
@app.route('/getResults', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'GET':
        crim = float(request.args.get('crim'))
        #CRIM	ZN	INDUS	CHAS	NOX	RM	AGE	DIS	RAD	TAX	PTRATIO	B	LSTAT
        zn = float(request.args.get('zn'))
        indus = float(request.args.get('indus'))
        chas = float(request.args.get('chas'))
        nox = float(request.args.get('nox'))
        rm = float(request.args.get('rm'))
        age = float(request.args.get('age'))
        dis = float(request.args.get('dis'))
        rad = float(request.args.get('rad'))
        tax = float(request.args.get('tax'))
        ptratio = float(request.args.get('ptratio'))
        b = float(request.args.get('b'))
        lstat = float(request.args.get('lstat'))

        model = request.args.get('model')

        if model == 'dt':
            f = open("DecisionTree", "rb")
        elif model == 'rf':
            f = open("RandomForest", "rb")
        elif model == 'xgb':
            f = open("XGBoost", "rb")
        elif model == 'ada':
            f = open("AdaBoost", "rb")
        elif model == 'svr':
            f = open("SVR", "rb")
        m = pickle.load(f)

        
        f = open("XGBoost", "rb")

        m = pickle.load(f)[-1][-1]
        a = crim+zn
        mean1 = (crim+zn+indus+chas+nox+rm+age+dis+rad+tax+ptratio+b+lstat)/13
        ans = m.predict([[crim, zn, indus, chas, nox, rm, age, dis, rad, tax, ptratio, b, lstat, mean1, mean1, mean1, mean1, mean1]])

        
        return render_template("result.html", res=ans)


if __name__ == '__main__':
   app.run(debug = True)