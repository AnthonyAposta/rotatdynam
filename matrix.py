import sympy as sym


a, t, p  = sym.symbols('a,t,p', real=True)


R_1 = sym.Matrix([[1,0,0],[0,sym.cos(t),sym.sin(t)],[0,-sym.sin(t),sym.cos(t)]])
R_2 = sym.Matrix([[sym.cos(a),0,-sym.sin(a)],[0,1,0],[sym.sin(a),0,sym.cos(a)]])
R_3 = sym.Matrix([[sym.cos(p),sym.sin(p),0],[-sym.sin(p),sym.cos(p),0],[0,0,1]])

rotation  = R_1*R_2*R_3
print(rotation.shape)

#sym.pprint(rotation)

rotation = rotation.subs([(t,sym.pi),(a,sym.pi/2),(p,sym.pi/4)])

sym.pprint(rotation)
#print(rotation.det())


def construct_rotation(b_in,b_out): #tem a a base inicial e final e quer saber a matrix de transf

    b_in = sym.Matrix(b_in)
    b_out = sym.Matrix(b_out)

    transformation = (b_in * (b_out.T))

    sym.pprint(transformation)

"""    
a = [[1,0,0],[0,1,0],[0,0,1]]
b = [[2,0,0],[0,0,0],[0,0,-1]]

construct_rotation(a,b)
"""

