
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Geslo</title>  
    <style>
      body{
          background: black}
      .center{
        position: relative;
        background-color: gray;
        left: 25%;
        margin-top: 25px; 
        width: 50%;
        height: 500px ;
        border-top-left-radius: 10px;
        border-top-right-radius: 10px;
      }
    </style> 
</head>
<body>
  <div class="center">
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
    <label>Vaše geslo je: {{ geslo }}</label>
  </div>
</body>
    
</html>