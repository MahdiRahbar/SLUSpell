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
  document.getElementById(new_id).classList.remove('hl_faded');
  document.getElementById(new_id).classList.add('hl_focused');
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


function call_async(){
  async();
}


function corrector(input_id,  word_index){
  // hide_correct(input_id);
  async_correction(input_id, word_index);
  // call_async();

};


// class WordDictionary{

//   constructor(inputJSON){
//     this.inputJSON=inputJSON;
//     this.word_list = []; 
//   }

//   buildWordList(){
//     for (let i = 0; i < this.inputJSON.length; i++) { 
//       console.log(this.inputJSON[i]);
//       var temp = this.inputJSON[i];
//       this.word_list.push(temp['new_string']);;
//     }
//   }

//   toString(){
//     let wordString = a.join(); 
// }
// }