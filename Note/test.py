 .. contents::
    if a != 0
        print("test")
https://github.com/riku/Markdown-Syntax-CN/blob/master/syntax.md#precode
    [参考]: http://example.com/  "Test"
链接内容定义的形式为：

方括号（前面可以选择性地加上至多三个空格来缩进），里面输入链接文字
接着一个冒号
接着一个以上的空格或制表符
接着链接的网址
选择性地接着 title 内容，可以用单引号、双引号或是括弧包着
 
    
<pre><code>这是一个代码区块。

    from zhihu import Answer
    answer_url = "http://www.zhihu.com/question/24269892/answer/29960616"
    answer = Answer(answer_url) 
</code></pre>
    
    
    
