function handleClick(event) {
    console.log("Mouse button clicked!");
    var activeele = findactiveele();
    var output_data = null;
    if (activeele=== "edit_ticket_toolbar") {
        console.log("the pressed button was the edit button");
        userele = document.getElementById("ticket_submitted_by_email");
        useremail = userele.value;
        userlist = useremail.split("@");
        userdomain = userlist[1];
        chrome.runtime.sendMessage({email: useremail, domain: userdomain}, (response) => {
            console.log("sent the email info");
            console.log("Heres the response: ", JSON.stringify(response));
            output_data = response;
            if (output_data && output_data != "no matches for this domain") {
                editboxelements(output_data);
            }
        });
        
        
    } else {
        console.log("the pressed button was not the edit button")
    }
  }


  function editboxelements(output_data) {
    console.log("starting editboxelements")
    summaryBox = document.getElementById("ticket_summary_edit_field");
    clientCBox = document.getElementById("ticket_c_client_code");
    pwissueBox = document.getElementById("ticket_c_person_with_issue");
    preportBox = document.getElementById("ticket_c_person_reporting");
    if (summaryBox.value.includes("-")) {

    } else {
        summaryBox.value = output_data["id"] + " - " + summaryBox.value;
    }
    if (clientCBox.value === ""){
        clientCBox.value = output_data["id"]
    } else { 
    }
    if (pwissueBox.value === ""){
        pwissueBox.value = output_data['fname'] + " " + output_data['lname']
    } else {
    }
    if (preportBox.value === "") {
        preportBox.value = output_data['fname'] + " " + output_data['lname']
    } else {
    }
    console.log("completed editboxelements")
  }



function findactiveele() {
    var activeele = document.activeElement.id;
    console.log("The selected element is: " + activeele);
    return activeele;
}




document.addEventListener("click", handleClick);


