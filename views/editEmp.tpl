% rebase('layout.tpl', title='Edit Employee')
<h3>Add Data</h3>
<form action="/editEmp" method="POST"> 
    <p>Employee ID: <input name="empID" type="text"></p>
    <p>Hours Worked: <input name="hours" type="text"></p>
    <p><input type="submit"></p>
</form>