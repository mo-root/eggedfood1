from database import *
#from flask_bootstrap import Bootstrap
from flask import Flask, request, redirect, render_template
from flask import session as login_session
from model import *
import webbrowser
import os
app = Flask(__name__)
#Bootstrap(app)




app.config['SECRET_KEY'] = 'you-will-never-guess'



@app.route('/')
def main():
        return render_template('main.html')
              



@app.route('/log.html')
def log():
      return render_template('log.html')





@app.route('/about.html')
def fullList():
    return render_template('about.html')

@app.route('/main.html')
def main2():
      return render_template('main.html')

@app.route('/pay.html')
def mai():
      return render_template('pay.html')



@app.route('/order.html')
def fullList1():
    items=query_all()
    return render_template('order.html',items=items)


@app.route('/Learn.html')
def fullList2():
    return render_template('Learn.html')


@app.route('/profile.html')
def fullList3():
    return render_template('profile.html')

@app.route('/list.html/<int:p_id>')
def order(p_id):
    order=session.query(Item).filter_by(id=p_id).one()
    return render_template('list.html',Item=Item)


@app.route('/list.html')
def ey():
    return render_template('list.html')




@app.route('/list.html/main.html')
def easday():
    return render_template('main.html')


@app.route('/list.html/log.html')
def eaassday():
    return render_template('log.html')

@app.route('/list.html/about.html')
def eas123day():
    return render_template('about.html')


@app.route('/list.html/order.html')
def eas1asd23day():
    return render_template('order.html')




@app.route('/list.html/list.html')
def eas1as234d23day():
    return render_template('list.html')

@app.route('/list.html/upload.html')
def day():
    return render_template('upload.html')


##@app.context_processor
##def override_url_for():
##    return dict(url_for=dated_url_for)
##
##def dated_url_for(endpoint, **values):
##    if endpoint == 'static':
##        filename = values.get('filename', None)
##        if filename:
##            file_path = os.path.join(app.root_path,
##                                 endpoint, filename)
##            values['q'] = int(os.stat(file_path).st_mtime)
##    return url_for(endpoint, **values)



##
##@app.route('/')
##def main():
##
##	return render_template('/home/student/Desktop/meet stuff/meet folder/final_css_pro/web/templates/maim.html')
##




@app.route('/upload.html' , methods=['GET','POST'])
def upload():
	if request.method == 'GET' :
		return render_template('upload.html')

	else:
		print("creating object")
		name_of_item = request.form['name']
		description = request.form['description']
		price_d = request.form['price']
		link = request.form['imgLs']
		place = request.form['place']
		view = request.form['view']
		exp = request.form['exp']
		add_item(name_of_item , description , price_d, link , place , view , exp)
		return redirect('main.html')

@app.route('/list.html/upload.html' , methods=['GET','POST'])
def pppasdasasdadaqqwrq():
    if request.method == 'GET' :
        return render_template('upload.html')

    else:
        print("creating object")
        name_of_item = request.form['name']
        description = request.form['description']
        price_d = request.form['price']
        link = request.form['imgLs']
        place = request.form['place']
        view = request.form['view']
        exp = request.form['exp']
        add_item(name_of_item , description , price_d, link , place , view , exp)
        return redirect('main.html')


@app.route('/list.html/upload.html')
def asdasdrftgyhujik():
    return redirect('upload.html')



##@app.route('/list.html')
##def fullList():
##	places=query_all()
##	return render_template('list.html',places=places)
##
##@app.route('/place.html/<int:p_id>')
##def place(p_id):
##	place=session.query(Place).filter_by(id=p_id).one()
##	return render_template('place.html',place=place)

# @app.route('/blog.html',methods=["GET","POST"])
# def blog():
# 	if request.method == "GET":
# 		return render_template("blog.html")
# 	else :
# 		username = request.form['username']
# 		event = request.form["event"]
# 		phonenumber = request.form["phonenumber"]
# 		add_event(username,event,phonenumber)
# 		return NewHome()
# @app.route('/about.html')
# def about():
# 	return render_template("about.html")














# @app.route('/login', methods=['POST'])
# def login():
#     user = get_user(request.form['username'])
#     if user != None and user.verify_password(request.form["password"]):
#         login_session['name'] = user.username
#         login_session['logged_in'] = True
#         return logged_in()
#     else:
#         return home()


# @app.route('/signup', methods=['POST'])
# def signup():
#     #check that username isn't already taken
#     user = get_user(request.form['username'])
#     if user == None:
#         add_user(request.form['username'],request.form['password'])
#     return home()


# @app.route('/logged-in')
# def logged_in():
#     return render_template('logged.html')


# @app.route('/logout')
# def logout():
#     login_session['name'] = None
#     login_session['logged_in'] = False
#     return home()



if __name__ == '__main__':
	app.run(debug=True)
