

document.getElementById("command")
    .addEventListener("keyup", function(e) {
        if (e.key === 'Enter' || e.key === 'Intro') {
            document.getElementById("main-button").click();
        }
    });
 

let main_button = document.getElementById('main-button');

main_button.addEventListener("click", function() {
  var command = document.getElementById("command").value;

  // commands log
  let command_logs = document.getElementById('commands-log')

  command_logs.innerHTML += command+"<br><br>";

  // scrap
  const url = `http://127.0.0.1:8000/get_scrap?command=${command}`;
  const Http = new XMLHttpRequest();

  Http.open("GET", url);
  Http.send();

  Http.onreadystatechange=(e)=>{

    let show = document.getElementById('show');
    let export_to = document.getElementById('export_to');

    if (command.includes("/export")) {

      export_to.style.display = "block";
      export_to.href = url;
      export_to.innerHTML = "export.txt";
      
      if (Http.status == 404) {
        show.innerHTML = "Export Failed";
        export_to.style.display = "none";
      }
      
    } else {
      export_to.style.display = "none";
      show.innerHTML = Http.response;
  };
  
} 
});

// Get the canvas node and the drawing context
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

// set the width and height of the canvas
const w = canvas.width = document.body.offsetWidth;
const h = canvas.height = document.body.offsetHeight;

// draw a black rectangle of width and height same as that of the canvas
ctx.fillStyle = '#000';
ctx.fillRect(0, 0, w, h);

const cols = Math.floor(w / 20) + 1;
const ypos = Array(cols).fill(0);

function matrix () {
  // Draw a semitransparent black rectangle
  ctx.fillStyle = '#0001';
  ctx.fillRect(0, 0, w, h);

  // Set color
  const randomColor = Math.floor(Math.random()*16777215).toString(16)
  ctx.fillStyle = '#0f0';
  ctx.font = '20pt monospace';

  // for each column put a random character at the end
  ypos.forEach((y, ind) => {
    // generate a random character
    const text = String.fromCharCode(Math.random() * 122);

    // x coordinate of the column, y coordinate is already given
    const x = ind * 20;
    // render the character at (x, y)
    ctx.fillText(text, x, y);

    // randomly reset the end of the column if it's at least 100px high
    if (y > 100 + Math.random() * 10000) ypos[ind] = 0;
    // otherwise just move the y coordinate for the column 20px down,
    else ypos[ind] = y + 20;
  });
}

// 20 FPS.
setInterval(matrix, 50);