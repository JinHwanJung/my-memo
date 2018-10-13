---


---

<h1 id="자주-찾아보는-것들-정리">자주 찾아보는 것들 정리</h1>
<h2 id="prevent-master-commit--merge & push"> prevent master commit &amp; push</h2>
<p>link: <a pushhttps://stackoverflow.com/questions/40462111/git-prevent-commits-in-master-branch">https://stackoverflow.com/questions/40462111/git-prevent-commits-in-master-branch</a></p>
<ol>
<li>.git/hooks/pre-commit</li>
</ol>
<pre class=" language-bash"><code class="prism  language-bash"><span class="token shebang important">#!/bin/sh</span>
branch<span class="token operator">=</span><span class="token string">"<span class="token variable"><span class="token variable">$(</span><span class="token function">git</span> rev-parse --abbrev-ref HEAD<span class="token variable">)</span></span>"</span>

<span class="token keyword">if</span> <span class="token punctuation">[</span> <span class="token string">"<span class="token variable">$branch</span>"</span> <span class="token operator">=</span> <span class="token string">"master"</span> <span class="token punctuation">]</span><span class="token punctuation">;</span> <span class="token keyword">then</span>
  <span class="token keyword">echo</span> <span class="token string">"You can't commit directly to master branch"</span>
  <span class="token keyword">exit</span> 1
<span class="token keyword">fi</span>
</code></pre>
<ol start="2">
<li>.git/hooks/pre-push</li>
</ol>
<pre><code>#!/bin/bash
protected_branch='master'
current_branch=$(git symbolic-ref HEAD | sed -e 's,.*/\(.*\),\1,')

if [ $protected_branch = $current_branch ]
then
    read -p "You're about to push master, is that what you intended? [y|n] " -n 1 -r &lt; /dev/tty
    echo
    if echo $REPLY | grep -E '^[Yy]$' &gt;> /dev/null
    then
        exit 0 # push will execute
    fi
    exit 1 # push will not execute
else
    exit 0 # push will execute
fi
</code></pre>
<ol start="3">
<li>Make it executable</li>
</ol>
<pre class=" language-bash"><code class="prism  language-bash"><span class="token function">chmod</span> +x .git/hooks/pre-commit
<span class="token function">chmod</span> +x .git/hooks/pre-push
</code></pre>

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTQ2MjM1Mjc2Nl19
-->