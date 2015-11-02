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
                        var overview = $(that).siblings('.overview');
                        overview.append(e);
                        e.slideDown("slow");
                        setTimeout(function () {
                            if(overview.find('.get_more_empty').size()){
                                $(that).hide();
                                $(that).next().show();
                            }
                        },500);

                    };
            }(this)
    )})};

var recoverInTags = function(){$(".recover")
    .click(function () {
        var overview = $(this).siblings('.overview');
        var container = overview.children().slice(3).slideUp('slow');
        setTimeout(function() {
            container.remove();
        },600)
        $(this).hide().prev().show();
    })
    
}

getMorePagesInTags();
recoverInTags();