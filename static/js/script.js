let main_button = document.getElementById('main-button');

main_button.addEventListener("click", function() {
  var command = document.getElementById("command").value;

  const url = `http://127.0.0.1:8000/get_scrap?command=${command}`;
  const Http = new XMLHttpRequest();

  Http.open("GET", url);
  Http.send();

  Http.onreadystatechange=(e)=>{

  

  if (command.includes("/export")) {
    let export_to = document.getElementById('export_to')
    export_to.innerHTML = "some link"
    
  } else {

    let show = document.getElementById('show');
    show.innerHTML = Http.response;
  };
  
} 
});
