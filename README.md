PARTYLandRemake
===============

PARTY Land Remake - Building a real-life playfield replica of the PARTY Land pinball table from the Amiga game Pinball Fantasies

![A preview of the playfield design implemented using the SolidPinball python library](https://raw.github.com/felipesanches/PinballFantasiesRemake/master/PARTYLandRemake_preview.png)

Dependencies
------------

> sudo pip install solidpinball  
> sudo apt-get install openscad  

Hacking
-------

Use the command "make preview" to generate only the SCAD file.  
Then, open outputs/SCAD/partyland_assembly.scad using Openscad and 
make sure you enable the "Automatic Reload and Preview" option in the
"Design" menu. This will make it much easier to see the results of modifications to
the "CAD/PARTYLandRemake.py" file as soon as you re-run "make preview"  

There are lots of parts that still need to be modeled. The proper place for the parts
models is in the SolidPinball code repository. Feel free to contribute code to this repository
or to SolidPinball. I'll review any pul requests as soon as possible.

Licensing
---------

Although the original design of the PARTY Land pinball table does not belong to me, the 3d models,
SVG/DXF vectors and SCAD scripts here are authored by me (Felipe Sanches <juca@members.fsf.org>) and
I publish these files under the GNU GPLv3 or later so that other DIY pinball enthusiasts can
build upon my work and hopefully we can have more people building their own homebrew pinball machines. :-)


