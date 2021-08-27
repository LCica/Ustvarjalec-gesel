
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
      h1{
        color: red;
      }
      .center{
        position: relative;
      }
      .gumb {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
        }
  
        #btn {
            text-align: center;
            height: 60px;
            width: 200px;
            display: block;
            font-size: 1.5em;
            background: #68E73C;
        }
  
        #btn:hover {
            animation: effect 0.4s infinite;
        }
  
        @keyframes effect {
            0% {
                transform: translateX(0px) rotate(0deg);
            }
  
            20% {
                transform: translateX(-4px) rotate(-4deg);
            }
  
            40% {
                transform: translateX(-2px) rotate(-2deg);
            }
  
            60% {
                transform: translateX(4px) rotate(4deg);
            }
  
            80% {
                transform: translateX(2px) rotate(2deg);
            }
  
            100% {
                transform: translateX(0px) rotate(0deg);
            }
        }
    </style> 
</head>
<body text="white"> 
  <div class="center" >
    <form method="POST" action="/geslo/" >
      <h1> Generator gesel</h1>
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
          <div class="gumb"><button type="submit" id="btn">Novo Geslo</div>
    </form>
    <label>Vaše geslo je: {{ geslo }}</label>
  </div>
  <img src="mojgif.gif" alt="mojgif.gif">
</body>
    
</html>