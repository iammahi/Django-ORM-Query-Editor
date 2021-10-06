function ajax(name) 
{
  if(name === undefined)
  {
     name = document.getElementById("book_name").value;
  }
  
  var div = document.getElementById('show');
  div.style.display='none';
  var name =name.replaceAll('&','%26')
  var name =name.replaceAll('+','%2B')
  var http =new XMLHttpRequest();
  var url= '/ajax?name='+name;
  http.onreadystatechange = function()
  {
    if(this.readyState == 4 && this.status == 200)
    { 
     
      try
      {

        var data = eval(http.responseText);
        div.style.display='block';
        div.innerHTML=''
        var table = document.createElement('TABLE');
        var c=0
        var row = table.insertRow(0);
        for (var i in data[0])
        {
             
            row.insertCell(c).innerHTML=i.toUpperCase();
            c++;
        }
          
        for (var i = 0; i < data.length; i++)
        {
          var row = table.insertRow(i+1);
          k=0;
          for(var j in data[0])
          {   
            row.insertCell(k).innerHTML=data[i][j];
            k++;
          }
        }
             
        div.appendChild(table)
        table.className ='table border table-striped '; 
      }
      catch(e){
        var data = http.responseText ;
        alert(data)
      }   
    }
  }
  http.open('GET',url,true);
  http.send();
}
function Query(){
  ajax();
}
function Table(name){
  ajax(name);
}



