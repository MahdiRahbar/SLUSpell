bandi
#7275



Direct Message
Schmidtologist
Search

September 13, 2021
 
Schmidtologist — 09/13/2021
Nothing for this sprint, except learning Python
September 14, 2021
 
bandi — 09/14/2021
Okay 👍🏻
September 25, 2021
 
bandi — 09/25/2021
Hey Mahdi , the code hasn’t finished yet for me to get the update . I can add the typing indicator when the code is finished
October 4, 2021
 
bandi — 10/04/2021
Hey Mahdi , which branch should I commit my changes into ?
 
Schmidtologist — 10/04/2021
Hey, 
You should make a branch on your local with any name and then make a PR to the project Main branch
 
bandi — 10/04/2021
There has been few conflicts in my repository ..I’ll delete the whole repository and do it from scratch ..then I’ll commit my changes to main repository..is that fine ??
 
bandi — 10/04/2021
I’m done with the code .. due to certain issues with my laptop ,I’ll upload it by tomorrow
October 5, 2021
 
Schmidtologist — 10/05/2021
ok
November 14, 2021
 
bandi — Yesterday at 7:06 PM
Hey  Mahdi , couldn’t see the comments you’ve left .. can you help me out
 
Schmidtologist — Yesterday at 7:06 PM
Hey Bandi
[7:06 PM]
here you are
[7:06 PM]
https://github.com/MahdiRahbar/SLUSpell/pull/34
GitHub
Copy button added by Bandisaiprasad · Pull Request #34 · MahdiRahba...
Image
November 15, 2021
 
Schmidtologist — Today at 7:12 PM
Bandi?
[7:12 PM]
Are you there?
 
bandi — Today at 7:12 PM
Yes
 
Schmidtologist — Today at 7:13 PM
Are you home yet?
[7:13 PM]
Did you update the repo?
 
bandi — Today at 7:15 PM
I’m doing it bro
 
Schmidtologist — Today at 7:15 PM
ok. let me know when you're done
 
Schmidtologist — Today at 8:18 PM
Bandi
[8:18 PM]
are you still doing it?
[8:18 PM]
whats up?
 
bandi — Today at 8:19 PM
I just picked up my laptop, I’ll let you know once it’s done
 
Schmidtologist — Today at 8:20 PM
Please work on it. I have also other things to do.
[8:20 PM]
let's get it done as soon as possible
 
Schmidtologist — Today at 10:05 PM
Bandi? I'm still waiting
[10:05 PM]
Did you update it?
 
bandi — Today at 10:06 PM
I’m  trying but it’s not working..but I’ll raise a pull request  of the updated copy button I.e javascript css and html ..can you update it please ??
 
Schmidtologist — Today at 10:07 PM
What's the error?
[10:07 PM]
Why it's not working?
[10:07 PM]
I can't update it myself.
[10:07 PM]
If I update it, that wouldn't have your name on it
[10:07 PM]
I want you to do it
[10:08 PM]
Tell me what part you're stuck so I can help you with
 
bandi — Today at 10:08 PM
The copy button  is not visible even thought I change the colour
 
Schmidtologist — Today at 10:09 PM
Bandi
[10:09 PM]
Forget about that
[10:09 PM]
I don't want you to do anything right now
[10:09 PM]
just update the repository
[10:09 PM]
get the last one
[10:09 PM]
that's all I want from you
 
bandi — Today at 10:12 PM
I updated my repository
 
Schmidtologist — Today at 10:13 PM
good
[10:14 PM]
are you on your computer right now?
 
bandi — Today at 10:14 PM
Yes bro
 
Schmidtologist — Today at 10:14 PM
ok,
[10:14 PM]
give me a moment
[10:14 PM]
<!doctype html>
<html lang="en">
  <head>
  	<title>SLUSpell</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
Expand
index.html
6 KB

Schmidtologist
Click to see attachment
 
Schmidtologist — Today at 10:15 PM
download this file and copy and paste it directly to this directory: 
SLUSpell\sluspell\templates
[10:15 PM]
let me know when you did it
 
bandi — Today at 10:19 PM
yeah ok mahdi
 
Schmidtologist — Today at 10:19 PM
did you copy it?
 
bandi — Today at 10:19 PM
i have copied it
[10:19 PM]
i'm pushing it to right bow
[10:20 PM]
now
 
Schmidtologist — Today at 10:20 PM
no
[10:20 PM]
wait a second
[10:20 PM]
/////------------------------------------------------------------------------

function show_popup(input_id, correct_word) { // field_ID
  let new_id = "pop-up" + input_id;
  document.getElementById(new_id).classList.remove('hide');
  document.getElementById(new_id).classList.add('show');
Expand
script.js
6 KB
[10:20 PM]
copy this one in : SLUSpell\sluspell\static\js
[10:20 PM]
/*!
 * Bootstrap v4.3.1 (https://getbootstrap.com/)
 * Copyright 2011-2019 The Bootstrap Authors
 * Copyright 2011-2019 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 */
... (203 KB left)
Expand
style.css
253 KB
[10:20 PM]
and this one in: SLUSpell\sluspell\static\css
[10:21 PM]
make a branch called dev_interface   and then push it
[10:21 PM]
then make a PR
[10:22 PM]
whenever you got stuck let me know
 
bandi — Today at 10:22 PM
yes okay
 
Schmidtologist — Today at 10:22 PM
I'm waiting so I can merge your code in tonight
 
bandi — Today at 10:22 PM
yeah okay I'm doing it
 
Schmidtologist — Today at 10:22 PM
Thanks buddy


Message @Schmidtologist
﻿




 to select
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
script.js
6 KB
