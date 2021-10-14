
function async(){
      var textData = document.getElementById("Text_box").textContent;
      var languageSelector = document.getElementById("Language_Selection").value;
      var formalitySelector = document.getElementById("Formality_Selection").value;
      

        var xml = new XMLHttpRequest();
        xml.open("POST", "/check", true);
        xml.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xml.onload = function(){
            var dataReply = JSON.parse(xml.responseText) ;// checked_text
            console.log(dataReply.checked_text);
            document.getElementById("Text_display").innerHTML = dataReply.checked_text;

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
          document.getElementById("Text_display").innerHTML = dataReply.checked_text;

  };
  dataSend = JSON.stringify({
      'element_id' : element_id,
  });
  xml2.send(dataSend)

  event.preventDefault();
};