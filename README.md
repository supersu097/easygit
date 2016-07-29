## Easygit
这是一个用来帮助自己在终端下提交代码的小脚本，目前功能比较简单，  
基本够自己用了,后续自己再有什么需求了再慢慢实现。。
### Usage  
```
usage: gitp [-h] (-f [FILENAME [FILENAME ...]] | -a | -o)

a simple py script to help you use git easily

optional arguments:
  -h, --help            show this help message and exit
  -f [FILENAME [FILENAME ...]], --filename [FILENAME [FILENAME ...]]
                        the file you wanna push to the remote git server,
                        support multiple filename as args
  -a, --add_option      add one or more case of file changes between new,
                        modified and deleted to stage regarding your local git
                        version and your choice
  -o, --other_case      other case of change except for new,modified and
                        deleted,then just commit and push
```
### Other
对于各种`git add`各种选项如下图：  
![](img/git_add_diff.png)  
详情参考：[StackOverflow: Difference between “git add -A” and “git add .”](http://stackoverflow.com/questions/572549)
### 效果图如下
![](img/workflow.png)
