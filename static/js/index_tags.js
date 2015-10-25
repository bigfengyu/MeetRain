/**
 * Created by fengyu on 15/10/22.
 */



var getMorePagesInTags = function(){$(".get_more")
    .click(function(){
        $.get(
            function(e){
                var lastPageID = $(e).prev().find('a').last().attr('page-id');
                var lastTagID = $(e).parent('.tagitem').attr('data-tag-id');
                var url =  "/blog/tags/get_more?pageid="+lastPageID+"&tagid="+lastTagID;
                return url;
            }(this),
            function(that){
                return function(data,status){
                        var e = $(data);
                        e.hide();
                        $(that).siblings('.overview').append(e);
                        e.slideDown("slow").css("display","block");
                    };
            }(this)
    )})};

getMorePagesInTags();