from solid.utils import *
from pinball.playfield import Playfield
from pinball.parts.ballhole import BallHole
from pinball.parts.flipper import Flipper 
from pinball.parts.slingshot import Slingshot 
from pinball.parts.popbumper import PopBumper
from pinball.parts.laneguide import LaneGuideAssembly
from pinball.parts.post import Post
from pinball.parts.standuptarget import RoundStandupTarget, NarrowStandupTarget, WideStandupTarget

pf_width = 600
pf_height = 1200
playfield_variant="msdos"

class VerticalUpKicker(BallHole):
	#TODO: Implement this in SolidPinball
	pass

class BallDrain(BallHole):
	#TODO: Implement this in SolidPinball
	pass

#TODO: SolidPinball: implement the PopBumper body 3d-model
#TODO: SolidPinball: implement the Slingshot assembly 3d-model (including rubber and 3 posts automatically)
#TODO: SolidPinball: implement the 3d-model of the StardupTargets metal part

pf = Playfield(pf_width, pf_height)
pf.append_parts([
  {'part': BallDrain(), 'position': [303,53.5] }, # ball drain
  {'part': BallHole(), 'position': [340.2,1116.3] }, # hidden entrance
  {'part': BallHole(), 'position': [135,942] }, # million loop
  {'part': BallHole(), 'position': [266,873.5] }, # arcade
  {'part': VerticalUpKicker(), 'position': [39.5,703.5] }, # snack
  {'part': Flipper(angle=-65, rubber_color="red"), 'position': [62.5, 746.5] }, #top left
  {'part': Flipper(angle=-35, rubber_color="red"), 'position':   [197.5, 181.5] }, #bottom left
  {'part': Flipper(angle=180+35, rubber_color="red"), 'position': [402, 181.5] }, #bottom right
  {'part': Slingshot(angle=-71.5), 'position': [300 - 172, 351] }, # left
  {'part': Slingshot(angle=71.5), 'position': [300 + 172, 351] }, # right
  {'part': PopBumper(cap_color="orangered", game="partyland", version=playfield_variant), 'position': [543.0, 670.0] },
  {'part': PopBumper(cap_color="royalblue", game="partyland", version=playfield_variant), 'position': [388.8, 631.7] },
  {'part': PopBumper(cap_color="lightseagreen", game="partyland", version=playfield_variant), 'position': [437.3, 690.0] },
# These could also be a 3 drop-target bank
  {'part': RoundStandupTarget(), 'position': [311-33*cos(-71.5*3.1415/180), 626-33*sin(-71.5*3.1415/180)], 'rotation':-71.5  }, # H
  {'part': RoundStandupTarget(), 'position': [311, 626], 'rotation':-71.5  }, # I
  {'part': RoundStandupTarget(), 'position': [311+33*cos(-71.5*3.1415/180), 626+33*sin(-71.5*3.1415/180)], 'rotation':-71.5  }, # T
  {'part': WideStandupTarget(), 'position': [278, 807], 'rotation':-20 }, # arcade
])

#TODO: SolidPinball: Implement BallLauncher()
#TODO: SolidPinball: Implement RollOverSwitch()
#TODO: SolidPinball: Implement RollUnderSwitch()
#TODO: SolidPinball: Implement RollUnderGate()
#TODO: SolidPinball: Implement Light()
#TODO: SolidPinball: Implement Ramp()
#TODO: SolidPinball: Implement WireBridge()

posts_coords = [
  [617.305 ,342.080],
  [410.4616, 200.030],
  [215.2479, 60.473],
  [1501.7811, 342.080],
  [1708.6245, 200.030],
  [1903.8382, 60.474]
];

#TODO: fix the list of Post() coordinates
#for coords in posts_coords:
#	pf.append(Post(), position=coords)


#TODO: SolidPinball: make it possible to attach a mini-playfield to a main one
# (perhaps the Playfield class could also inherit from the Part class?)
# (Or should we implement a MiniPlayfield class?)

#TODO: SolidPinball: make it possible to construct a Playfield by passing a vector
# curve that defines it's layout shape

upper_pf = Playfield(pf_width, pf_height)
upper_pf.append_parts([
  {'part': LaneGuideAssembly(), 'position': [310, 1076] },
  {'part': LaneGuideAssembly(), 'position': [366, 1066] },
  {'part': LaneGuideAssembly(), 'position': [422, 1076] },
])

#This exports the design to a .scad file that you can render with OpenSCAD
#Available for download at www.openscad.org
scad_render_to_file( pf.assembly(), 'outputs/SCAD/partyland_assembly.scad')

# This renders only the playfield wood with the holes you need:
# Exporting it to an STL file you can CNC mill your own pinball playfield! 
scad_render_to_file( pf.wood(), 'outputs/SCAD/partyland_playfield_wood.scad')

