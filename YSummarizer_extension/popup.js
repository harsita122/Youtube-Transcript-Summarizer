
$(function(){
    chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {
        let url = tabs[0].url;
        chrome.storage.sync.set({link1 : url});
    });
    $('#as').click(function(){
        // alert("as is clicked");
        chrome.storage.sync.get('link1',function(video){
            var url = "http://127.0.0.1:5000/abstractivesummarizer/" + video.link1 ;
            var callobject = {
                "url" : url,
                "type" : "popup",
                "width" : screen.availWidth/2,
                "height" : screen.availHeight/2,
                "top" : 5,
                "left" : 5
            };
            chrome.windows.create(callobject, function(){})
        });
    })
    $('#es').click(function(){
        // alert("es is clicked");
        chrome.storage.sync.get('link1',function(video){
            var url = "http://127.0.0.1:5000/extractivesummarizer/" + video.link1 ;
            var callobject = {
                "url" : url,
                "type" : "popup",
                "width" : screen.availWidth/2,
                "height" : screen.availHeight/2,
                "top" : 5,
                "left" : 5
            };
            chrome.windows.create(callobject, function(){})
        });
    })
    
})