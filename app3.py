# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 14:48:27 2021

@author: User
  """

from flask import Flask,render_template,request,redirect
import pymysql
app=Flask(__name__)
@app.route('/')
def index():
       try:
         db=pymysql.connect(host='localhost',user='root',password='',db='employee1')
         cu=db.cursor()
         sql="select * from emply1"
         cu.execute(sql)
         data=cu.fetchall()
         #return "success"
         return render_template('dashboard3.html',d=data)
       except Exception:
         return"Error"
    #return render_template('dashboard3.html')
    
@app.route('/store',methods=['POST','GET'])
def store():
      rid=request.form['id']
      nm=request.form['name']
      add=request.form['address']
      dt=request.form['date'] 
      
      try:
        db=pymysql.connect(host='localhost',user='root',password='',db='employee1')
        cu=db.cursor()
        sql="insert into emply1(id,name,address,date)values('{}','{}','{}','{}')".format(rid,nm,add,dt)
        cu.execute(sql)
        db.commit()
        return redirect('/')
        #return "data inserted into table"
        
      except Exception:
         db.rollback()
         return 'Error in connection'
         
      #return rid+nm+add+dt

@app.route('/form')
def form():
    return render_template('form3.html')

@app.route('/delete/<rid>')
def delete(rid):
     try:
        db=pymysql.connect(host='localhost',user='root',password='',db='employee1')
        cu=db.cursor()
        sql="delete from emply1 where id={}".format(rid)
        cu.execute(sql)
        db.commit()
        return redirect('/')
        
     except Exception:
        db.rollback()
        return 'Error in connection'
         
    #return "ID to be deleted is:"+rid
@app.route('/edit/<rid>')
def edit(rid):
     try:
        db=pymysql.connect(host='localhost',user='root',password='',db='employee1')
        cu=db.cursor()
        sql="select * from emply1 where id={}".format(rid)
        cu.execute(sql)
        data=cu.fetchone()
        return render_template('editform3.html',d=data)
     except Exception:
        return 'Error'
@app.route('/update',methods=['POST','GET'])
def update():
         rid=request.form['id']
         nm=request.form['name']
         add=request.form['address']
         dt=request.form['date'] 
         #return rid+nm+add+dt
         try:
            db=pymysql.connect(host='localhost',user='root',password='',db='employee1')
            cu=db.cursor()
            sql="update emply1 SET rid='{}',name='{}',address='{}',date='{}' where id='{}'".format(rid,nm,add,dt,)
            cu.execute(sql)
            db.commit()
            return ('/redirect')
         except Exception:
            db.rollback()
            return 'error'
         
    
app.run(debug=True)
    
    
     