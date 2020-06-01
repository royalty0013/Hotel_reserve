var DeluxeSuite  = 120000;  
var TwinRoomWithSeaview = 150000;
var DoubleRoom  = 130000;
var SingleRoom  = 70000;

var daysDifference = 1

$( document ).ready(function() {
  $( "#dep_date" ).change(function() {
    var valDep = $('#dep_date').val();
    var valArv = $('#arval_date').val();
    console.log(valDep);
    console.log(valArv);
    var dep=Math.round(new Date(valDep).getTime()/1000);
    var arv=Math.round(new Date(valArv).getTime()/1000);
    var difference = dep - arv;
    daysDifference = Math.ceil(difference/60/60/24);

    console.log(daysDifference);
    updatePrice();

  });
    
});


$('#room_type').change(function(){
  updatePrice();
});

function updatePrice(){
  if (document.getElementById('room_type').value == "Deluxe Suite") {
    document.getElementById("no_days").value = daysDifference;
    document.getElementById("spanprice").textContent = DeluxeSuite*daysDifference;
    document.getElementById('price').value = document.getElementById('spanprice').innerHTML;
  }
  if (document.getElementById('room_type').value == "Twin Room With Seaview") {
    document.getElementById("no_days").value = daysDifference;
    document.getElementById("spanprice").textContent = TwinRoomWithSeaview*daysDifference;
    document.getElementById('price').value = document.getElementById('spanprice').innerHTML;
  }
  if (document.getElementById('room_type').value == "Double Room") {
    document.getElementById("no_days").value = daysDifference;
    document.getElementById("spanprice").textContent = DoubleRoom*daysDifference;
    document.getElementById('price').value = document.getElementById('spanprice').innerHTML;
  }
  if (document.getElementById('room_type').value == "Single Room") {
    document.getElementById("no_days").value = daysDifference;
    document.getElementById("spanprice").textContent = SingleRoom*daysDifference;
    document.getElementById('price').value = document.getElementById('spanprice').innerHTML;
  }
}