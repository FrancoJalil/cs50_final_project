let main_button = document.getElementById('main-button');

main_button.addEventListener("click", function() {
  var command = document.getElementById("command").value;
  console.log(command)

  const url = `http://127.0.0.1:8000/get_scrap?command=${command}`;
  console.log(url)

  const Http = new XMLHttpRequest();

  Http.open("GET", url);
  Http.send();


  Http.onreadystatechange=(e)=>{
  console.log(Http.responseText)

  let show = document.getElementById('show');
  show.innerHTML = Http.responseText;

}
});


