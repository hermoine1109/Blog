# Blog

Supported by Pelican framework.
Assuming that you have Pelican installed in your pc, you can run the following codes to preview and modify the blog.

Open terminal and switch to the directory where you've cloned this. 
$pelican content
This generates the content and saves it up to output directory.
Now change your present directory to output directory.
$python -m pelican.server
This starts up the server with the generated blog.
You can view your blog at http://localhost:8000
