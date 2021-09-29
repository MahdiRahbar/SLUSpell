var $firstButton = $(".first"),
  $secondButton = $(".second"),
  $input = $("input"),
  $name = $(".name"),
  $more = $(".more"),
  $yourname = $(".yourname"),
  $reset = $(".reset"),
  $ctr = $(".container");

$firstButton.on("click", function(e){
  $(this).text("Saving...").delay(900).queue(function(){
    $ctr.addClass("center slider-two-active").removeClass("full slider-one-active");
  });
  e.preventDefault();
});

$secondButton.on("click", function(e){
  $(this).text("Saving...").delay(900).queue(function(){
    $ctr.addClass("full slider-three-active").removeClass("center slider-two-active slider-one-active");
    $name = $name.val();
    if($name == "") {
      $yourname.html("Anonymous!");
    }
    else { $yourname.html($name+"!"); }
  });
  e.preventDefault();
});

// copy
balapaCop("Step by Step Form", "#999");
/////
////
/////


function edit_enable(){
  
  // document.getElementById("spell_check_btn").classList.add('disabled');
  // document.getElementById("edit_btn").classList.remove('disabled');
}
function spell_check_enable(){
  // document.getElementById("edit_btn").classList.add('disabled');
  // document.getElementById("spell_check_btn").classList.remove('disabled');
}

function popup_function() {
  var popup = document.getElementById("pop-up");
  popup.classList.toggle("show");
}


function highlight(text) {
  var innerHTML = document.getElementById("Text_box").value;
  // var innerHTML = inputText.innerHTML;
  var index = innerHTML.indexOf(text);
  if (index >= 0) { 

  innerHTML = innerHTML.substring(0,index) + "<span class='highlight popup' onclick='popup_function()'><span class='popuptext' id='pop-up'>This</span>" + innerHTML.substring(index,index+text.length) + "</span></span>" + innerHTML.substring(index + text.length);

  }
  
  document.getElementById("Text_display").innerHTML = innerHTML;

  edit_enable();
}




