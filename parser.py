from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a command
     Any command that requires varuments must have those varuments in the second command.
     The commands are as follows:
         command: add a command to the edge matrix -
               takes 6 varuemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 varuments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 varuments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 varuments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the commands of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the commands of the edge matrix to the screen
               save the screen to a file -
               takes 1 varument (file name)
         quit: end parsing

See the file script for an example of the file format
"""

def parse_file( fname, points, transform, screen, color ):
      file = open(fname, "r")
      commands = file.read().split('\n')
      file.close()
      i = 0
      while i < len(commands):
            if commands[i] == "line":
                  coords = commands[i+1].split(' ')
                  add_edge(points, int(coords[0]), int(coords[1]), int(coords[2]), int(coords[3]), int(coords[4]), int(coords[5]))
                  i += 2
            elif commands[i] == "ident":
                  ident(transform)
                  i += 1
            elif commands[i] == "scale":
                  dil = commands[i+1].split(' ')
                  scale = make_scale(int(dil[0]), int(dil[1]), int(dil[2]))
                  matrix_mult(scale, transform)
                  i += 2
            elif commands[i] == "move":
                  units = commands[i+1].split(' ')
                  translate = make_translate(int(units[0]), int(units[1]), int(units[2]))
                  matrix_mult(translate, transform)
                  i += 2
            elif commands[i] == "rotate":
                  var = commands[i+1].split(' ')
                  axis = var[0]
                  theta = float(var[1])
                  rotate = None
                  if axis == 'x':
                        rotate = make_rotX(theta)
                  elif axis == 'y':
                        rotate = make_rotY(theta)
                  elif axis == 'z':
                        rotate = make_rotZ(theta)
                  matrix_mult(rotate, transform)
                  i += 2
            
            elif commands[i] == "apply":
                  matrix_mult(transform, points)
                  i += 1
            elif commands[i] == "display":
                  clear_screen(screen)
                  draw_lines(points, screen, color)
                  display(screen)
                  i += 1
            elif commands[i] == "save":
                  fname = commands[i+1].split(' ')[0]
                  clear_screen(screen)
                  draw_lines(points, screen, color)
                  save_ppm(screen, fname)
                  save_ppm_ascii(screen, fname)
                  save_extension(screen, fname)
                  i += 1
            elif commands[i] == "quit":
                  break
            else:
                  break
