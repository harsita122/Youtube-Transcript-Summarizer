
console.log("Content script running...");

chrome.runtime.sendMessage({todo: "showPageAction"});

// chrome.runtime.onMessage.addListener(
//     function(message){
//         alert(message);
//         console.log(message);
//     });

// chrome.runtime.onClicked.addListener(async () => {
//     let url = chrome.runtime.getURL("popup.html");
//     let tab = await chrome.tab.create({url})
// })

