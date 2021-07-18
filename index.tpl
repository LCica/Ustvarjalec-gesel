<!DOCTYPE html>
<html>

<head>
    <title>Vislice</title>
    <style type="text/css">
        h1 { color: red;}
        body { background-color: lightyellow;}
    </style>
</head>

<body>
    <h1>Generator gesel!</h1>
    <table>
      <tr>
               
        <th>Katere znake naj vsebuje vaše geslo?</th>
        
      </tr>
      <tr>
        
        <td>Številke?</td>
        <td><input type="checkbox"></td>
      </tr>
      <tr>
        <td>Male črke?</td>
        <td><input type="checkbox" ></td>
      </tr>
      <tr>
        <td>Velike črke?</td>
        <td><input type="checkbox"></td>
      </tr>
      <tr>
        <td>Simbole?</td>
        <td><input type="checkbox"></td>
      </tr>   
    </table>
    <form action= "/geslo/" method="POST">
      <label>Dolžina gesla:
        <input type="text" name="dolzina">
      </label>
      <input type="submit" value="Zgeneriraj Geslo"/>
    </form>
    
    
</body>

</html>