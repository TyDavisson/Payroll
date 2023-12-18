% rebase('layout.tpl', title='Department Data')

<h2>Department: {{dept}}</h2>

<table class='table'>
    <tr>
        <th>Emp ID</th>
        <th>Name</th>
        <th>Wage</th>
        <th>Hrs Worked</th>
        <th>Weekly Pay</th>
    </tr>
    % for row in rows:
        <tr>
            % for col in row:
                <td>{{col}}</td>
            % end
        </tr>
    % end
</table>


