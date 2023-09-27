<h1>WEB SERVER</h1>
<h2>Resources</h2>
<p>
<ul>
   <li><a href="https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works">HOW WEB WORKS</a>.</li>
   <li><a href="https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-16-04">HOW TO CONFIGURE NGINX</a>.</li>
   <li><a href="https://landingi.com/help/domains-vs-subdomains/">ROOT AND SUB DOMAIN</a>.</li>
</ul> 
<h2>Requirements</h2>
</p>
<ul>
  <li>Allowed editors: vi, vim, emacs</li>
  <li>All your files will be interpreted on Ubuntu 16.04 LTS and checked with Shellcheck</li>
  <li>First line of all your Bash scripts should be <b>#!/usr/bin/env bash</b></li>  
<h2>TASKS : MANDATORY</h2>
<p><b>0. Transfer a file to your server</b></p>
<ol>
   <ul>
      <li>Write a Bash script that transfers file from our client to a server</li>
      <li>Accepts 4 parameters</li></li>
      <li>scp must transfer the file to the user home directory</a>.</li>
   </ul>
</ol>
  
<p><b>1. Install nginx web server</b></p>

<ol>
   <ul>
      <li>Install nginx on server listening on port 80</li>
      <li>write a Bash script that configures a new Ubuntu machine</li>
      <li>You can’t use systemctl for restarting nginx</li>
   </ul>
</ol>
<p><b>2. Setup a domain name</b></P>
<ol>
   <ul>
      <li>provide domain name and configure your DNS records with an A entry</li>
      <li>When your domain name is setup, please verify the Registrar</li>      
   </ul>
</ol>
<p><b>3. Redirection</b></p>
<ol>
   <ul>
      <li>Configure Nginx server so that /redirect_me is redirecting to another pagee</li>
      <li>Write Bash script containing commands to automatically configure a Ubuntu machine</li>
      <li><a href="https://stackoverflow.com/questions/26041088/sed-replace-line-with-multiline-variable">Replace a line with multiple lines with sed</a>.</li>
   </ul>
 </ol>
<p><b>4. Not found page 404</b></p>
<ol>
   <ul>
      <li>The page must return an HTTP 404 error code</li>
      <li>configure a brand new Ubuntu machine</li>
   </ul>
 </ol>
<h2>TASKS: ADVANCED<h5>
<p><b>5. Install Nginx web server (w/ Puppet)</b></p>
<ol>
    <ul>
      <li>Nginx should be listening on port 80</li>
      <li>The redirection must be a “301 Moved Permanently”</li>
    </ul>
</ol>

<pre class="literal-block">
</pre>
<p><br/><br/></p>
