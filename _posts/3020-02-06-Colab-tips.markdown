---
layout: post
title:  "Tips and Tricks for Machine Learning Work in Google Colab"
permalink: blog/colab-tips/
tags: machine-learning colab tips

---


[Colab](colab.research.google.com) is one of my favourite machine learning tools and quite possibly the most useful online-based tool for democratizing Machine Learning currently in existance. It is used by many to share research, working models, ideas, a reproducible environment to present github issues, usable machine with a powerful GPU or TPU that many won't have acces to otherwise and more. Colab is extremely useful for novices who are just getting started, allowing them to quickly make or copy something working ᴀɴᴅ it's useful for seasoned practioners who want to share their work.  And it's all free.


There are alternatives of course. [Kaggle Kernels](https://www.kaggle.com/kernels) being perhaps the most popular. If you don't need a GPU [GoCalc](https://cocalc.com/app), [Azure Notebooks](https://notebooks.azure.com/), [Datalore](https://datalore.io/) or [FloydHub Workspaces](https://docs.floydhub.com/guides/workspace/) might be viable options. I'm sure there are other free services, but again as far as I know none of them give you access to a GPU or a TPU which is so often needed in Machine Learning.

However, at least for me Colab has been the most useful despite some pain points. This posts is mostly about addressing those pain points first, and some general Colab tips second.

##### **The most important advice in the article is bolded for easy skimming.**


### Drive

Colab is great for one-off runs or for sharing something that can be setup quickly in a single notebook. However, one often needs to work on something for a long time or might need access to big amounts of data to the point where downloading them each time is too cumbersome or would take too long. In those cases using Google Drive with Colab is your best bet.

Connecting to one of your Google Account's Drive is as simple as:
```
from google.colab import drive
drive.mount('/content/drive')
```
After which you can just `cd` into it.
```
%cd /content/drive/My\ Drive/
```

I'd reccomend to <b>just work straight from Drive in most cases</b> as then your setup time is faster and you likely won't lose as much if your instance times out. Of course, in that case you might run out of space but Drive (or Google One, which is how it's called when you pay for it) has pretty [cheap plans](https://one.google.com/faq/plans-pricing) to extend the space. I personally use the 2TB plan for €9.99 / month but there are even cheaper plans. You can even share a plan between up to 5 people.

Using Drive, however, is not always without issues. For one, files over 5 GB or so can easily get [inaccessible for 24 hours](https://support.google.com/drive/search?q=download+quota+exceeded) due to a hidden quota if you just read or write over them a few times. So, whenever you can <b> make sure to keep all your files under 5gb and split datasets when possible</b>. If you can't split them try to only read from them once at a time - copying them to the local runtime and using them locally is wise in that case.

If you have Google One, you also have access to that most mythical of creatures - Google Support, but they are rarely helpful, and at least in regards to the hidden quota issue none of them seem able to understand what the problem is, let alone help. My advice is not to bother.

Another problem with using Drive is that you can't easily delete a file - the usual options like `os.remove` and `%rm` put the file into Drive's Thrash which still takes up space. What you want to do instead is <b> either empty out files or overwrite them with new data </b>.

Having too many files in the same directory can also cause issues so <b> Avoid having too many files in the root directory of your Drive for faster initial loading </b> and <b> have a directory structure so you never have too many files in the same folder </b>. 

Additionally, <b>don't write to too many files at the same time as some of the writes might silently fail</b>.

### Time outs

A Colab expires after 12 hours of use or over 1 hour of being idle. Sometimes it can time out earlier but that's rare as long as you <b> keep the Colab tab always open on a machine</b>. Nonetheless, saving to Drive at least once every one-two hours is wise.

Sometimes, there might be a random error from Colab itself and the runtime can time out, it doesn't happen too often but be prepared for it.

In general, you probably shouldn't use it longer than you have to - your Accelerator availability seems to drop whenever you use it too much, so <b> always stop the runtime when you are done</b> from Runtime>Manage Sessions>Terminate. Sadly, there is a bug recently where the Terminate option is grayed out but all you have to do to make it available is interupt execution and refresh the page.

I also wouldn't reccomend having more than a single Runtime running (technically you are allowed two) as it also seems to impact your access.


### Runtimes

Sometimes you just have to run something continuusly and in those cases, I'd reccomend to <b> always use the appropriate Runtime </b>. Use CPU (or CPU + high memory runtime) for preprocessing, save to Drive and only use the TPU/GPU runtimes for actual work. Furthermore, Google seem to be a lot happier with people using TPUs - in fact they give access to [more of them somewhat easily to researchers](https://www.tensorflow.org/tfrc) - so if you don't mind what accelerator to focus on, I'd reccomend using TPUs.

You can also cycle through GPU runtimes to get e.g. a P100 by terminating the instance and starting it again, but it's not too reliable and is likely something Google aren't too fond of.
 

### Colab Pro

There is less availability of Accelerators on Colab recently, and my guess is that it is related to them ramping up their Pro version (which has higher priority). I haven't tested it myself because it is sadly US-only but priority access, double the ram, 24 hour (instead of 12 hour) limit and leniency on idle timeouts for $10 / month sound pretty worth it. It sounds like a great deal, and if it was available outside of the US I would've paid for it on the spot. Nonetheless, you can take full advantage of Colab for free, and the upgrade is [currently] purely optional.


https://news.ycombinator.com/item?id=22129422
https://news.ycombinator.com/item?id=22132546

https://news.ycombinator.com/item?id=22164916