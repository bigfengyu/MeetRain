/**
 * Created by fengyu on 15/10/18.
 */

$(".page").click(function(){
   window.location=$(this).find("a").attr("href");
   return false;
})
