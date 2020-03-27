---
layout: post
title:  "StyleGAN for Evil: Trypophobia and Clockwork Oranging"
permalink: blog/StyleGAN-for-evil/
tags: machine-learning training code StyleGAN image image-generation trypophobia clockwork orange conditioning evil gan disturbing phobia

---


GANs have become the default image generation technique, and many are familiar with sites like [artbreeder](https://www.artbreeder.com/), [thispersondoesnotexist](https://www.thispersondoesnotexist.com/), and its off-shoots such as [thiswaifudoesnotexist](https://www.thiswaifudoesnotexist.net/). The generated samples are stunning and quite hard to distinguish from real images, and StyleGAN, in particular, has been used and finetuned by many with interesting results.

I've experimented with them before - for example, the projection of real images onto the StyleGAN latent space, and then modifying those is something I find quite interesting. In this project, however, I decided to go in a different direction and use them for evil. 

**All generated horrors in this post are hidden unless you click on them. You can read without looking if you so choose**

Now, some of the more traditional ways of using Generative models for evil are for spam, [deepfakes](https://www.wired.com/story/deepfake-porn-harms-adult-performers-too/), [fake news](https://newsyoucantuse.com/), and [scams](https://analysis.leadstories.com/3471185-fake-faces-people-Who-Do-Not-Exist-Invade-Facebook-To-Influence-2020-Elections.html) but we are going in a different direction here.

### Trypophobia



[Trypophobia](https://en.wikipedia.org/wiki/Trypophobia) is a common condition where people react with discomfort and even strong disgust towards specific irregular patterns of holes or bumps. For some the effect is quite strong, for others, it is just unpleasant, and some like me can see what the issue is but have almost no negative reaction.

It so happens that there is a small, but just [big enough dataset on Kaggle](https://www.kaggle.com/cytadela8/trypophobia) to train a StyleGAN on.

Here are a few examples of how the dataset looks:



<details>
<summary>
<i>Example dataset 1 <small>(click to expand)</small></i>
</summary>
<br>
<br>
<div style="text-align: center;"><img class="img-fluid" src='/static/trypo/dataset1.png'></div>
<br>
</details>
<details>
<summary>
<i>Example dataset 2 <small>(click to expand)</small></i>
</summary>
<br>
<br>
<div style="text-align: center;"><img class="img-fluid" src='/static/trypo/dataset2.png'></div>
<br>
</details>
<details>
<summary>
<i>Example dataset 3 <small>(click to expand)</small></i>
</summary>
<br>
<br>
<div style="text-align: center;"><img class="img-fluid" src='/static/trypo/dataset3.png'></div>
<br>
</details>
<br>


### Training

The training data is very varied - ~6000 images many of completely different objects that only share somewhat similar hole patterns. Inconsistent data works poorly with StyleGAN - what works best is things that are cropped in the same way, from the same angles and generally the same thing but with different features - e.g. faces, even doing full bodies often lead to blobs (less so with stylegan2). This is certainly something that should be a problem with our dataset, but on the bright side we don't care if the rest of the image is blobby, we just want it to learn the specific patterns that trigger trypophobia, doesn't matter if the rest of the image is abstract - in fact, it is better in some ways if it is abstract, as that can make the videos and images more appealing.

I took one of the pretrained StyleGANs nearly at random - churches and started finetuning on the dataset.
The results even early on looked quite interesting. Here are some from the first hours:

<details>
<summary>
<i>Example training 1 <small>(click to expand)</small></i>
</summary>
<br>
<br>
<div style="text-align: center;"><img class="img-fluid" src='/static/trypo/training1.png'></div>
<br>
</details>
<details>
<summary>
<i>Example training 2 <small>(click to expand)</small></i>
</summary>
<br>
<br>
<div style="text-align: center;"><img class="img-fluid" src='/static/trypo/training2.png'></div>
<br>
</details>

<details>
<summary>
<i>Example training 3 <small>(click to expand)</small></i>
</summary>
<br>
<br>
<div style="text-align: center;"><img class="img-fluid" src='/static/trypo/training3.png'></div>
<br>
</details>
<br>


If you find the above fascinating, you can see [much](https://mega.nz/#!eVsC0AjC!6QHzPJMlwuHm5mkxTPOhGsII2ZGycQAv2hE9up6JZYc) [more](https://mega.nz/#!KMtljazI!R4KrNNJMsx4wn4OF8L7gf-TQoakTVee3BO-Myfrq4S4) [at](https://mega.nz/#!nV0zAKgZ!p-0qpKluSlDkTHfjRHR-IYtEnD5zs3RT5QJqvoZdGME) [these](https://mega.nz/#!HU9wXYzL!DAjf448jAXej_38vmmSArDtAV3XHZLXqXvw092DtTBY) [links](https://mega.nz/#!WVU12ayB!sNs5_BgT4iW9CTGtUt4QcI9r8ny83eBMvOvaOGHCaOg).


Here are some video versions.


<details>
<summary>
<i>Example vid 1 <small>(click to expand)</small></i>
</summary>
<br>
<iframe width="560" height="315" src="https://www.youtube.com/embed/l_gK9Q__GVY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<br>
</details>
<details>
<summary>
<i>Example vid 2 <small>(click to expand)</small></i>
</summary>
<br>
<iframe width="560" height="315" src="https://www.youtube.com/embed/yj_mAhj2EwY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<br>
</details>
<details>
<summary>
<i>Example vid 3 <small>(click to expand)</small></i>
</summary>
<br>
<iframe width="560" height="315" src="https://www.youtube.com/embed/vvww_rZQVsI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<br>
</details>
<br>

Responses of the above vary - some are too disgusted too quickly, while others get just a bit of disgust from the worse of it while being intrigued overall, and some don't get a negative reaction at all.

I should also note - videos like these might also be useful for good, as a form of [Exposure Therapy](https://en.wikipedia.org/wiki/Exposure_therapy) but let's not focus on that.

All of the above was trained on Colab using a p100. The final model was trained for roughly 4 days (I saw no improvement near the end), but there were good results within the first day of training.

### Clockwork Oranging

After looking at the early examples of my trypophobia finetunning, I saw some churches that still very much look like churches while also having trypo features. For example these:

<details>
<summary>
<i>Church AND Trypo <small>(click to expand)</small></i>
</summary>
<br>
<br>
<div style="text-align: center;"><img class="img-fluid" src='/static/trypo/trypochurches-training.png'></div>
<br>
</details>
<br>

This gave me the idea that you can fairly easily combine the two (or combine trypophobia and similar images with something else) to create videos which can make someone associate a concept - in this case a church - with negative feelings a la [A Clockwork Orange](https://en.wikipedia.org/wiki/A_Clockwork_Orange_(film)). I chose to add churches to the mix because that's what my pretrained model was already trained on, and I had the dataset (it was not a religious statement) .

The idea (in this scenario we are very evil) is to strap someone (with trypophobia) to a chair and force them to watch those videos which only require some flowing patterns, at least some churchiness and at least some trypophobia-triggering. Admittedly, those videos didn't turn out quite so well - I had to experiment with training them with different ratios of trypo to church photos, but they (and the possibly better photos above) demonstrate the idea well enough.

<details>
<summary>
<i>Example vid 1 <small>(click to expand)</small></i>
</summary>
<br>
<iframe width="560" height="315" src="https://www.youtube.com/embed/KtZFkdP88tQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<br>
</details>
<details>
<summary>
<i>Example vid 2 <small>(click to expand)</small></i>
</summary>
<br>
<iframe width="560" height="315" src="https://www.youtube.com/embed/pvmtJTIKAls" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<br>
</details>
<br>


### Conclusion

This was a fun little project, that I spent a few days on. You would need to spend a bit more time to create something actually dangerous (which I doubt this really is) but not that much more. Of course, what I describe as clockwork oranging doesn't look so useful in the real world but what if you could (and you can) use it to make some images just a bit more repulsive to the general population and others just a bit more appealing with little effort? That seems bad but then again a lot of advertising fits that mold despite it requiring more time per image/video. And at any rate - neither this nor 'evil' are near my main concerns with respect to machine learning. So even though I was thinking of finishing this with something about the dangers of AI, I'll just let people make their own conclusions if there any to make.