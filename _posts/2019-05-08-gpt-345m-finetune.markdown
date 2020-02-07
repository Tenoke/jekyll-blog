---
layout: post
title:  "Fine-tunning OpenAI's (Larger) GPT-2-345M on Conversation data (Update)"
subtitle: "Using Google Colab"
permalink: blog/gpt-345M-finetune/
tags: gpt gpt2 finetune colab nlp machine-learning

---

NLP, Machine Conversations and the road to passing the Turing Test have always interested me. That's why when OpenAI released a larger (345M parameters vs the previous ) version of [GPT-2, their current state of the art language model](https://openai.com/blog/better-language-models/#update) I jumped to test it out on my small but personal dataset of 14mb of my own facebook conversations along with testing it a bit on a [Two person Ubuntu-related dialogue corpus](https://www.kaggle.com/rtatman/ubuntu-dialogue-corpus).

The newly released pre-trained version has 345 million parameters, compared to the 117M parameter version so one would expect significantly better results. Note, this is still significantly smaller than the 1.5B version they've shown off. OpenAI are, however, releasing the aforementioned 1.5B version along with a 762M version to partner organizations along with plans to release those to the public in the future, too.

Although it will be interesting to play around with those much bigger GPT-2 versions, they might not even be relevant by the time they are released - training on the same data with the same amount of compute one can already most likely build an even better model using recent advances e.g. even just with better transformers like OpenAI's [Sparse Transformer](https://openai.com/blog/sparse-transformer/) or Google AI's [Transofmer-XL](https://ai.googleblog.com/2019/01/transformer-xl-unleashing-potential-of.html) both of which improve on GPT-2's current architecture.

I won't go into detail describing the Colab with Facebook data, as it is almost the same as the one used with the 117M version which I describe [here](/blog/gpt-finetune/). We are again using [nsheppered's GPT training code](https://github.com/nshepperd/gpt-2), this time with gradient checkpointing to be able to fit the larger model in memory.


You can follow in the new GPT-2-345M collab FB data [here](https://colab.research.google.com/drive/1EhZG2_AQLeDvW2s841d502FydMn1vgmK). Make sure to click Runtime> Change Runtime type> GPU (or TPU)

**[Generated Facebook Messenger Dialogue Samples](#facebook-examples)**

There is also the GPT-2-345M ubuntu data (including preprossesing)  [here](https://colab.research.google.com/drive/161JjdAyqckSBLD45N9WZzFI21rUYk2ns). Make sure to click Runtime> Change Runtime type> GPU (or TPU)

**[Generated Ubuntu Dialogue Samples](#ubuntu-examples)**


## Results

First of, The results are visibly better. Even without fine-tuning 345M produces visibly (but not overwhelmingly so) better results than 117M, and preliminary outputs from [fine-tuning it on poetry](https://www.gwern.net/GPT-2) are reportedly even more promising. It is hard to judge how much better but for example, I couldn't get the loss on my small 14M facebook messages dataset to go consistently bellow *2.10* with 117M, while with 345M (and admittedly a bit more training) I got it down to *1.85*.

### Facebook

The results are a bit better and more coherent but 14M is clearly too small a dataset. I had to do some small tricks (mainly decreasing the learning rate periodically and occasionally attempting to use the ubuntu data, too). Adding the *endoftext* token instead of two blank lines between conversations also helped as expected.

#### *Facebook Examples:*



>(1353629564276) Tom Middlebrook: alright, i was given a bag as a present. so i had to return it to my parents. was fine getting it again though but only with a small amount

>(1353595877463) Svilen Todorov: nice

>(1353655925201) Tom Middlebrook: https://www.youtube.com/watch?v=tYJhLgK1KqU

>(1353655946673) Svilen Todorov: i should've probably taken a photo when i did that haha

>(1353655984955) Svilen Todorov: i saw someone else on youtube trying to buy like 20 quid extra lol

>(1353656240766) Svilen Todorov: i think ill have to do a job at some point after i graduate but yh

>(1353654726000) Svilen Todorov: http://www.reddit.com/tb/y2r0r

>(1353654728111) Svilen Todorov: i dont get why not to give him the money :D

>(1354159959666) Tom Middlebrook: lol

>(1354165011230) Tom Middlebrook: that's awesome

>(1354155045207) Svilen Todorov: hahaha, yh

>(1354255181784) Tom Middlebrook: http://i.imgur.com/Ypk.png

>(1354255222767) Tom Middlebrook: I'm pretty sure the other two guys that I had work with from the day before had worked with jsa lol 

>(1354255453761) Svilen Todorov: hahah

>(1354357524074) Svilen Todorov: oh ya

>(1354357528963) Tom Middlebrook: http://i.imgur.com/m4h5.jpg

>(1354357535641) Tom Middlebrook: looks really cool

>(1354357540333) Svilen Todorov: hahahaha

>(1354357562322) Svilen Todorov: nice

>(1354357563001) Tom Middlebrook: looks like a cool outfit

<br>
<br>

>(1496878572976) Ioannis Agathocleous: Ill have to see a place in the east of london

>(1496878585860) Svilen Todorov: maybe

>(1496878623078) Svilen Todorov: not too far

>(1496878673631) Svilen Todorov: well not that far

>(1496878673234) Svilen Todorov: might be too much as I am not going to get much for a place that already has one

>(1496878680863) Svilen Todorov: but dunno

>(1496878688387) Svilen Todorov: i'll go to a place in london instead since I don't have a job

>(1496878698013) Ioannis Agathocleous: I could find one somewhere on the east but the distance is pretty small

>(1496878706547) Ioannis Agathocleous: But I dont mind

>(1496878783822) Svilen Todorov: it's not too far

>(1496878792946) Svilen Todorov: well, Im pretty sure it'd be easier to just find a place in london instead if I get too many people to live with

>(1496878807895) Svilen Todorov: if there isnt one in the UK I might be able to get a place here or something

>(1496888089082) Svilen Todorov: yeah, i can find somewhere

>(1496888051110) Ioannis Agathocleous: Ye probs best to be a foreigner

>(1496888061658) Ioannis Agathocleous: Just find a new place and work

>(1496888093631) Svilen Todorov: yh true

>(1496888096719) Svilen Todorov: yh, I've found a place

>(1496888096620) Ioannis Agathocleous: You gotta find something

>(1496887102292) Ioannis Agathocleous: Or stay at a mate's house for a few months

>(1496887143560) Svilen Todorov: will do

>(1496887162939) Svilen Todorov: I think you'll find something in Bulgaria

>(1496887172227) Svilen Todorov: in london might be easier to find something

>(1496887193938) Svilen Todorov: so yh find what you want

>(1496888245750) Ioannis Agathocleous: Ye will do

>(1496895273936) Svilen Todorov: just saw a flat for 200 which is 2 hours from my place

>(1496895284880) Svilen Todorov: I can also get a place cheaper if I move there too

>(1496895358255) Ioannis Agathocleous: Seems like a decent deal

>(1496895641622) Ioannis Agathocleous: Ill see if I can find something from the guys

>(1496893649976) Svilen Todorov: looks like it's in the center of meelerdham

>(1496893664983) Ioannis Agathocleous: Kl ill check it out

>(1496893669386) Svilen Todorov: if I move tomorrow Ill be living in London until March for a year

>(1496893688213) Ioannis Agathocleous: Ye but I dont mind moving anyway

<br>
<br>

>(13136700170) Svilen Todorov: i'm going to sleep

>(1313670106021) Michal Rostecki: ah sorry, I forgot

>(1313670197807) Michal Rostecki: yeah, I will prob go there around 19:30

>(1313670199539) Svilen Todorov: ok, about to try to make it to the bar at least

>(1313670199507) Svilen Todorov: if its like that

>(1313670199579) Svilen Todorov: its way down

>(1313670199997) Michal Rostecki: yeah, now I'm on my way

>(1313670199994) Svilen Todorov: oh and I keep forgetting my passport when I get there

>(1313670199923) Svilen Todorov: well i have it already :D

>(1313680514053) Svilen Todorov: http://www.buzzfeed.com/buzzfeed/comments/2lh/how-do-you-use-the-device-menu-system-in-ubuntu-10-04-lucid-with-ubuntu-10-04-lucid-lucid-with-ubuntu-10-04-lucid-lucid-with-ubuntu-10-04-lucid-lucid-with-ubuntu-10-04-lucid-lucid-with-ubuntu-10-04-lucid-like-after-reinstalling-the-grub-loader-for-ubuntu-10-04/

>(1313671553576) Michal Rostecki: what's your plan for today? did you find it?

>(1313671607100) Svilen Todorov: nah got some stuff to do

>(1313671627252) Svilen Todorov: im heading to work now

>(1313671638781) Michal Rostecki: cool! I'll probably be there around 4ish

>(1313671666644) Svilen Todorov: didnt get that

>(1313671669988) Svilen Todorov: nah it's fine

>(1313671670159) Michal Rostecki: ok

<br>
<br>

>(1544396720429) Carmen Quasi: are you going to a bar?

>(1544396782520) Svilen Todorov: yeah sure

>(1544396988765) Svilen Todorov: but Ill probably stay at mine longer

>(1544397997134) Carmen Quasi: hihi i can come to yours at some point

>(1544397996679) Carmen Quasi: I'm in a park with my friend Jonas. you could just head there and drink a beer

>(1544402012633) Svilen Todorov: Ja

>(1544402269095) Svilen Todorov: If I will come by the same time Ill pass by to get my backpack

>(1544402529078) Carmen Quasi: it's not so big a park

>(1544402839650) Carmen Quasi: i dont get where you are

>(1544407472321) Svilen Todorov: Ja same

>(1544407506681) Svilen Todorov: It's in the center

>(1544407505377) Svilen Todorov: A lot bigger than London for sure

>(1544503854605) Carmen Quasi: yeah it's in the center with a garden

>(1544505993833) Carmen Quasi: there is a pool pool in the center, not the backyard

>(1544507562468) Svilen Todorov: Ye fair

>(1544507569097) Svilen Todorov: Might come for a bit to try it

>(1544507617387) Carmen Quasi: nice



### Ubuntu

I mainly tried this out of curiosity but also in order to attempt to use a somewhat similar (dialogue) dataset for somehow improving the accuracy on my all-to-small facebook dataset. I tried multiple things but the only thing that actually helped was to train for a bit (<1500 steps) on the ubuntu dataset a few times when the loss on my own dataset won't go down and then go back. This sped things up slightly and allowed me to reach a little bit higher accuracy in the end but the difference isn't too big.

I only tried this for a couple of hours and used slightly less than half the data (there are 3 folders in the datasets and I only used the 951M one) but the results were quite close to what's in the dataset. Here are some random (non-cherry picked) samples. Honestly, if you give me some actual conversations from this dataset and some generated conversations, I'm not sure if I'd do much better than 60% at recognizing which is which.

#### *Ubuntu Examples:*


>(1191738600) chrism_: hi all

>(1191738760) chrism_: can somebody help me set up a nvidia x driver? my system doesn't display an X server. I think it's not a graphical problem.

>(1191738820) jocke: I would use xorg1-driver

>(1191738900) jocke: then do that

>(1191738960) jocke: I usually install both but at least you can do that

>(1191738960) jocke: I would just follow this guide to help you

>(1191739020) jocke: https://wiki.ubuntu.com/X11/UsingX11/Manual

>(1191739080) jocke: if your setup doesn't load the driver it might be a bad idea to disable it. But when you run xmodmap <keycode> and it says no such buffer I assume that you are good to set it back to working state you should be fine

>(1191739080) jocke: the first step (the xorg1-driver) is to run xmodmap from that directory. Once that is done it will be available as a device for 'device' on your desktop. If your only problems are with xorg1.h or X11.h, just add it to /etc/X11/xorg.conf

>(1191739400) jocke: if you need the xorg.conf just edit my example file to change it to the one you want to have.

<br>
<br>


>(1299144700) luigi__: hey i have this problem, how do i stop and remove all the packages ubuntu has, it keeps re-installing everything when i change the source and i change the repository to another one

>(1299144760) luigi__: thanks

>(1299144760) cnj_: right-click the source folder and look for a dropdown area

>(1299144760) cnj_: yes

>(1299144760) cnj_: then right-click

>(1299144760) cnj_: then type   dpkg -L      and hit enter

>(1299144760) cnj_: then click add

>(1299144820) cnj_: it will start downloading everything, just in case

>(1299144820) cnj_: it will tell you to restart the system to do that

>(1299144820) luigi__: what do you mean?

>(1299144880) cnj_: in here?

>(1299144880) luigi__: i don't have that on my laptop

>(1299144880) cnj_: I'll give you a link.

>(1299144880) cnj_: http://paste.ubuntu-nl.org/134440/

>(1299144880) cnj_: this is my machine

>(1299144880) cnj_:  my

>(1299144880) cnj_: my problem

>(1299144880) luigi__: the thing is its working perfectly fine on my laptop

>(1299144880) cnj_: the laptop has no problems with downloading any package that is offered through my terminal

>(1299144940) cnj_: I have no connection to you.

>(1299144940) cnj_: in ubuntu/lubuntu/solaris

>(1299144940) luigi__: so if i just installed those ubuntu packages, they still need reinstallation?

>(1299144940) cnj_: yes

<br>
<br>

>(1189447620) m0nix_: hmm

>(1189447680) m0nix_: I had a good time with Wine2X, but i changed my mind, I will not use Wine2 for this application.

>(1189447740) m0nix_: Is there a way to make the application run on Ubuntu?

>(1189447740) MrFool: sudo dpkg --purge wine2x ?

>(1189447740) MrFool: I got wine

>(1189447740) MrFool: yes.

>(1189447800) MrFool: I guess you don't really need the whole x server, but that you can just install.

>(1189447860) MrFool: Wine2 is just an extension from Wine3

>(1189447920) MrFool: Yes you want to run X?

>(1189442140) MrFool: You have a server

<br>
<br>

>(1199918140) kalzior: anyone know where i can get fiesty to work with this new version?

>(1199918140) nishant: you can use gtk-fiesty

>(1199918140) kalzior: thanks

>(1199918140) nishant: I have never really used freestyle, but the gui interface does a good job



>(1321455720) wuqh2u2n: do you know how to do ubuntu and windows together??

>(1321455780) theadmin: you need to use the ubuntu iso to install.

>(1321455840) wuqh2u2n: but its just 2 partitions

>(1321455900) theadmin: ok so when installing ubun

>(1321446060) theadmin: which one is the right?

>(1321456600) theadmin: which ISO

>(1321456600) wuqh2u2n: i've tried downloading the iso but they're all wrong, but theres a way to use it

>(1321462060) theadmin: try and use the iso you downloaded, it will be an iso you can burn to

>(1321462300) theadmin: thats it, you will be able to burn it to cd

>(1321462300) theadmin: its the right iso

>(1321462300) theadmin: how do i burn them? i need some help

>(1321462300) theadmin: i need to burn the iso from the internet

>(1321462540) theadmin: you need to have a cd

<br>

## Conclusion

The conversations look better but not ideal. The model is learning even more relevant stuff - e.g. they are about mutual interests, acquaintances etc. It truly seems to have some idea of who each person is and can mostly catch the tone and relevant facts about most people I've talked enough to.

It was also easy and fun to play with and makes me wonder how much better we can do with the biggest model or better techniques or ideally more of everything. At this rate, we might soon have chatbots good enough for people to not even compare them to Eliza!