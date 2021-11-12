
function WordDictionary(input_json){   
        let word_list = [];
       
 
        let n = 0;
        for (let key in input_json) {
            n++;
        }
        for (let i = 0; i < n; i++) {
            let temp = input_json[i];
            word_list.push(temp['new_string'].replace(/ /g, '\u00a0')); // &nbsp;   
            }

             
        let wordString = word_list.join(''); 
        return wordString;   
  };


function ShowMisspelled(input_json){
    var word_id = [];
    var word_list = [];
    var temp_string = [];
    var n = 0;

    for (var key in input_json) {
        n++;
    }
    for (var i = 0; i < n; i++) {
        var temp = input_json[i];
        if (temp['correction_flag'] == true){
            word_list.push(temp['correct']);   
            word_id.push(temp['id']);
            // temp_string.push("<a class='hl_faded' id='word"+ temp['id'] + "\'" + "onmouseover='show_correct("+ temp['id'] +")' onclick='corrector("+temp['id']+")'>"+temp['correct']+"<a>");
            console.log(temp);
            var new_string= '';
            for (var j = 0; j < temp['correct'].length; j++) {
                new_string = new_string + "<button type='button' class='btn btn-light word"+temp['id']+ " hl_"+j+" hl_faded' id='word"+ temp['id']+ "\'" + "onmouseover='show_correct("+ temp['id'] +")' onclick='corrector("+temp['id']+"," +j + ")'>"+temp['correct'][j]+"</button>" + "</br>";
                    
                }  
                temp_string.push(new_string);  
            }
        }
    var correct_string = temp_string.join('<br>'); 
    return correct_string;   
};





function async(){
      var textData = document.getElementById("Text_box").textContent;
      var languageSelector = document.getElementById("Language_Selection").value;
      var formalitySelector = document.getElementById("Formality_Selection").value;
      

        var xml = new XMLHttpRequest();
        xml.open("POST", "/check", true);
        xml.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xml.onload = function(event){
            var dataReply = JSON.parse(xml.responseText) ;// checked_text
            // document.getElementById("Text_display").innerHTML = dataReply.checked_text;
            // console.log(dataReply);
            console.log(dataReply.checked_text);

            let html_string = WordDictionary(dataReply.checked_text);
            console.log("called from inside async\n"+html_string);
            let corrected_string = ShowMisspelled(dataReply.checked_text);
            // console.log("HTML String" + html_string);
            document.getElementById("Text_box").innerHTML = html_string;
            document.getElementById("Text_display").innerHTML = corrected_string;

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
    xml.send(dataSend)
    

    // event.preventDefault();
};



function async_correction(input_id, word_index){
    var element_id = input_id;    
    var list_index = word_index;

      var xml2 = new XMLHttpRequest();
      xml2.open("POST", "/correct", true);
      xml2.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
      xml2.onload = function(event){
          var dataReply = JSON.parse(xml2.responseText) ;// checked_text
          console.log(dataReply.checked_text);

          var html_string = WordDictionary(dataReply.checked_text);
          var corrected_string = ShowMisspelled(dataReply.checked_text);

        //   console.log("HTML String" + html_string);
          document.getElementById("Text_box").innerHTML = html_string;
          document.getElementById("Text_display").innerHTML = corrected_string;

          event.preventDefault();
  };
  dataSend = JSON.stringify({
      'element_id' : element_id,
      'list_index' : list_index
  });
  xml2.send(dataSend)
//   event.preventDefault();
  
};




