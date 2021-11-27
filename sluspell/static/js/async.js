
function WordDictionary(input_json){   
        let word_list = [];
       
 
        let n = 0;
        for (let key in input_json) {
            n++;
        }
        for (let i = 0; i < n; i++) {
            let temp = input_json[i];
            if (temp['correction_flag']){
              word_list.push(temp['new_string']); // &nbsp;    .replace(/ /g, '\u00a0')

            }else{
              word_list.push(temp['new_string'].replace(/ /g, '\u00a0')); // &nbsp;    
            }
              
            }

             
        let wordString = word_list.join(''); 
        return wordString;   
  };


function ShowMisspelled(input_json){
    let word_id = [];
    let word_list = [];
    let temp_string = [];
    let n = 0;

    for (let key in input_json) {
        n++;
    }
    for (let i = 0; i < n; i++) {
        let temp = input_json[i];
        if (temp['correction_flag'] == true){
            word_list.push(temp['correct']);   
            word_id.push(temp['id']);
            // temp_string.push("<a class='hl_faded' id='word"+ temp['id'] + "\'" + "onmouseover='show_correct("+ temp['id'] +")' onclick='corrector("+temp['id']+")'>"+temp['correct']+"<a>");
            // console.log(temp);
            let new_string= '';
            for (let j = 0; j < temp['correct'].length; j++) {
                new_string = new_string + "<button type='button' class='btn btn-light word"+temp['id']+ " hl_"+j+" hl_faded' id='word"+ temp['id']+ "\'" + "onmouseover='show_correct("+ temp['id'] +")' onclick='corrector("+temp['id']+"," +j + ")'>"+temp['correct'][j]+"</button>" + "</br>";
                    
                }  
                temp_string.push(new_string);  
            }
        }
    let correct_string = temp_string.join('<br>'); 
    return correct_string;   
};



  function placeCaretAtEnd(el) {
    el.focus();
    if (typeof window.getSelection != "undefined" &&
      typeof document.createRange != "undefined") {
      var range = document.createRange();
      range.selectNodeContents(el);
      range.collapse(false);
      var sel = window.getSelection();
      sel.removeAllRanges();
      sel.addRange(range);
    } else if (typeof document.body.createTextRange != "undefined") {
      var textRange = document.body.createTextRange();
      textRange.moveToElementText(el);
      textRange.collapse(false);
      textRange.select();
    }
  }



function async(){
      let textData = document.getElementById("Text_box").textContent;
      let languageSelector = document.getElementById("Language_Selection").value;
      let formalitySelector = document.getElementById("Formality_Selection").value;
      

        let xml = new XMLHttpRequest();
        xml.open("POST", "/check", true);
        xml.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xml.onload = function(event){
            let dataReply = JSON.parse(xml.responseText) ;// checked_text
            // document.getElementById("Text_display").innerHTML = dataReply.checked_text;
            // console.log(dataReply);
            // console.log(dataReply.checked_text);

            let html_string = WordDictionary(dataReply.checked_text);
            // console.log("called from inside async\n"+html_string);
            let corrected_string = ShowMisspelled(dataReply.checked_text);
            // console.log("HTML String" + html_string);

            
            document.getElementById("Text_box").innerHTML = html_string;
            document.getElementById("Text_display").innerHTML = corrected_string;
            placeCaretAtEnd(document.getElementById("Text_box"));

            REQUEST_STATUS = true ; 

            // let input_element = document.getElementById("Text_box");
            // input_element.focus();
            // input_element.selectionStart = input_element.selectionEnd = input_element.innerHTML.length;

            event.preventDefault();

    };
    dataSend = JSON.stringify({
        'input_text' : textData,
        'language_selector' : languageSelector,
        'formality_selector' : formalitySelector
    });
    // REQUEST_STATUS = false; 
    xml.send(dataSend)
    

    // event.preventDefault();
};



function async_correction(input_id, word_index){
    let element_id = input_id;    
    let list_index = word_index;

      let xml2 = new XMLHttpRequest();
      xml2.open("POST", "/correct", true);
      xml2.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
      xml2.onload = function(event){
          let dataReply = JSON.parse(xml2.responseText) ;// checked_text
          // console.log(dataReply.checked_text);

          let html_string = WordDictionary(dataReply.checked_text);
          let corrected_string = ShowMisspelled(dataReply.checked_text);

        //   console.log("HTML String" + html_string);
          document.getElementById("Text_box").innerHTML = html_string;
          document.getElementById("Text_display").innerHTML = corrected_string;
          REQUEST_STATUS = true ; 

          event.preventDefault();
  };
  dataSend = JSON.stringify({
      'element_id' : element_id,
      'list_index' : list_index
  });
  // REQUEST_STATUS = false; 
  xml2.send(dataSend)
  
//   event.preventDefault();
  
};




