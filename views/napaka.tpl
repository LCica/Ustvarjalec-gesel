% rebase('base.tpl')


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
          <td>Kopiraj geslo</td>
          <td><input type="checkbox" name="ctrlc" value="1"></td>
        </tr>
        <tr>
          <td>Dolžina?</td>
          <td><input type="text" name="dolzine"></td></tr>
      </table>
        <button type="submit" class="offset">Novo Geslo</button>
  </form>
  
  </div>
  <div class="napaka">
  <h4>* PROSIMO IZBERITE VSAJ ENO VRSTO KARAKTERJEV IN VNESITE ZAŽELJENO DOLŽINO!</h4>
  </div>
</body>
</html>