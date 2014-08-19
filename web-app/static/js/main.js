//has to be bound to pages + buttons
//really this is entirely bindings, it doesn't
//do anything at all unless attached to something
function swapPage (page) {
    //change button styles
    $("nav button").removeClass("shown");
    $("nav button"+page).addClass("shown")
    //get rid of a thing
    leaving = $("article.shown")
    leaving.addClass("fadeOutDownBig");
    leaving.removeClass("fadeInDownBig");
    leaving.removeClass("shown")
    //bring in another thing
    coming = $("article"+page)
    coming.removeClass("none")
    coming.addClass("fadeInDownBig");
    coming.removeClass("fadeOutDownBig");
    coming.addClass("shown")
    window.setTimeout(function() {
        leaving.addClass("none") //dont show the thing that just left
        coming.removeClass("none") //unless it didnt actually leave
    },1000);
}
//gets url query strings
function getQueryVariable(variable)
{
       var query = window.location.search.substring(1);
       var vars = query.split("&");
       for (var i=0;i<vars.length;i++) {
               var pair = vars[i].split("=");
               if(pair[0] == variable){return pair[1];}
       }
       return(0);
}
//changes to that page 
$(document).ready(function () {
    var qString = "."+String(getQueryVariable("page"))
    if (qString!=0) {
        swapPage(qString);
    }
});