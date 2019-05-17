import sympy as sym

"""
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

   
a = [[1,0,0],[0,1,0],[0,0,1]]
b = [[2,0,0],[0,0,0],[0,0,-1]]

construct_rotation(a,b)
"""

# quero uma função que dado o objeto e o ponto de origem, calcule o tensor de inercia
#objetos inicias: /placa_2d/paralelepipedo/cilindro/cone/


class disco(object):

	def __init__(self):

		self.x_1, self.x_2, self.x_3, t = sym.symbols('x_1, x_2, x_3, t', real=True) #variaveis

		self.M, self.r, self.h, self.a = sym.symbols('M,r,h,a',real=True) #caracteristicas do obejto fisico

		dimens  = [[self.r,0,self.a],[t,0,(sym.pi*2)]] #dimensoes do obejto com relação a origem do sistema de coordenadas

		X = [(self.r*sym.cos(t)), (self.r*sym.sin(t)),0] # disco em coordenadas polares

		self.sigma = self.M/(sym.pi * (self.a**2)) #densidade de massa 

		self.disco_I_cm = sym.zeros(3,3)

		#primeiro calcular no centro de massa e depois utlizar rotação e teorema dos eixos paralelos

		for i in range(0,3):
			for j in range(0,3):

				if i==j:

					self.disco_I_cm[i,j] = sym.integrate(self.sigma * ((self.r**2) - (X[i]**2)) * self.r , (dimens[0][0], dimens[0][1],dimens[0][2]), (dimens[1][0],dimens[1][1],dimens[1][2]))


				else:

					self.disco_I_cm[i,j] = sym.integrate( -self.sigma * X[i] * X[j] * self.r, (dimens[0][0], dimens[0][1],dimens[0][2]), (dimens[1][0], dimens[1][1],dimens[1][2]))

		print('tensor de inercia no centro de massa do disco:\n')
		sym.pprint((self.disco_I_cm))
		print('\n\n\n')




class placa(object):

	def __init__(self):

		self.x_1, self.x_2, self.x_3 = sym.symbols('x_1, x_2, x_3', real=True) #variaveis

		self.M, self.a, self.b = sym.symbols('M,a,b',real=True) #caracteristicas do obejto fisico

		self.dimens  = [[self.x_1,-self.a/2,self.a/2],[self.x_2,-self.b/2,self.b/2],[0,0,0]] #dimensoes do obejto com relção a origem do sistema de coordenadas

		self.raio_2 = [self.x_2**2,self.x_1**2, self.x_1**2 + self.x_2**2] #raio de giração ao quadrado em relação aos eixos x1 x2 e x3 respectivamente

		self.sigma = self.M/(self.a*self.b) #densidade de massa 

		self.tensor_I_cm = sym.zeros(3,3)


		#primeiro calcular no centro de massa e depois utlizar rotação e teorema dos eixos paralelos

		for i in range(0,3):
			for j in range(0,3):

				if i==j:

					self.tensor_I_cm[i,j] = sym.integrate(self.sigma * (self.raio_2[i]), (self.dimens[0][0], self.dimens[0][1],self.dimens[0][2]), (self.dimens[1][0], self.dimens[1][1],self.dimens[1][2]))

				else:

					self.tensor_I_cm[i,j] = sym.integrate( -self.sigma *  self.dimens[i][0] * self.dimens[j][0], (self.dimens[0][0], self.dimens[0][1],self.dimens[0][2]), (self.dimens[1][0], self.dimens[1][1],self.dimens[1][2]))

		print('tensor de inercia no centro de massa:\n')
		sym.pprint(sym.simplify(self.tensor_I_cm))
		print('\n\n\n')

	def calcular_I_em(self): #x e y são coordenadas em relação ao objeto, f( variabel, operacao, variavel operacao, variavel operacao   ) 

		#aplicar rotações e ou translação para recalcular o tensor de inercia

		self.x = 0
		self.y = 0
		self.z = 0

		self.R = sym.Matrix([self.x,self.y,self.z])  #vetor que localiza o novo ponto onde será calculado o tensor de inercia

		self.RR = self.R.T * self.R  #modulo do vetor R

		tensor_I = sym.zeros(3,3)

		for i in range(0,3):
			for j in range(0,3):

				if i==j:
					tensor_I[i,j] = self.tensor_I_cm[i,j] + (self.M*( (self.RR[0]) - (self.R[i]*self.R[j])))

				else:
					tensor_I[i,j] = self.tensor_I_cm[i,j] - (self.M*(self.R[i]*self.R[j]))

		print('tensor de inercia no ponto x=%s, y=%s:\n'%(self.x,self.y))
		sym.pprint(sym.simplify(tensor_I))
		print('\n\n\n')

		return tensor_I

	def rotacao_diagonal(self,I): # aplica uma rotação em I de um angulo que forma tg(teta) = a/b, ou seja o novo eixo setará na diagonal da placa

		diag_rot_matrix = (1/(sym.sqrt(self.a**2 + self.b**2)))*sym.Matrix([[self.b,self.a,0],
																		 [-self.a,self.b,0],
																		 [0,0,1]])

		tensor_I_diagon = diag_rot_matrix*I

		print('tensor de inercia no eixo diagonal da placa:')
		sym.pprint(sym.simplify(tensor_I_diagon))
		print('\n\n\n')



p = disco()






