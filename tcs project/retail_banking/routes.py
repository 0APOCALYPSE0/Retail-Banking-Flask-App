from flask import render_template, url_for, flash, redirect, session
from retail_banking import app, conn
from retail_banking.forms import LoginForm, AddCustomerForm, EditCustomerForm, DeleteCustomerForm, AddAccountForm, DeleteAccountForm, DepositeForm, WithdrawForm, TransferForm, StatementForm, SearchForm


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if 'username' in session:
        return redirect(url_for('home'))
    else:
        if form.validate_on_submit():
            cursor =conn.cursor()
            cursor.execute("SELECT * from userstore")
            data = cursor.fetchone()
            if form.username.data.strip() == data[1] and form.password.data.strip() == data[2]:
                session['username'] = form.username.data
                flash(f'You have been logged in successfully!','success')
                return redirect(url_for('home'))
            else:
                flash(f'Please check your username and password!','danger')
                return render_template("login.html", title='Login', form=form)
        return render_template("login.html", form=form)

@app.route("/home", methods=['GET', 'POST'])
def home():
    login = False
    if 'username' in session:
        login=True
        cursor =conn.cursor()
        cursor.execute("select customers.id, accounts.accid, customers.name, accounts.acctype, customers.state from customers inner join accounts on customers.id = accounts.custid")
        data = cursor.fetchall()
        form = SearchForm()
        if form.validate_on_submit():
            c_id = form.custId.data
            a_id = form.accId.data
            if len(c_id) == 0:
                c_id = '0'
            elif len(a_id) == 0:
                a_id = '0'
            custid = int(c_id)
            accid = int(a_id)
            query1 = "select customers.id, accounts.accid, customers.name, accounts.acctype, customers.state from customers inner join accounts on customers.id = accounts.custid where customers.id = %s"
            cursor.execute(query1, (custid-100000000))
            data1 = cursor.fetchall()
            query2 = "select customers.id, accounts.accid, customers.name, accounts.acctype, customers.state from customers inner join accounts on customers.id = accounts.custid where accounts.accid = %s"
            cursor.execute(query2, (accid-500000000))
            data2 = cursor.fetchall()
            print(a_id)
            print(c_id)
            print(data1)
            print(data2)
            if len(data1)>0:
                data = data1
            elif len(data2)>0:
                data = data2
            return render_template("home.html", login=login, data=data, form=form)
        return render_template("home.html", login=login, data=data, form=form)
    else:
        return redirect(url_for('login'))

@app.route('/add_customer', methods=['GET', 'POST'])
def add_customer():
    login = False
    if 'username' in session:
        login=True
        form = AddCustomerForm()
        if form.validate_on_submit():
            params = {
                'ssnid' : form.ssnid.data,
                'name'  : form.name.data,
                'age'   : form.age.data,
                'add'   : form.add.data,
                'city'  : form.city.data,
                'state' : form.state.data
            }
            cursor =conn.cursor()
            queryCheck = "select * from customers where ssnid = %s"
            cursor.execute(queryCheck, (form.ssnid.data))
            res = cursor.fetchall()
            if len(res) > 0:
                flash(f'This Customer ID is already exists!','danger')
                return render_template("create_customer.html", login=login, form=form) 
            query = """insert into customers (ssnid,name,age,addr,city,state) values (%(ssnid)s,%(name)s,%(age)s,%(add)s,%(city)s,%(state)s)"""
            bool = False
            bool = cursor.execute(query, params)
            conn.commit()
            query1 = "select id from customers where ssnid = %s"
            bool = cursor.execute(query1, (params['ssnid']))
            custid = cursor.fetchone()
            mssg = "Customer Creation Completed."
            param = {
                'c_id' : custid[0],
                'mssg' : mssg
            }
            query2 = """insert into custstatus (custid,mssg) values (%(c_id)s, %(mssg)s)"""
            bool = cursor.execute(query2, param)
            conn.commit()
            if bool:
                flash(f'Customer creation initiated successfully!','success')
                return redirect(url_for('home'))
            else:
                flash(f'Customer creation not initiated!','danger')
                return render_template("create_customer.html", login=login, form=form)
        return render_template("create_customer.html", login=login, form=form)
    else:
        return redirect(url_for('login'))

@app.route('/update_customer')
def update_customer():
    login = False
    if 'username' in session:
        login=True
        cursor =conn.cursor()
        cursor.execute("SELECT * from customers")
        data = cursor.fetchall()
        return render_template("update_customer.html", login=login, data=data)
    else:
        return redirect(url_for('login'))

@app.route('/edit_customer/<id>', methods=['GET', 'POST'])
def edit_customer(id):
    login = False
    if 'username' in session:
        login=True
        form = EditCustomerForm()
        cursor =conn.cursor()
        query = "SELECT * from customers where id = %s"
        cursor.execute(query, (id))
        data = cursor.fetchone()
        if form.validate_on_submit():
            new_name = form.name.data
            new_age = form.age.data
            new_Add = form.add.data
            new_city = form.city.data
            new_state = form.state.data
            query_str = "update customers set name = %s, age = %s, addr = %s, city = %s, state = %s where id = %s"
            bool = False
            bool = cursor.execute(query_str, (new_name,new_age,new_Add,new_city,new_state,id))
            conn.commit()
            query1 = "update custstatus set mssg = %s where custid = %s"
            mssg = "Customer Updation Completed"
            bool = cursor.execute(query1, (mssg, id))
            conn.commit()
            if bool:
                flash(f'Customer updation initiated successfully!','success')
                return redirect(url_for('update_customer'))
            else:
                flash(f'Customer updation not initiated successfully!','danger')
                return redirect(url_for('update_customer'))
        return render_template("edit_customer.html", login=login, data=data, form=form)
    else:
        return redirect(url_for('login'))

@app.route('/delete_customer/<id>', methods=['GET', 'POST'])
def delete_customer(id):
    login = False
    if 'username' in session:
        login=True
        form = DeleteCustomerForm()
        cursor =conn.cursor()
        query = "SELECT * from customers where id = %s"
        cursor.execute(query, (id))
        data = cursor.fetchone()
        if form.is_submitted():
            query_str = "delete from customers where id = %s"
            bool = False
            bool = cursor.execute(query_str, (id))
            conn.commit()
            if bool:
                flash(f'Customer deletion initiated successfully!','success')
                return redirect(url_for('update_customer'))
            else:
                flash(f'Customer deletion not initiated successfully!','danger')
                return redirect(url_for('update_customer'))
        return render_template("delete_customer.html", login=login, data=data, form=form)
    else:
        return redirect(url_for('login'))

@app.route('/add_account', methods=['GET', 'POST'])
def add_account():
    login = False
    if 'username' in session:
        login=True
        form = AddAccountForm()
        if form.validate_on_submit():
            params = {
                'custid' : int(form.customerid.data)-100000000,
                'accType'  : form.accType.data
            }
            cursor =conn.cursor()
            queryCheck = "select * from accounts where custid = %s and acctype = %s"
            cursor.execute(queryCheck, (int(form.customerid.data)-100000000, form.accType.data))
            res = cursor.fetchall()
            if len(res) > 0:
                flash(f'Account is already exists!','danger')
                return render_template("create_account.html", login=login, form=form)
            query = """insert into accounts (custid, accType) values (%(custid)s,%(accType)s)"""
            bool = False
            bool = cursor.execute(query, params)
            conn.commit()
            query1 = "select accid from accounts where custid = %s"
            bool = cursor.execute(query1, (params['custid']))
            accid = cursor.fetchone()
            mssg = "Account Creation Completed."
            param = {
                'accid' : accid[0],
                'mssg' : mssg
            }
            query2 = """insert into accstatus (acid,mssg) values (%(accid)s, %(mssg)s)"""
            bool = cursor.execute(query2, param)
            conn.commit()
            param1 = {
                'accid' : accid[0],
                'transaction' : form.depositeAmount.data,
                'balance' : form.depositeAmount.data,
                'transtype' : 1
            }
            query3 = """insert into accbalance (acid, transactions, balance, transtype) values(%(accid)s,%(transaction)s,%(balance)s,%(transtype)s)"""
            bool = cursor.execute(query3, param1)
            conn.commit()
            if bool:
                flash(f'Account creation initiated successfully!','success')
                return redirect(url_for('home'))
            else:
                flash(f'Account creation not initiated!','danger')
                return render_template("create_account.html", login=login, form=form)
        return render_template("create_account.html", login=login, form=form)
    else:
        return redirect(url_for('login'))

@app.route('/view_account')
def view_account():
    login = False
    if 'username' in session:
        login=True
        cursor =conn.cursor()
        cursor.execute("SELECT * from accounts")
        data = cursor.fetchall()
        return render_template("view_account.html", login=login, data=data)
    else:
        return redirect(url_for('login'))


@app.route('/delete_account/<id>', methods=['GET', 'POST'])
def delete_account(id):
    login = False
    if 'username' in session:
        login=True
        form = DeleteAccountForm()
        cursor =conn.cursor()
        query = "SELECT * from accounts where accid = %s"
        cursor.execute(query, (id))
        data = cursor.fetchone()
        if form.is_submitted():
            query_str = "delete from accounts where accid = %s"
            bool = False
            bool = cursor.execute(query_str, (id))
            conn.commit()
            if bool:
                flash(f'Account deletion initiated successfully!','success')
                return redirect(url_for('view_account'))
            else:
                flash(f'Account deletion not initiated successfully!','danger')
                return redirect(url_for('view_account'))
        return render_template("delete_account.html", login=login, data=data, form=form)
    else:
        return redirect(url_for('login'))

@app.route('/view_customer_status')
def view_customer_status():
    login = False
    if 'username' in session:
        login=True
        cursor =conn.cursor()
        cursor.execute("SELECT customers.ssnid, customers.id, custstatus.status, custstatus.mssg, custstatus.lastupdated from customers inner join custstatus on customers.id = custstatus.custid")
        data = cursor.fetchall()
        return render_template("view_customer_status.html", login=login, data=data)
    else:
        return redirect(url_for('login'))

@app.route('/view_customer/<id>', methods=['GET', 'POST'])
def view_customer(id):
    login = False
    if 'username' in session:
        login=True
        cursor =conn.cursor()
        query = "select * from customers where id = %s"
        cursor.execute(query, (id))
        data = cursor.fetchone()
        return render_template("view_customer.html", login=login, data=data)
    else:
        return redirect(url_for('login'))

@app.route('/view_account_status')
def view_account_status():
    login = False
    if 'username' in session:
        login=True
        cursor =conn.cursor()
        cursor.execute("SELECT accounts.accid, accounts.custid, accstatus.status, accstatus.mssg, accstatus.lastupdated from accounts inner join accstatus on accounts.accid = accstatus.acid")
        data = cursor.fetchall()
        return render_template("view_account_status.html", login=login, data=data)
    else:
        return redirect(url_for('login'))

@app.route('/view_customer_details/<id>', methods=['GET', 'POST'])
def view_customer_details(id):
    login = False
    if 'username' in session:
        login=True
        cursor =conn.cursor()
        query = "select customers.ssnid, customers.id, accounts.accid, customers.name, customers.age, customers.addr, customers.city, customers.state, accounts.acctype from customers inner join accounts on customers.id = accounts.custid where id = %s"
        cursor.execute(query, (id))
        data = cursor.fetchone()
        query1 = "select balance from accbalance where acid = %s order by lastupdated desc limit 0,1"
        cursor.execute(query1, (data[2]))
        data1 = cursor.fetchone()
        data = data+data1
        return render_template("view_customer_details.html", login=login, data=data)
    else:
        return redirect(url_for('login'))

@app.route('/deposite/<id>', methods=['GET', 'POST'])
def deposite(id):
    login = False
    if 'username' in session:
        login=True
        form = DepositeForm()
        cursor =conn.cursor()
        query2 = "select * from accounts where custid = %s"
        cursor.execute(query2, (id))
        data = cursor.fetchone()
        accid = data[0]
        query3 = "select balance from accbalance where acid = %s order by lastupdated desc limit 0,1"
        cursor.execute(query3, (accid))
        data2 = cursor.fetchone()
        data = data+data2
        if form.validate_on_submit():
            deposite = form.deposite.data
            query = "select balance from accbalance where acid = %s order by lastupdated desc limit 0,1"
            cursor.execute(query, (accid))
            data1 = cursor.fetchone()
            balance  = deposite + data1[0]
            param = {
                'accid' : accid,
                'transaction' : deposite,
                'balance' : balance,
                'transtype' : 1
            }
            query1 = """insert into accbalance(acid, transactions, balance, transtype) values(%(accid)s, %(transaction)s, %(balance)s, %(transtype)s)"""
            bool = False
            bool = cursor.execute(query1, param)
            conn.commit()
            if bool:
                flash(f'Amount deposited successfully!','success')
                return redirect(url_for('update_mssg',id=id,type=0))
            else:
                flash(f'Amount not deposited successfully!','danger')
                return redirect(url_for('deposite',id=id))
        return render_template("deposite.html", login=login, data=data, form=form)
    else:
        return redirect(url_for('login'))

@app.route('/withdraw/<id>', methods=['GET', 'POST'])
def withdraw(id):
    login = False
    if 'username' in session:
        login=True
        form = WithdrawForm()
        cursor =conn.cursor()
        query2 = "select * from accounts where custid = %s"
        cursor.execute(query2, (id))
        data = cursor.fetchone()
        accid = data[0]
        query3 = "select balance from accbalance where acid = %s order by lastupdated desc limit 0,1"
        cursor.execute(query3, (accid))
        data2 = cursor.fetchone()
        data = data+data2
        if form.validate_on_submit():
            withdraw = form.withdraw.data
            query = "select balance from accbalance where acid = %s order by lastupdated desc limit 0,1"
            cursor.execute(query, (accid))
            data1 = cursor.fetchone()
            if withdraw > data1[0]:
                flash(f'Insufficient Balance!','danger')
                return redirect(url_for('withdraw',id=id))
            balance  = data1[0] - withdraw
            param = {
                'accid' : accid,
                'transaction' : withdraw,
                'balance' : balance,
                'transtype' : 0
            }
            query1 = """insert into accbalance(acid, transactions, balance, transtype) values(%(accid)s, %(transaction)s, %(balance)s, %(transtype)s)"""
            bool = False
            bool = cursor.execute(query1, param)
            conn.commit()
            if bool:
                flash(f'Amount withdraw successfully!','success')
                return redirect(url_for('update_mssg',id=id,type=1))
            else:
                flash(f'Amount not withdraw successfully!','danger')
                return redirect(url_for('withdraw',id=id))
        return render_template("withdraw.html", login=login, data=data, form=form)
    else:
        return redirect(url_for('login'))

@app.route('/update_mssg/<id>/<type>')
def update_mssg(id, type):
    login = False
    if 'username' in session:
        login=True
        cursor =conn.cursor()
        query = "select name from customers where id = %s"
        cursor.execute(query, (id))
        data = cursor.fetchone()
        query1 = "select * from accounts where custid = %s"
        cursor.execute(query1, (id))
        data1 = cursor.fetchone()
        query2 = "select transactions, balance from accbalance where acid = %s order by lastupdated desc limit 0,1"
        cursor.execute(query2, (data1[0]))
        data2 = cursor.fetchone()
        data = data+data1+data2
        return render_template("update_mssg.html", login=login, data=data, type=type)
    else:
        return redirect(url_for('login'))

@app.route('/transfer/<id>', methods=['GET', 'POST'])
def transfer(id):
    login = False
    if 'username' in session:
        login=True
        cursor =conn.cursor()
        cursor.execute("select accid from accounts")
        accids = cursor.fetchall()
        accidsList = []
        for accid in accids:
            t1 = (accid[0], 500000000+accid[0])
            accidsList.append(t1)
        queryaccid = "select accid from accounts where custid = %s"
        cursor.execute(queryaccid, (id))
        accids1 = cursor.fetchall()
        accidsList1 = []
        for accid in accids1:
            t1 = (accid[0], 500000000+accid[0])
            accidsList1.append(t1)
        form = TransferForm()
        form.sourceAcc.choices = accidsList1
        form.targetAcc.choices = accidsList
        data = int(id)
        if form.is_submitted():
            transfer = form.transfer.data
            sourceAcc = form.sourceAcc.data
            targetAcc = form.targetAcc.data
            query = "select balance from accbalance where acid = %s order by lastupdated desc limit 0,1"
            cursor.execute(query, (sourceAcc))
            data1 = cursor.fetchone()
            if transfer > data1[0]:
                flash(f'Insufficient Balance!','danger')
                return redirect(url_for('transfer',id=id))
            balance  = data1[0] - transfer
            param = {
                'accid' : sourceAcc,
                'transaction' : transfer,
                'balance' : balance,
                'transtype' : 0
            }
            query1 = """insert into accbalance(acid, transactions, balance, transtype) values(%(accid)s, %(transaction)s, %(balance)s, %(transtype)s)"""
            bool = False
            bool = cursor.execute(query1, param)
            conn.commit()
            query2 = "select balance from accbalance where acid = %s order by lastupdated desc limit 0,1"
            cursor.execute(query2, (targetAcc))
            data1 = cursor.fetchone()
            balance  = data1[0] + transfer
            param = {
                'accid' : targetAcc,
                'transaction' : transfer,
                'balance' : balance,
                'transtype' : 1
            }
            query3 = """insert into accbalance(acid, transactions, balance, transtype) values(%(accid)s, %(transaction)s, %(balance)s, %(transtype)s)"""
            bool = cursor.execute(query3, param)
            conn.commit()
            if bool:
                flash(f'Amount transfered successfully!','success')
                return redirect(url_for('transfer_update_mssg',sourceId=sourceAcc, targetId=targetAcc))
            else:
                flash(f'Amount not transfered successfully!','danger')
                return redirect(url_for('transfer'))
        return render_template("transfer.html", login=login, data=data, form=form)
    else:
        return redirect(url_for('login'))

@app.route('/transfer_update_mssg/<sourceId>/<targetId>')
def transfer_update_mssg(sourceId, targetId):
    login = False
    if 'username' in session:
        login=True
        cursor =conn.cursor()
        query = "select balance from accbalance where acid = %s order by lastupdated desc limit 1,1"
        cursor.execute(query, (sourceId))
        spbalance = cursor.fetchone()
        query1 = "select balance from accbalance where acid = %s order by lastupdated desc limit 0,1"
        cursor.execute(query1, (sourceId))
        subalance = cursor.fetchone()
        query = "select balance from accbalance where acid = %s order by lastupdated desc limit 1,1"
        cursor.execute(query, (targetId))
        tpbalance = cursor.fetchone()
        query1 = "select balance from accbalance where acid = %s order by lastupdated desc limit 0,1"
        cursor.execute(query1, (targetId))
        tubalance = cursor.fetchone()
        data = (int(sourceId),) + (int(targetId),) + spbalance + tpbalance + subalance + tubalance
        print(data)
        return render_template("transfer_update_mssg.html", login=login, data=data)
    else:
        return redirect(url_for('login'))

@app.route('/account_statement', methods=['GET', 'POST'])
def account_statement():
    login = False
    if 'username' in session:
        login=True
        cursor =conn.cursor()
        cursor.execute("select accid from accounts")
        accids = cursor.fetchall()
        accidsList = []
        for accid in accids:
            t1 = (accid[0], 500000000+accid[0])
            accidsList.append(t1)
        cursor.execute("select lastupdated from accbalance")
        dates = cursor.fetchall()
        datesList = []
        for date in dates:
            t1 = (date[0], date[0])
            datesList.append(t1)
        form = StatementForm()
        form.accid.choices = accidsList
        form.startDate.choices = datesList
        form.endDate.choices = datesList
        data = False
        if form.is_submitted():
            accid = form.accid.data
            stmtOption = form.stmtOption.data
            transNo = int(form.transNo.data)
            startDate = form.startDate.data
            endDate = form.endDate.data
            query = "select * from accbalance where acid = %s order by lastupdated desc limit 0,%s"
            cursor.execute(query, (accid, transNo))
            data1 = cursor.fetchall()
            query = "select * from accbalance where acid = %s and lastupdated between %s and %s order by lastupdated desc"
            cursor.execute(query, (accid, startDate, endDate))
            data2 = cursor.fetchall()
            if stmtOption == 'trans':
                data = data1
            elif stmtOption == 'date':
                data = data2 
            bool = False
            print(data)
            if len(data) > 0:
                bool = True
            if bool:
                flash(f'Statement Generated successfully!','success')
                return render_template("account_statements.html", login=login, data=data, form=form)
            else:
                flash(f'Something Wrong!','danger')
                return redirect(url_for('account_statement',login=login, data=data, form=form))
        return render_template("account_statements.html", login=login, data=data, form=form)
    else:
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('login'))