console.log("Background script running...");

chrome.runtime.onMessage.addListener(function(request, sender, sendResponse){
    if ( request.todo == "showPageAction")
    {
        chrome.tabs.query({active:true, currentWindow: true}, function(tabs){
            chrome.pageAction.show(tabs[0].id);
        })
    }
    else{
        chrome.tabs.query({active:true, currentWindow: true}, function(tabs){
            chrome.pageAction.hide(tabs[0].id);
        })
    }
})



// chrome.runtime.onInstalled.addListener(
//     function()
//     {
//         chrome.declarativeContent.onPageChanged.removeRules(undefined,function()
//         {
//             chrome.declarativeContent.onPageChanged.addRules([
//                 {
//                     conditions: [
//                         new chrome.declarativeContent.PageStateMatcher({               //this does the feature of matching
//                             pageUrl: { urlContains: "https://www.youtube.com/watch?v=" },
//                         })
//                     ],
//                     actions: [new chrome.declarativeContent.ShowPageAction() ]
//                 }
//             ]);
//         });
//     });

// const iconRules = [{
//     conditions: [
//         new chrome.declarativeContent.PageStateMatcher({
//             pageUrl: {hostEquals: 'youtube.com'},
//         })
//     ],
//     actions: [new chrome.declarativeContent.ShowPageAction()]
// }];
// chrome.pageAction.onClicked.addListener(function(){
//     chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
//         chrome.tabs.sendMessage(tabs[0].id, {action: "REPLACE_TEXT"});
//         })
//     });