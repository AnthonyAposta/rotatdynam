import sympy as sm

### passos
### 1- input da energia potencial
### 3- encontrar os pontos de equilibrio
### 4- encontrar os pontos estaveis
### 5- escrever a equação para w e p
### 6- resolver a quação para w det(V0-w^2M0)=0
### 7- encontrar as frequencias W
### 8- utilizar (V0-w^2M0)p para enontrar p
### 9- escrever a solução geral para perturbação


class  perturb_solut(object):
	"""docstring for ClassName"""
	

	def __init__(self, arg):

		## no final U deve ser imput, en~tão as coordenada generalizadas devem se transfomadas em simbolos
		
		m,g,l,t_1,t_2 = sm.symbols('m,g,l',real=True)

		self.mass = [m,3*m]

		R = [ [],
			  [] ]

		self.U = (4*m*g*l*sm.cos(t_1))-(3*m*g*l*sm.cos(t_2))


	def mass_matrix(self):
		pass
		#return M

	def V_matrix(self):
		pass
		#return V

	def find_w(self):
		pass
		#solve det(v0 - X.M0) = 0 for X

	def find_p(self):
		pass
		#solve (v0 - X.M0)p = 0 for p

	def general_solution(self):
		pass
		#return etha



		