from pyglet.gl import *
from typing import Sequence

def render_hull_from_vertices(verts:Sequence['Vec2d'], color=None):
    """
    Renders the outline of a hull via a list of vertices.
    :param verts: Sequence of vertices in a sensible order
    :param color: Color given as vec3f. Defaults to white / (1.0,1.0,1.0) if not given
    :param batch: Batch this should be part of, if part of a larger rendering operation
    :return: None
    """

    if not color:
        color = (1.0, 0.0, 0.0)

    glBegin(GL_LINES)
    glColor3f(*color)
        
    for v in verts:
        glVertex2f(v[0], v[1])
    if len(verts) > 0:
        glVertex2f(verts[0][0], verts[0][1])  # Line from end to start to close the hull
    
    glEnd()
    
