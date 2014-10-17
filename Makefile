STL_FILES = \
	outputs/STL/partyland_playfield_wood.stl

preview: outputs/SCAD/partyland_assembly.scad

all: $(STL_FILES)

%.scad: CAD/PARTYLandRemake.py
	mkdir -p outputs/SCAD
	python CAD/PARTYLandRemake.py

outputs/STL/%.stl: outputs/SCAD/%.scad
	mkdir -p outputs/STL
	openscad -o $@ $<

clean:
	rm outputs -rf


