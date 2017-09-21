/**
 * Created by dell on 2017/1/12.
 */

//使用jquery扩展需要包进匿名函数里
(function (arg) {
    arg.extend({
       'Topaz':function () {
           return '喵喵喵~';
       }
   });
})(jQuery)


