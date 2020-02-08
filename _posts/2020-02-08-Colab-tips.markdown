---
layout: post
title:  "Tips and Pain Point Workarounds for Machine Learning Work in Google Colab"
permalink: blog/colab-tips/
tags: machine-learning colab tips google drive

---


[Colab](https://colab.research.google.com/) is one of my favourite machine learning tools and quite possibly the most useful online-based tool for democratizing Machine Learning currently in existence. It is used by many to share research, working models, ideas. It is a reproducible environment to present GitHub issues, a usable machine with a powerful GPU or TPU which many won't have access to otherwise, and more. Colab is extremely useful for novices who are just getting started, allowing them to quickly make or copy something working ᴀɴᴅ it is convenient for seasoned practitioners who want to share their work.  And it's all free.

##### **The key advice in this post is all bolded for easy skimming.**


There are alternatives of course. [Kaggle Kernels](https://www.kaggle.com/kernels) being perhaps the most popular. If you don't need a GPU or are willing to pay then [GoCalc](https://cocalc.com/app), [Azure Notebooks](https://notebooks.azure.com/), [Datalore](https://datalore.io/) or [FloydHub Workspaces](https://docs.floydhub.com/guides/workspace/) might be viable options. That's not even all of the free services out there, but as far as I know, none of the others give you access to a GPU or TPU out of the box which is so often required in Machine Learning.

Nonetheless, at least for me, Colab has been the most useful out of those despite some pain points. This post is about addressing those pain points first, and some general Colab tips I've benefited from second.



### Drive

Colab is great for one-off runs or when sharing something that can be set up quickly in a single notebook. However, one often needs to work on projects for a long time or needs access to big amounts of data to the point where downloading them each time is too cumbersome or would take too long. In those cases using Google Drive with Colab is your best bet.

Connecting to one of your Google Account's Drive is as simple as:
```
from google.colab import drive
drive.mount('/content/drive')
```
After which you can just `cd` into it.
```
%cd /content/drive/My\ Drive/
```

I'd recommend to <b>just work straight from Drive in most cases</b> as then your setup time is faster and you likely won't lose as much if your instance times out. Of course, in that case, you might run out of Drive storage space but Drive (or Google One, which is how it's called when you pay for it) has pretty [cheap plans](https://one.google.com/faq/plans-pricing) to extend the space. I personally use the 2TB plan for €9.99 / month but there are even cheaper ones. You can even share a plan between up to 5 people. On the other hand <b> if you really need fast reads and writes above all else copy the data from Drive to the Colab VM instead </b>.

<em>If you pay for Google One, you also have access to that most mythical of creatures - Google Support, but they are rarely helpful, and at least in regards to the hidden quota issue none of them seem able to understand what the problem is, let alone help. My advice is not to bother.</em>

Using Drive, sadly, is not always frictionless. For one, files over 5 GB or so can get [inaccessible for 24 hours](https://support.google.com/drive/search?q=download+quota+exceeded) easily due to a hidden quota - even by just reading a portion of them a few times. So, whenever you can, <b> make sure to keep all your files under 5gb and split datasets when possible</b>. If you can't divide them try to only read from the big files once at a time - copying them to the local runtime and using them locally can also be wise in that case.


Another problem with using Drive is that you can't easily delete a file - the usual options like `os.remove` and `%rm` put the file into Drive's Thrash which still takes up space. What you want to do instead is <b> either empty out files or overwrite them with new data </b>.

Having too many files in the same directory can also cause issues so <b> Avoid having too many files in the root directory of your Drive for faster initial loading </b> and <b> have a directory structure such that you never have too many files in the same folder </b>. 

Additionally, <b>don't write to too many files at the same time as some of the writes might silently fail</b>.

### Time outs

A Colab expires after 12 hours of use or after 1 hour of being idle. Sometimes it can time out earlier but that's rare as long as you <b> keep the Colab tab always open on a machine</b>. Nonetheless, saving to Drive at least once every one-two hours is wise.

<em>Sometimes, there might be a random error from Colab itself and the runtime can time out - it doesn't happen too often but be prepared for it.</em>

In general, you probably shouldn't use instances longer than you have to - your Accelerator availability seems to drop whenever you use it too much, so <b> always stop the runtime when you are done</b> from Runtime>Manage Sessions>Terminate. Sadly, there is a bug recently where the Terminate option is greyed out but all you have to do to make it available is interrupt execution and refresh the page.

I also wouldn't recommend having more than a single Runtime running (technically you are allowed two) as it also seems to impact your access.


### Runtimes

Sometimes you just have to run something continuously and in those cases, I'd recommend to <b> always use the appropriate Runtime </b>. Use CPU (or CPU + high memory runtime) for preprocessing, save to Drive and only use the TPU/GPU runtimes for actual work. Furthermore, Google seem a lot happier with people using TPUs - in fact, they give access to [a fair amount of them somewhat easily to researchers](https://www.tensorflow.org/tfrc) - so if you don't have a preference for what accelerator to focus on, I'd recommend using TPUs.

You can also cycle through GPU runtimes to get e.g. a P100 by terminating the instance and starting it again, but it's not too reliable and is likely something Google isn't too fond of. <b>To check your current GPU just run `!nvidia-smi`.</b>
 

### Colab Pro

There is less availability of Accelerators on Colab recently, and my best guess is that it is related to them ramping up the Pro version (which has higher priority). I haven't tested it myself because Pro is sadly US-only but priority access, double the ram, 24 hour (instead of 12 hour) limit and leniency on idle timeouts for $10 / month sound pretty worth it - if it was available outside of the US I would've paid for it on the spot. Nonetheless, you can take full advantage of Colab for free, and the upgrade is [currently] purely optional.


### Miscellaneous

One general pain point with notebooks is that you often end up needing to check something once, e.g. `print(x.shape)` which can lead to too much clutter. A great way to combat that is to <b> go to Insert>Scratch Code Cell (or ctr+alt+N) and do all your prints and one-off statements in there </b>.

---

If you are not working with Drive you can simply set it up so you download your results to your own machine at the end of your cell. Simply do:

```
from google.colab import files
files.download(result) 
```

---

If you need to edit multiple lines at once <b> you can use find and replace using ctr+H which also allows you to match using regular expressions</b>. This only works when you don't have a running cell.

### Conclusion

Colab is pretty great, and I've benefited tremendously from it. There are some annoyances but you can work around them. That's it.