/**
 * Created by fengyu on 15/10/18.
 */

var boundClick = function(){$(".page").click(function(){
   window.location.href = $(this).find("a").attr("href");
    //$(this).find("a")[0].click();
   return false;
})};



var boundGetmore = function(){$(".get_more")
    .click(function(){
        $.get("/blog/get_more?id="+$(".page").last().attr('id'),
            function(data,status){
                var e = $(data);
                e.hide();
                $(".items").append(e);
                e.slideDown("slow");
                boundClick();
            })
    })};


$(document).ready(boundClick);
$(document).ready(boundGetmore);
