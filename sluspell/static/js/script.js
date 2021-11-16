/////------------------------------------------------------------------------

function show_popup(input_id, correct_word) { // field_ID
  let new_id = "pop-up" + input_id;
  document.getElementById(new_id).classList.remove('hide');
  document.getElementById(new_id).classList.add('show');
  setTimeout('',2000);
  
};

function hide_popup(input_id, correct_word){
  let new_id = "pop-up" + input_id;
  setTimeout(function(){
    document.getElementById(new_id).classList.remove('show');
    document.getElementById(new_id).classList.add('hide');
  }  
  ,3000);
};



/////------------------------------------------------------------------------

function show_correct(input_id) { // field_ID
  let new_id = "word" + input_id;
  let element = document.getElementsByClassName(new_id);
  [].forEach.call(element, function(el) {
    el.classList.remove("hl_faded");
    el.classList.add("hl_focused");
  });

  // element.classList.remove("hl_faded");
  // element.classList.add("hl_focused");

  // document.getElementsByClassName(new_id).classList.remove('hl_faded');
  // document.getElementsByClassName(new_id).classList.add('hl_focused');
  // document.getElementById(new_id).classList.remove('hl_faded');
  // document.getElementById(new_id).classList.add('hl_focused');
  setTimeout('',4000);
  
}; 

function hide_correct(input_id){
  let new_id = "word" + input_id; 
  try {
    setTimeout(function(){
      document.getElementById(new_id).classList.remove('hl_focused');
      document.getElementById(new_id).classList.add('hl_faded');
    }  
    ,2000);
  }catch (e) {
    // console.log(e.message)
  }

};

/////------------------------------------------------------------------------


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


// document
// .querySelector("#Text_box")
// .addEventListener("keyup", function countWord() {
//   let res = [];
//   let str = this.value.replace(/[\t\n\r\.\?\!]/gm, " ").split(" ");
//   str.map((s) => {
//     let trimStr = s.trim();
//     if (trimStr.length > 0) {
//       res.push(trimStr);
//     }
//   });
//   document.querySelector("#word_count").innerText = res.length;
// });


/////------------------------------------------------------------------------
//// typingindicator


var TYPE_FLAG_BOOL = 0 ; 
let timer,
		timeoutVal = 1000;

const label = document.getElementById('indicator');
const typing = document.getElementById('Text_box');

typing.addEventListener('keypress', handleKeyPress);
typing.addEventListener('keyup', handleKeyUp);

function handleKeyPress(e) {
	window.clearTimeout(timer);
  if (TYPE_FLAG_BOOL ==1){
    TYPE_FLAG_BOOL =0 ;
  }
  label.innerHTML = '<p class="typing">Typing<span>.</span><span>.</span><span>.</span></p>';
}

function handleKeyUp(e) {
	window.clearTimeout(timer);

  
	timer = window.setTimeout(() => {
  	label.innerHTML = ''; //'<p class="typing"><span>.</span><span>.</span><span>.</span></p>';
    if (TYPE_FLAG_BOOL ==0){
      TYPE_FLAG_BOOL =1 ;
      call_async();
    }
  }, timeoutVal);
}


function fix_cursor(input_element, input_string) {
  input_element.focus();
  // input_element.setSelectionRange(input_string.length, input_string.length);
  input_element.setSelectionRange = (input_string.length, input_string.length);
}


function positionCursor() {
              
  var tag = document.getElementById("Text_box");  
  // Creates range object
  var setpos = document.createRange();    
  // Creates object for selection
  var set = window.getSelection();    
  // Set start position of range
  setpos.setStart(tag, tag.textContent.length);    
  // Collapse range within its boundary points
  // Returns boolean
  setpos.collapse(true);    
  // Remove all ranges set
  set.removeAllRanges();    
  // Add range with respect to range object.
  set.addRange(setpos);    
  // Set cursor on focus
  tag.focus();
}


function call_async(){
  async();
  // var tag = document.getElementById("Text_box");  
  // fix_cursor(tag, tag.innerHTML);

  // fix_cursor(input_element,input_element.innerHTML);
}


function corrector(input_id,  word_index){
  // hide_correct(input_id);
  async_correction(input_id, word_index);
  // call_async();

};

// ================================

function copyToClipboard() {
    let textarea = document.getElementById("Text_box");
    if(textarea.textContent == ""){
      return
    }else{
      /* Select the text field */
      // textarea.select();
      // textarea.setSelectionRange(0, 99999); /* For mobile devices */

      /* Copy the text inside the text field */
      navigator.clipboard.writeText(textarea.textContent);
  }
};