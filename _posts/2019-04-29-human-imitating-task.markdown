---
layout: post
title:  "A Proposed Task for Training a Human-Imitating System as a Benchmark and Potential Part of The Road to AGI "
permalink: blog/human-imitating-task/

---


## Basic idea:

One of the most important pieces for training a more general ‘human-like’ System (Neural Network) is having a good open-ended task which is either unsupervised or where generating very large amounts of data is doable.

I propose training a model where the input is simply people interacting with their computer (just the browser for simplicity) as they normally do and the output is a prediction of the next action they will take.

<sub><sup>
For those who don't think AGI is possible - I am not saying it definitely is (especially not immediately), just proposing a task to get closer to something that is realistically doable.
</sub></sup>

## Rationale

At this point in the current Deep Learning revolution it seems like variations of [our](https://github.com/NVlabs/stylegan) [current](https://openai.com/five/) [techniques](https://github.com/openai/gpt-2) can likely solve most any *well-defined* problem if you use the right parts, have enough data and make the network big enough.
Alternatively, if this isn’t the case seeing how far we can go and having a harder human-imitating task can be used as a good benchmark. 

Thus, I am operating under the assumption that having the right problem with a strong enough signal is as important, or plausibly a more important problem than finding a new technique for developing an algorithm that can at minimum behave in a more general, human-like fashion. For example, I no longer believe that there is a game (video or otherwise) that isn't solvable at human-level with current techniques as long as you have enough resources (time, people, and computation).

## Task

Record an enormous training set of people using their browsers. Include mouse clicks, key presses, screenshots of the screen, text on screen, OCR (text from images), html elements, urls, etc.

Do feature extraction with ideally also pre-trained and initially frozen specialized nets for creating features from the text, timeframe-by-timeframe screenshots etc. and feed it all into a general model which predicts the next keypress/mouse event sent by the user.



There is enough of a signal in the data to theoretically be able to [more] accurately predict the next action a person will take if you as a human observed them enough and have full information of what they were just doing, and what they are seeing. Moreso if an algorithm does it.

The idea is the same as with text-prediction, however (for a simple example) even an exceptional human studying literature all their life, can only predict the next word in a book with limited accuracy. On the other hand, at least on paper, if one person studies all interactions someone has or at least all of those with their browser (and many other people's) they can likely very accurately predict the next thing a human will do based on what they see and what they've been doing.

In the case of pure text prediction it is one thing to only feed a neural network text, not related to anything, and another for the text (and everything) else to relate to real actions and other input. Simplified example - seeing the word red more often after interacting with an image that has more red in it. There is just more to connect to make an accurate model with a more full internal representations of it’s environment - and said environment is incredibly vast.

The thing the model would actually be modelling at the end of the day is [more or less] open-ended human behaviour.

Of course, the exciting part comes not as much from predicting the next action of real humans but from letting the model run freely - predict actions and perform them without there being a human any more. Would it visit sites successfully? Will it attempt to leave comments on articles or browse photos? Try to register or login anywhere?

I believe this is technically doable with enough resources, even today.


## Conclusion

Now, I am not deluded enough to assume that this will in any way straight lead to AGI but I expect it to supply us with to a lot of interesting insights, and the question is *how much would a model trained like that learn*? . Before, I might have thought the task would simply be too hard to start learning but after recent success in solving games, text prediction etc., as well as the fact that it can start predicting a lot of actions quite easily, and that a lot of the modules (e.g. text extraction) would be pre-trained (but again, not frozen), I suspect it will learn more than most people assume.
Also how much better (or if not better, how come) would for example the text-relevant portion of the model get after training as part of the full system?


Additionally, I am well aware that there are many obvious and non-obvious problems that would need to be solved in the process. Creating the data and sanitizing user’s credentials, other privacy considerations. Enormous training time and designing the right Network(s) etc. Is any of it infeasible for a sufficiently large organization, however? I think no - this can very well be attempted today.

<br>
<sub><sup>
I would be very interested to hear about arguments why this would or wouldn’t work, potential improvements or alternatives (e.g. having a RL and/or GAN-like approach with a similar task which is also doable), or if there is anyone working on something similar to this. Feel free to contact me about this or any related or unrelated offers for work or collaboration.
<sub><sup>
