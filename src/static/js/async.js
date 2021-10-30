
function WordDictionary(input_json){   
        var word_list = [];
       
 
        var n = 0;
        for (var key in input_json) {
            n++;
        }
        for (var i = 0; i < n; i++) {
            var temp = input_json[i];
            word_list.push(temp['new_string']);
            }
        var wordString = word_list.join(' '); 
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
            temp_string.push("<button type='button' class='btn btn-light hl_faded' id='word"+ temp['id'] + "\'" + "onmouseover='show_correct("+ temp['id'] +")' onclick='corrector("+temp['id']+")'>"+temp['correct']+"</button>");

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
        xml.onload = function(){
            var dataReply = JSON.parse(xml.responseText) ;// checked_text
            // document.getElementById("Text_display").innerHTML = dataReply.checked_text;
            // console.log(dataReply);

            var html_string = WordDictionary(dataReply.checked_text);
            console.log("called from inside async\n"+html_string);
            var corrected_string = ShowMisspelled(dataReply.checked_text);
            // console.log("HTML String" + html_string);
            document.getElementById("Text_box").innerHTML = html_string;
            document.getElementById("Text_display").innerHTML = corrected_string;

    };
    dataSend = JSON.stringify({
        'input_text' : textData,
        'language_selector' : languageSelector,
        'formality_selector' : formalitySelector
    });
    xml.send(dataSend)

    event.preventDefault();
};



function async_correction(input_id){
    var element_id = input_id;    

      var xml2 = new XMLHttpRequest();
      xml2.open("POST", "/correct", true);
      xml2.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
      xml2.onload = function(){
          var dataReply = JSON.parse(xml2.responseText) ;// checked_text
          console.log(dataReply.checked_text);

          var html_string = WordDictionary(dataReply.checked_text);
          var corrected_string = ShowMisspelled(dataReply.checked_text);

        //   console.log("HTML String" + html_string);
          document.getElementById("Text_box").innerHTML = html_string;
          document.getElementById("Text_display").innerHTML = corrected_string;


  };
  dataSend = JSON.stringify({
      'element_id' : element_id,
  });
  xml2.send(dataSend)

  event.preventDefault();
};




