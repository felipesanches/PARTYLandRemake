STL_FILES = \
	outputs/STL/partyland_playfield_wood.stl

all: $(STL_FILES)

%.scad: CAD/PARTYLandRemake.py
	mkdir -p outputs/SCAD
	python CAD/PARTYLandRemake.py

outputs/STL/%.stl: outputs/SCAD/%.scad
	mkdir -p outputs/STL
	openscad -o $@ $<

clean:
	rm outputs -rf


