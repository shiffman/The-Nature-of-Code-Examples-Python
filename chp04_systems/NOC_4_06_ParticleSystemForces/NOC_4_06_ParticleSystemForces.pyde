# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Python port by Abhik Pal

from particle_system import ParticleSystem

def setup():
    size(640, 360)
    global ps 
    ps = ParticleSystem(PVector(width/2, 50))

def draw():
    background(255)

    global ps
    gravity = PVector(0, 0.1)
    ps.apply_force(gravity)

    ps.add_particle()
    ps.run()