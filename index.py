# Ty Davisson - project 6
import sqlite3 as db
from bottle import route, run, template, request

# Index page - displays login page
@route('/', method='GET')
def index():
    return template('login')
# Displays form on get or table on a post
@route('/displayDept', method=['GET', 'POST'])
def displayDept():
    if request.method == 'GET':
        return template('getDept')
    else:
        # Gets dept from form
        dept = request.forms.get('dept')

        conn = db.connect('payroll.db')
        cur = conn.cursor()
        # query for employee data
        sql = "SELECT p.emp_id, e.emp_name, e.wage, p.hrs_worked FROM employees e JOIN pay_data p ON e.emp_id = p.emp_id WHERE e.department = ?"

        cur.execute(sql, (dept,))
        deptList = cur.fetchall()
        cur.close()
        # if anything is returned this calucales weekly pay with or without OT and returns the table
        if deptList:
            dataList = []
            for row in deptList:
                eID, name, wage, hrs = row
                if hrs <= 40:
                    weeklyPay = hrs * wage
                else:
                    ot = (hrs - 40) * 1.5 * wage
                    weeklyPay = (40 * wage) + ot
                data = (eID, name, wage, hrs, weeklyPay)
                dataList.append(data)
            deptData = {'rows': dataList, 'dept': dept}
            return template('deptData', deptData)
# Displays form on a get, and updates database on a post                           
@route('/editEmp', method=['GET', 'POST'])
def editEmp():
    if request.method == 'GET':
        return template('editEmp')
    else:
        eID = request.forms.get('empID')
        hrs = request.forms.get('hours')
        
        try:
            conn = db.connect('payroll.db')
            cur = conn.cursor()
            
            # gets employee infor for success msg
            cur.execute("SELECT emp_id, emp_name, department FROM employees WHERE emp_id = ?", (eID,))
            emp = cur.fetchone()
            # updates employee data
            sql = "UPDATE pay_data SET hrs_worked = ? WHERE emp_id = ?"
            cur.execute(sql, (hrs, eID))
            conn.commit()
            # returns success msg
            msg = f"eid: {emp[0]}, name: {emp[1]}, department: {emp[2]} successfully updated."
            return template('status', msg=msg)
        # returns error 
        except db.Error as e:
            msg = f"Error: {e}"
            return template('status', msg=msg)
        # closes connection    
        finally:
            cur.close()
            conn.close()
               
run(host='localhost', port=8081)