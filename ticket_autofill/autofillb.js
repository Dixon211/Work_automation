var jsonData;
fetch('clients.json')
    .then(response => response.json())
    .then(data => {
        console.log("clients.JSON is loaded");
        jsonData = data;
    })

function compareEmail(email, jsonData) {
    var result = "no matches for this domain";
    var data = null;
    for (var key in jsonData) {
        var value = jsonData[key];
        for (var i =0; i < value.length; i++) {
            var ele = value[i];
            if (ele.hasOwnProperty("email") && email == ele.email) {
                    data = ele;
                    data["id"] = key;
                    return data;
            }
        } 
    }
    return result;
}
   





chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if(request.email && request.domain && jsonData){
        rep = compareEmail(request.email, jsonData);
        sendResponse(rep);
    } else {
        var rep = "I didn't get em";
        sendResponse(rep);
    }
});

