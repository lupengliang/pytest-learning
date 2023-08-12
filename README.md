# $\color{#3d3ce3ff}{1. 运行命令}$ 

#### $\color{#00FF00}{1.1 运行所有用例}$
<code>pytest -vs</code>

#### $\color{#00FF00}{1.2 运行指定目录下的用例}$
<code>pytest -vs testcasedir</code>

#### $\color{#00FF00}{1.3 运行指定目录下文件的用例}$
<code>pytest -vs testcase_**.py</code>

#### $\color{#00FF00}{1.4 使用关键字过虑出符合要求的所有用例 }$
<code>pytest -vs testcasedir -k "keyword"</code>

#### $\color{#00FF00}{1.5 失败1个用例测试任务停止 }$
<code>pytest -vs testcasedir -x</code>

#### $\color{#00FF00}{1.6 最大失败2个用例测试任务停止 }$
<code>pytest -vs testcasedir --maxfail 2</code>

#### $\color{#00FF00}{1.7 失败用例重复执行两次 }$
<code>pytest -vs testcasedir --reruns 2</code>

#### $\color{#00FF00}{1.8 多线程执行用例 }$
<code>pytest -vs testcasedir -n 2</code>


<br><br>
# $\color{#3d3ce3ff}{2. 运行标记用例}$

#### $\color{#00FF00}{2.1 运行冒烟用例}$
<code>@pytest.mark.mark01</code><br>
<code>pytest -vs testcasedir -m "mark01 or mark02"</code>


<br><br>
# $\color{#3d3ce3ff}{3. 生成测试报告}$

#### $\color{#00FF00}{3.1 生成测试数据&&生成报告}$
<code>pytest -sv --alluredir ./temp</code><br>
<code>allure generate ./temp -o ./report --clean</code><br>



<br><br><br><br><br><br><br><br><br><br>
<div class=float🤛><kbd>一&nbsp;</kbd> <kbd>切&nbsp;</kbd> <kbd>都&nbsp;</kbd><kbd>会&nbsp;</kbd><kbd>好&nbsp;</kbd><kbd>的&nbsp;</kbd><kbd>ok&nbsp;!</kbd></div> 
1🥇2🥇3🥇3🥇4🥇5🥇6🥇7🥇8🥇9🥇10🥇11🥇12🥇13🥇14🥇15🥇16🥇17🥇18🥇19🥇20🥇21🥇

