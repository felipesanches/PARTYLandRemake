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

pf = Playfield(pf_width, pf_height)
pf.append_parts([
  {'part': BallHole(), 'position': [pf_width/2,60] }, #ball drain
  {'part': BallHole(), 'position': [510, 720] },
  {'part': BallHole(), 'position': [200, 630] },
  {'part': BallHole(), 'position': [120, 670] },
  {'part': Flipper(angle=-42, rubber_color="orangered"), 'position': [pf_width/2 - 100, 200] },
  {'part': Flipper(angle=180+42, rubber_color="orangered"), 'position': [pf_width/2 + 100, 200] },
  {'part': Slingshot(angle=-70), 'position': [pf_width/2 - 130, 330] },
  {'part': Slingshot(angle=+70), 'position': [pf_width/2 + 130, 330] },
  {'part': PopBumper(cap_color="darkred"), 'position': [330, 630] },
  {'part': PopBumper(cap_color="darkblue"), 'position': [380, 690] },
  {'part': PopBumper(cap_color="darkgreen"), 'position': [410, 580] },
  {'part': LaneGuideAssembly(), 'position': [210, 920] },
  {'part': LaneGuideAssembly(), 'position': [260, 900] },
  {'part': LaneGuideAssembly(), 'position': [310, 920] },
  {'part': RoundStandupTarget(), 'position': [40, 820], 'rotation': 30 },
  {'part': NarrowStandupTarget(), 'position': [80, 840] },
  {'part': WideStandupTarget(), 'position': [120, 820], 'rotation': -30 },
  {'part': Post(), 'position': [360, 500] }
])

#This exports the design to a .scad file that you can render with OpenSCAD
#Available for download at www.openscad.org
scad_render_to_file( pf.assembly(), 'outputs/SCAD/partyland_assembly.scad')

# This renders only the playfield wood with the holes you need:
# Exporting it to an STL file you can CNC mill your own pinball playfield! 
scad_render_to_file( pf.wood(), 'outputs/SCAD/partyland_playfield_wood.scad')

