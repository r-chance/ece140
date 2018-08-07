function button1() {
 
  var x = entries[0];
  var bn;
  var bt;
  var job;
  var rev;

  bn = x[0]; 
  bt = x[1];
  job = x[2];
  rev = x[3];
 
  document.getElementById("amazon").innerHTML = "TEST";
  var x = document.getElementById("amazon");
  if (x.style.display ==="none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
} 


