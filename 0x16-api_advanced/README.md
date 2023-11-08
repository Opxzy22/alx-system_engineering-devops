<!DOCTYPE html>
<html lang="en">
  <head>
  <h1> 0x16. API advanced </h1>
</head>
<body>
<h2>BACKGROUND CONTEXT</h2>

<p>Questions involving APIs are common for interviews. Sometimes they&rsquo;re as simple as &lsquo;write a Python script that queries a given endpoint&rsquo;, sometimes they require you to use recursive functions and format/sort the results.</p>

<p>A great API to use for some practice is the Reddit API. There&rsquo;s a lot of endpoints available, many that don&rsquo;t require any form of authentication, and there&rsquo;s tons of information to be parsed out and presented. Getting comfortable with API calls now can save you some face during technical interviews and even outside of the job market, you might find personal use cases to make your life a little bit easier.</p>

<h2>RESOURCES</h2>

<p><strong>READ or WATCH</strong>:</p>
<ul>
<li><a href="/rltoken/b-4nD6hwEeNYTwYl5yWNwA" title="Reddit API Documentation" target="_blank">Reddit API Documentation</a> </li>
<li><a href="/rltoken/luFn_zrgmAQ0OAO_PEI9bA" title="Query String" target="_blank">Query String</a></li>
</ul>
<h3>KNOWLEGE TEST</h3>

<ul>
<li>How to read API documentation to find the endpoints you&rsquo;re looking for</li>
<li>How to use an API with pagination</li>
<li>How to parse JSON results from an API</li>
<li>How to make a recursive API call</li>
<li>How to sort a dictionary by value</li>
</ul>

<h2>REQUIREMENTS</h2>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using <code>python3</code> (version 3.4.3)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>Libraries imported in your Python files must be organized in alphabetical order</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>PEP 8</code> style</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>All your modules should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
<li>You must use the Requests module for sending HTTP requests to the Reddit API</li>
</ul>
 <h2 class="gap">TASKS</h2>
 <h2 class="gap">mandatory</h2>
<h3 class="panel-title">
      0. How many subs?
</h3>
<h4>Write a function that queries the <a href="/rltoken/b-4nD6hwEeNYTwYl5yWNwA" title="Reddit API" target="_blank">Reddit API</a> and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.</h4>

<p>Hint: No authentication is necessary for most features of the Reddit API. If you&rsquo;re getting errors related to Too Many Requests, ensure you&rsquo;re setting a custom User-Agent.</p>

<h3>REQUIREMENTS:</h3>

<ul>
<li>Prototype: <code>def number_of_subscribers(subreddit)</code></li>
<li>If not a valid subreddit, return 0.</li>
<li>NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.</li>
</ul>
<h3 class="panel-title">
      1. Top Ten
</h3>
<h4>Write a function that queries the <a href="/rltoken/b-4nD6hwEeNYTwYl5yWNwA" title="Reddit API" target="_blank">Reddit API</a> and prints the titles of the first 10 hot posts listed for a given subreddit.</h4>

<p>REQUREMENTS:</p>

<ul>
<li>Prototype: <code>def top_ten(subreddit)</code></li>
<li>If not a valid subreddit, print None.</li>
<li>NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.</li>
</ul>

 <h3 class="panel-title">
      2. Recurse it!
</h3>

<h4>Write a <em>recursive function</em> that queries the <a href="/rltoken/b-4nD6hwEeNYTwYl5yWNwA" title="Reddit API" target="_blank">Reddit API</a> and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None.</h4>

<P>Hint: The Reddit API uses pagination for separating pages of responses.</p>

<h5>REQUIREMENTS:</h5>

<ul>
<li>Prototype: <code>def recurse(subreddit, hot_list=[])</code></li>
<li>Note: You may change the prototype, but it must be able to be called with just a subreddit supplied. AKA you can add a counter, but it must work without supplying a starting value in the main.</li>
<li>If not a valid subreddit, return None.</li>
<li>NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.</li>
</ul>

<p>Your code will NOT pass if you are using a loop and not recursively calling the function! This /can/ be done with a loop but the point is to use a recursive function. :)</p>

<h3 class="panel-title">
      3. Count it!
</h3>
<p>Write a <em>recursive function</em> that queries the <a href="/rltoken/b-4nD6hwEeNYTwYl5yWNwA" title="Reddit API" target="_blank">Reddit API</a>, parses the title of all hot articles, and prints a sorted count of given keywords (case-insensitive, delimited by spaces. <code>Javascript</code> should count as <code>javascript</code>, but <code>java</code> should not).</p>

<p>Requirements:</p>

<ul>
<li>Prototype: <code>def count_words(subreddit, word_list)</code></li>
<li>Note: You may change the prototype, but it must be able to be called with just a subreddit supplied and a list of keywords. AKA you can add a counter or anything else, but the function must work without supplying a starting value in the main.</li>
<li>If <code>word_list</code> contains the same word (case-insensitive), the final count should be the sum of each duplicate (example below with <code>java</code>)</li>
<li>Results should be printed in descending order, by the count, and if the count is the same for separate keywords, they should then be sorted alphabetically (ascending, from A to Z). Words with no matches should be skipped and not printed. Words must be printed in lowercase.</li>
<li>Results are based on the number of times a keyword appears, not titles it appears in. <code>java java java</code> counts as 3 separate occurrences of <code>java</code>.</li>
<li>To make life easier, <code>java.</code> or <code>java!</code> or <code>java_</code> should not count as <code>java</code></li>
<li>If no posts match or the subreddit is invalid, print nothing.</li>
<li>NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are NOT following redirects.</li>
</ul>

<p>Your code will NOT pass if you are using a loop and not recursively calling the function! This /can/ be done with a loop but the point is to use a recursive function. :)</p>

<p><strong>Disclaimer</strong>: number presented in this example <em>cannot be accurate now</em> - Reddit is hot articles are always changing.</p>

  </body>
</html>
