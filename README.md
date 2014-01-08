fofops
======

a simple utility for connecting to amazon opsworks instances

###Installation
Just clone this repository: <code>git clone git@github.com:jawsthegame/fofops</code>

Then you will need to install boto: <code>pip install boto</code>

###Configuration
You will need to add [boto](https://github.com/boto/boto) configuration file if you don't already have one.

It should have this path: <code>~/.boto</code>
<pre><code>[Credentials]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
</code></pre>
