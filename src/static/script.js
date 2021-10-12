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

/////------------------------------------------------------------------------

function popup_function() { // field_ID
  document.getElementById("pop-up").classList.add('show');
//   popup.addEventListener("pop-up", function( event ) { 
//     document.getElementById("pop-up").classList.remove('show');
// });
};



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

/////------------------------------------------------------------------------
//// typingindicator

let timer,
		timeoutVal = 1000;

const label = document.getElementById('indicator');
const typing = document.getElementById('Text_box');

typing.addEventListener('keypress', handleKeyPress);
typing.addEventListener('keyup', handleKeyUp);

function handleKeyPress(e) {
	window.clearTimeout(timer);
  label.innerHTML = '<p class="typing">Typing<span>.</span><span>.</span><span>.</span></p>';
}

function handleKeyUp(e) {
	window.clearTimeout(timer);
	timer = window.setTimeout(() => {
  	label.innerHTML = '<p class="typing">Not Typing<span>.</span><span>.</span><span>.</span></p>';
  }, timeoutVal);
}

