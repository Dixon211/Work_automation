//content script
//edits the actual webpage
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if(message.actionType === "Reply") {
     var elementID = document.activeElement.id;
     var realElement = document.getElementById(elementID);
     realElement.value = message.content;
  }
});


