class coding():
	_nombre=["cero","uno","dos","tres","cuatro","cinco","seis","siete","ocho","nueve","diez","once","doce","trece","catorce","quince","veinte","treinta","cuarenta","cincuenta","secenta","setenta","ochenta","noventa","cien"]
	def __init__(self):
		self.proceso()
	def proceso(self):
		a=10
		t=6
		e=-1
		num=""
		dec=""
		for i in range(0,101):
			if(i<16):
				e+=1
				num=self._nombre[e]
				print"%s = %s" %(i,num)
				if i==15:
					e=6
			else:
				dec=self._nombre[a]
				num=self._nombre[e]
				if e>0:
					print "%s = %s y %s" %(i,dec,num)
				else:
					print "%s = %s" %(i,dec)
				e+=1
				if e==10:
					a=a+t
					t=1
					e=0 
p=coding()