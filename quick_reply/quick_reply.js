//menu
chrome.contextMenus.create({
    id: "quickReplyFunction",
    title: "Quick Reply",
    contexts: ["editable"]
});

// Create a submenu item
chrome.contextMenus.create({
    parentId: "quickReplyFunction", // ID of the parent menu item
    id: "genericReply",
    title: "Generic Reply",
    contexts: ["editable"]
});

chrome.contextMenus.create({
    parentId: "quickReplyFunction", // ID of the parent menu item
    id: "noReply",
    title: "Voicemail",
    contexts: ["editable"]
});

chrome.contextMenus.create({
    parentId: "quickReplyFunction", // ID of the parent menu item
    id: "spamReply",
    title: "Spam Reply",
    contexts: ["editable"]
});

chrome.contextMenus.create({
    parentId: "quickReplyFunction", // ID of the parent menu item
    id: "completedWork",
    title: "Finished",
    contexts: ["editable"]
});

//testing
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action = "testInfo") {
        console.log(message.data);
    }
});

//functions
//Need to move to activeElement.js
// function Getname () {
//     ticketname = document.getElementById("ticket_c_person_reporting")
//     fname = ticketname.split("")[0];
//     return fname;
// }

function Greeting() {
    var time = new Date();
    var hour = time.getHours();
    //var name = Getname();
    if (hour<12) {
        return "Good Morning ,\n";
    } else if (hour>17) {
        return "Good Evening ,\n";
    } else {
        return "Good Afternoon,\n";
    }
}

//sends the data to activeElement.js
chrome.contextMenus.onClicked.addListener((info, tab) => {
    if (info.menuItemId === "genericReply") {
        chrome.tabs.sendMessage(tab.id, {
            actionType: "Reply",
            content: Greeting() + "Thank you for letting us know about _____. We will have an engineer reach out to assist with troubleshooting this issue.\n\n-Mike Dixon"
        });     
    }
    if (info.menuItemId === "noReply") {
        chrome.tabs.sendMessage(tab.id, {
            actionType: "Reply",
            content: Greeting() + "I gave you a call but also wanted to reach out here. If you could please give me a call at 301-941-1444 x717 when you have a moment.\n\n-Mike Dixon"
        });
    }
    if (info.menuItemId === "spamReply") {
        chrome.tabs.sendMessage(tab.id, {
            actionType: "Reply",
            content: Greeting() + "Thank you for letting us know about this spam. We have blocked the domain ____. Please let us know if you need additional assistance.\n\n-Mike Dixon"
        });
    }
    if (info.menuItemId === "completedWork") {
        chrome.tabs.sendMessage(tab.id, {
            actionType: "Reply",
            content: Greeting() + "Thank you for speaking with me and giving me time to troubleshoot the issue. If you need additional assistance please give me a call at 301-941-1444 x717\n\n-Mike Dixon"
        });
    }
});




   