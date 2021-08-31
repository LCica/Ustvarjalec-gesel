<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
    .offset { color:  #19bc8b;
      box-shadow: 
        0.3em 0.3em 0 0 var(--color),
        inset 0.3em 0.3em 0 0 var(--color)}
    .offset:hover,
    .offset:focus {
      box-shadow: 
      0 0 0 0 var(--hover),
      inset 6em 3.5em 0 0 var(--hover);
    } 
    .offset {
      --color: #19bc8b;
      --hover: #{adjust-hue(19bc8b, 45deg)};
    }
         
    .offset:hover,
    .offset:focus { 
      border-color: var(--hover);
      color: dodgerblue;
    }   
    body {
      color: #fff;     
      font: 600 1.05em 'Fira Sans', sans-serif;
      background: hsl(227, 10%, 10%);     
      text-align: center;
      min-height: 100vh;
    }
    button {
      background: none;
      border: 2px solid;
      font: inherit;
      line-height: 1;
      margin: 0.5em;
      padding: 1em 2em;
      transition: 0.25s;
    }
    h1 {font: 10000 1em 'Fira Sans', sans-serif;
    color: #19bc8b;
      text-shadow: 0 0 10px #00b3ff;}
      
    .center{
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .napaka{
      width: 725px;
      border-top-left-radius: 10px;
      border-top-right-radius: 10px;
      border-bottom-left-radius: 10px;
      border-bottom-right-radius: 10px;
      margin: auto;
      display: flex;
      align-items: center;
      justify-content: center;    
    }
    h4{
      color: red;
      font-family: 'Fira Sans';
    }
    </style>
</head>
<body>
    {{!base}}
</body>
</html>