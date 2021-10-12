
function async(){
      var textData = document.getElementById("Text_box").value;
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