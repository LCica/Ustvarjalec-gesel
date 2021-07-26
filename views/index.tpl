
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Geslo</title>   
</head>
<body>
  <form method="POST" action="/geslo/" >
  <table>    
    <tr>
      <td>Številke?</td>
      <td><input type="checkbox" name="prva" value="1" ></td>
    </tr>
    <tr>
      <td>Male črke?</td>
      <td><input type="checkbox" name="druga" value="2"></td>
    </tr>
    <tr>
      <td>Velike črke?</td>
      <td><input type="checkbox" name="tretja" value="3" ></td>
    </tr>
    <tr>
      <td>Simboli?</td>
      <td><input type="checkbox" name="cetrta" value="4"></td>
    </tr>
    <tr>
      <td>Dolžina?</td>
      <td><input type="text" name="dolzine"></td></tr>
  </table>
    <input type="submit" name="vnesi" >
  </form>    
</body>

</html>