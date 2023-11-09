<!DOCTYPE html>
<html lang="en">
  <head>
   <h1> 0x17. Web stack debugging #3 </h1>
 </head>
<body>
 <h2 class="panel-title">Concepts</h2>
   <p>
   <em>For this project, we expect you to look at these concepts:</em>
   </p>
   <ul>
   <li>
   <a href="/concepts/17">Web Server</a>
   </li>
   <li>
   <a href="/concepts/68">Web stack debugging</a>
   </li>
   </ul>
<h2>Background Context</h2>

<p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/293/d42WuBh.png" alt="" loading='lazy' style="" /></p>

<p>When debugging, sometimes logs are not enough. Either because the software is breaking in a way that was not expected and the error is not being logged, or because logs are not providing enough information. In this case, you will need to go down the stack, the good news is that this is something Holberton students can do :)</p>

<p>Wordpress is a very popular tool, it allows you to run blogs, portfolios, e-commerce and company websites&hellip; It <a href="/rltoken/qxyFYZIwOXQWw02-HaQ7Bw" title="actually powers 26% of the web" target="_blank">actually powers 26% of the web</a>, so there is a fair chance that you will end up working with it at some point in your career.</p>

<p>Wordpress is usually run on LAMP (Linux, Apache, MySQL, and PHP), which is a very widely used set of tools. </p>

<p>The web stack you are debugging today is a Wordpress website running on a LAMP stack.</p>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>All your files will be interpreted on Ubuntu 14.04 LTS</li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file at the root of the folder of the project is mandatory</li>
<li>Your Puppet manifests must pass <code>puppet-lint</code> version 2.1.1 without any errors</li>
<li>Your Puppet manifests must run without error</li>
<li>Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about</li>
<li>Your Puppet manifests files must end with the extension <code>.pp</code> </li>
<li>Files will be checked with Puppet v3.4</li>
</ul>
<h2>More Info</h2>

<h3>Install <code>puppet-lint</code></h3>

<pre><code>$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
</code></pre>
<h3 class="panel-title">
      0. Strace is your friend
</h3>
<p><a href="https://youtu.be/uHEzt1QuASo" target="_blank"><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/6/f5af5167e65bd3101f76.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231107%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231107T142813Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=96f88ea243aaf0a9c7e18c88e6b192af2d055c9292ad8f5cf0db5efc1108c568" alt="" loading='lazy' style="" /></a></p>

<p>Using <code>strace</code>, find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet (instead of using Bash as you were previously doing).</p>

<p>Hint:</p>

<ul>
<li><code>strace</code> can attach to a current running process</li>
<li>You can use <a href="/rltoken/UsSRoxIYdq0l0QUIuDNnSw" title="tmux" target="_blank">tmux</a> to run <a href="/rltoken/ueMevAif95DjyW2sqVCMoA" title="strace" target="_blank">strace</a> in one window and <code>curl</code> in another one</li>
</ul>

<p>Requirements:</p>

<ul>
<li>Your <code>0-strace_is_your_friend.pp</code> file must contain Puppet code</li>
<li>You can use whatever Puppet resource type you want for you fix</li>
</ul>
</body>
</html>
