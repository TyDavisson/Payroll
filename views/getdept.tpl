% rebase('layout.tpl', title='Department Form')
<p> Choose Department: 
    <form action="/displayDept" method="POST"> 
        <select name='dept'>
            <option value='advertising'>Advertising</option>
            <option value='environment'>Environment</option>
            <option value='maintenance'>Maintenance</option>
            <option value='shipping'>Shipping</option>
        </select> &nbsp;
        <input type='submit'>
    </form>
</p>
