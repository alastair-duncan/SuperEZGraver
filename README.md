# SuperEZGraver

This is the Super EZ Graver project documentation. If any of the documentation doesn't make sense or links are broken etc please let me know and I'll do my best to fix it.

## Background

I started engraving early in 2019 after coming across some engraving videos by [Shaun Hughes](https://www.youtube.com/c/express375/videos) on YouTube. I started off with some push engraving while I ordered up the parts for Shaun's "Home made hand engraving machine". I built one of these and proceeded to hack my way through some brass and copper practice plates and I also enjoy making jewellery with enamel. I have now aquired a microscope which has had a marked effect on my engraving, previously I used an optivisor with an added loupe but it is not adequate for my old eyes.

Shaun had the idea of a solenoid powered engraving system over 2 years ago and posted a video on [YouTube](https://www.youtube.com/watch?v=2177lFeMcNw) and one of the engraving forums. He wasn't the first to come up with the idea, as far as I can find out that was [Steve Lindsay back in 1979](https://www.handengravetools.com/air-engraver-evolution.htm). So its nothing new although the availability of cheap electronic components and the advent of 3d printing has enabled me to put these together to make the Super EZ Graver. He also has tinkered with a Rolson engraver uses an AC driven laminated solenoid and power is regulated using a fan speed controller [YouTube](https://youtu.be//Ke8bDoJ-2io). Jerry Moralles uses a similar tool to engrave coins very effectively: [YouTube](https://www.youtube.com/channel/UC4XOksM98SMPymVrHOIaOxg). He also has made some additions that allow for the mounting of small abrasive stones to mechanise sanding and finishing very effectively.

Prior to this the McShirley power mallet utilises very similar technology by using a solenoid with presets for power and speed and a number of potentiometers which are used for fine control, you can view their 1975 [patent here](https://patentimages.storage.googleapis.com/81/7c/a0/0b0333b2f1563e/US3921044.pdf). There is also a video showing the [McShirley Power Mallet in action](https://www.youtube.com/watch?v=bn_Ea9L7uJU)

The Super EZ Graver that I have built is based around a XRN-13/30TLS solenoid. This is a small tubular solenoid that is 13mm in diameter and 30mm long. It will not plow its way through all materials put before it. You may find that for your purpose it does not pack the punch that you want but it suits me. I've had to adapt my engraving so that it is a bit more refined, which I think is an improvement for me, I no longer bury the tool and break tips. There may be a solenoid out there that will give all of the power and finess that everyone needs in a small package but I doubt it, I suspect that more than one toolpiece will be required and hopefully I'll add more designs and information to this project when it becomes available.

The controller and power source can handle much more powerful solenoids but I've only tried out a couple, I've made a [list of the ones I've tried](docs/solenoids.md) and added some comments. If you've tried others let me know and I'll add them to the list.

There are now 2 versions of the controler that I've built. The original based on the Ardiono Uno and the newer version based on the Pi Pico. The Pi Pico does not require a separate PWM "speed" controller for regulation of the power sent to the solenoid.

[Ardiono Uno controller](Arduino.md)

[Pico controller](Pico.md)

# Handpiece

I've created two 3d modelled handpieces in the open source 3d modelling application [Blender](https://www.blender.org/). 

there are no mk2 and mk3 versions 

### Mk2 Handpiece

The [blender source files](docs/design/XRN13-30TLS/mk2/blender) are available to download as well as the [stl](docs/design/XRN13-30TLS/mk2/blender/stl). There is a YouTube video on how to [setup the handpiece](https://www.youtube.com/watch?v=aNY35ATTJbg) and also the [Mk2](https://youtu.be/sa4kAdcZSkc) version which has a brass sleve insert. This was first produced using petg but it may be better to use a more heat conductive material such as [ice9](https://tcpoly.com/shop/) for better heat dissapation. I've not tried this yet.

### Mk3 Handpiece

This handpiece has the addition of a mount for a 25mm fan and is experimental. It suits my hand size and is comfortable. There are no threads on this handle, it does require some 2.5mm machine screws and nuts and a threaded insert in the handle for a stroke length adjuster. I will make a video of how its put together at some point and link to it from here. The handpiece works without the fan but if you want some additional cooling when pushing the Super EZ Graver hard then the fan really helps. Something like [this](https://www.google.com/search?q=micro+fan+25mm+12v+dc) I've used a 12v dc version but there are other voltages available.

[Anarasha](https://www.youtube.com/channel/UCKSbczGXmN4zeG3NeuPGLAg) had a problem with the blender version of the 3D model as the blender model has tolerances built in to it which causes problems with his slicer(I think). He has kindly produced a [fusion360](docs/design/XRN13-30TLS/fusion360) model of the handpiece which has the [stl](docs/design/XRN13-30TLS/fusion360/stl) and STEP files if this suits you better.

The first handpiece that I made was fabricated from brass and delrin. A YouTube video is available for the [handpiece](https://www.youtube.com/watch?v=D4yPBS8mucQ) along with a video on the handpiece [design refinement](https://www.youtube.com/watch?v=ALAtECnq1Rg)


# Gravers et al

[Carbide rods - UK](http://intertool.co.uk.websitebuilder.prositehosting.co.uk/carbide-rod)

[Carbide rods - US](https://centennialcarbide.com/products-page/carbide-rod-blanks/)

[3/32" HSS graver blanks - UK](https://www.ebay.co.uk/itm/360515374956) or [Gloster Tooling Supplies](https://www.glostertooling.co.uk/)

[Carbalt gravers](https://www.airgraver.com/graver-blanks.htm)

[Graver sharpening templates](http://airgraver.com/sharpening.html)