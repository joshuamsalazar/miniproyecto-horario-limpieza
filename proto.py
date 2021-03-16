#Funcion principal
import random
inqs = [] 												#Lista con los inquilinos registrados

print('**********************************\t Bienvenido \t*************************************')
print('*Generador de horarios de limpieza v0.1\n')
def main():	
	print('\t --->>> Seleccione una opcion: \t \t 1. Añadir un nuevo inquilino a casa  ')
	print('\t \t \t \t \t \t 2. Eliminar un inquilino de la lista')
	print('\t \t \t \t \t \t 3. Mostrar listado de los inquilinos actuales')
	print('\t \t \t \t \t \t 4. Exportar archivo con los datos de los inquilinos registrados')
	print('\t \t \t \t \t \t 5. Generar horario de limpieza')
	op_m = input('') #aqui se guarda la opcion que ingresa el usuario por teclado
	if 1 == int(op_m):
		if len(inqs) == 6:
			print('Se ha excedido el numero de inquilinos.')
		else:
			inqs.append( NuevoInq() )						#1.	Ingresa nuevo
	elif 2 == int(op_m):
		ElimInq()										#2. Elimina 
	elif 3 == int(op_m):
		MostrarInqs()									#3. Muestra
	elif 4 == int(op_m):
		GuardarDatos()
	elif 5 == int(op_m):
		MostrarHorario()
	else: 
		print('Opcion no existente. Intentalo otra vez...')
		input('')
		main()
	if eval(input('¿Desea realizar otra tarea?\t 1. Si\t Cualquier tecla. No\n')) ==  1 :
		main()
	else:
		exit()
		
def GuardarDatos():
	if len(inqs) == 0:
		print('No existen registros de inquilinos. (Puede aniadir nuevos desde el menu principal)')
	archivo = open('Inquilinos.txt','w')
	archivo.write('Nombre del Inquilino \t Cedula de Identidad \t Semestre\n\n')
	for inq in inqs:
		cadena = str(inq.nom) + '\t' + str(inq.cid) + '\t' +str(inq.nvl) + '\n'
		archivo.write(cadena)
	archivo.close()
	
def MostrarHorario():
	if len(inqs) == 0:
		print('No existen registros de inquilinos. (Puede aniadir nuevos desde el menu principal)')
		
		
	if len(inqs) == 1:
		pos_rand = random.randint( 0, 5 )
		semana[ pos_rand ].bno = inqs[0].nom 
		pos_rand = random.randint( 0, 5 )
		semana[ pos_rand ].csn = inqs[0].nom
		pos_rand = random.randint( 0, 5 )
		semana[ pos_rand ].sla = inqs[0].nom
		
	elif len(inqs) == 2:
		despl1 = random.randint(1,2)
		despl2 = random.randint(1,2)
		despl3 = random.randint(1,2)
		semana[0 - despl1 ].bno = inqs[0].nom
		semana[0 - despl2 ].csn = inqs[0].nom	
		semana[0 - despl3 ].sla = inqs[0].nom
		semana[3 - despl1 ].bno = inqs[1].nom
		semana[3 - despl2 ].csn = inqs[1].nom	
		semana[3 - despl3 ].sla = inqs[1].nom
		
	elif len(inqs) == 3:	
		despl1 = random.randint(1,2)
		despl2 = random.randint(1,2)
		if despl1 == despl2:
			despl1 = random.randint(1,2)
		despl3 = random.randint(1,2)
		semana[0 - despl1 ].bno = inqs[0].nom
		semana[0 - despl2 ].csn = inqs[2].nom	
		semana[0 - despl3 ].sla = inqs[1].nom
		semana[3 - despl1 ].bno = inqs[1].nom
		semana[3 - despl2 ].csn = inqs[0].nom	
		semana[3 - despl3 ].sla = inqs[2].nom
		
	elif len(inqs) == 4:	
		despl1 = random.randint(0,1)
		despl2 = random.randint(0,1)
		if despl1 == despl2:
			despl1 = random.randint(0,1)
		despl3 = random.randint(0,1)
		semana[0 - despl1 ].bno = inqs[0].nom
		semana[0 - despl2 ].csn = inqs[3].nom	
		semana[0 - despl3 ].sla = inqs[2].nom
		semana[2 - despl1 ].bno = inqs[1].nom
		semana[2 - despl2 ].csn = inqs[0].nom	
		semana[2 - despl3 ].sla = inqs[3].nom
		semana[4 - despl1 ].bno = inqs[2].nom
		semana[4 - despl2 ].csn = inqs[1].nom	
		semana[4 - despl3 ].sla = inqs[0].nom
		
	elif len(inqs) == 5:	
		despl1 = random.randint(0,1)
		despl2 = random.randint(0,1)
		if despl1 == despl2:
			despl1 = random.randint(0,1)
		despl3 = random.randint(0,1)
		semana[0 - despl1 ].bno = inqs[0].nom
		semana[0 - despl2 ].csn = inqs[3].nom	
		semana[0 - despl3 ].sla = inqs[1].nom
		semana[2 - despl1 ].bno = inqs[1].nom
		semana[2 - despl2 ].csn = inqs[4].nom	
		semana[2 - despl3 ].sla = inqs[2].nom
		semana[4 - despl1 ].bno = inqs[2].nom
		semana[4 - despl2 ].csn = inqs[0].nom	
		semana[4 - despl3 ].sla = inqs[3].nom
		
	elif len(inqs) == 6:
		despl1 = random.randint(0,1)
		despl2 = random.randint(0,1)
		if despl1 == despl2:
			despl1 = random.randint(0,1)
		despl3 = random.randint(0,1)
		semana[0 - despl1 ].bno = inqs[0].nom
		semana[0 - despl2 ].csn = inqs[3].nom	
		semana[0 - despl3 ].sla = inqs[0].nom
		semana[2 - despl1 ].bno = inqs[1].nom
		semana[2 - despl2 ].csn = inqs[4].nom	
		semana[2 - despl3 ].sla = inqs[1].nom
		semana[4 - despl1 ].bno = inqs[2].nom
		semana[4 - despl2 ].csn = inqs[5].nom	
		semana[4 - despl3 ].sla = inqs[2].nom
	
		
	
	
	
	print(' | \t  Lunes \t Martes \t Miercoles \t Jueves \t Viernes \t Sabado        |')
	print(' |Banio:   ', semana[0].bno, '\t' , semana[1].bno, '\t' , semana[2].bno, '\t' , semana[3].bno, '\t' , semana[4].bno, '\t' , semana[5].bno,'\t |')
	print(' |Cocina   ', semana[0].csn, '\t' , semana[1].csn, '\t' , semana[2].csn, '\t' , semana[3].csn, '\t' , semana[4].csn, '\t' , semana[5].csn,' \t |')
	print(' |Sala   ', semana[0].sla, '\t' , semana[1].sla, '\t' , semana[2].sla, '\t' , semana[3].sla, '\t' , semana[4].sla, '\t' , semana[5].sla,' \t |')
	
	for elem in semana:
		elem.bno = '---'
		elem.csn = '---'
		elem.sla = '---'
		
def MostrarInqs():
	print('\t *** Inquilinos registrados *** ')		
	if len(inqs) == 0:
		print('No hay inquilinos registrados')
	for i in range( len(inqs) ):							#Bucle que imprime los datos de cada alumno registrado 
		print('Inquilino #', i+1)
		print('\t Nombre:\t', inqs[i].nom)
		print('\t Cedula:\t', inqs[i].cid)
		print('\t Semestre:\t', inqs[i].nvl)
		
def ElimInq():
	cid = input('Ingresa la cedula eliminar: ')				#Otorga una cedula que buscar
	#if type(cid) == int:
	
	encontrado = False										#Condicion inicial de busqueda. No se la encuentra aun!
	n_busq = 0
	while not encontrado and n_busq < len(inqs):			#Busca hasta que encuentra o hasta buscar en todos los elemento
		print(n_busq, '\t', len(inqs), '\t', n_busq < len(inqs))
		if cid == inqs[n_busq].cid:
			encontrado = True
			inqs.pop( n_busq )
			
		n_busq += 1
		
	if encontrado == False:
		print('El inquilino con Cedula', cid , 'no existe')

	#else:
		#print('El dato ingresado no es un numero. Intentelo de nuevo...')
	#	ElimInq()

def NuevoInq():											#Clase que guarda un nuevo alumno a partir de los datos que ingresemos
	if len(inqs) == 6:
		print('Se ha excedido el numero de inquilinos.')
		inq = 0 
	else:
		inq = inquilino()
		inq.cid = input('Ingresa la cedula del inquilino: \t')
		inq.nom = input('Ingresa el primer nombre del inquilino: \t')
			
		inq.nvl = input('Ingresa el semestre que cursa actualmente: \t')
	return inq
	
class inquilino():											#Clase que guarda los datos del inquilino
	nom = ''														#Nombre, cedula de identidad, y nivel/semestre en curso
	cid = ''
	nvl = ''
	nvu = 0			#Numero de veces asignado
	
class tareaDeHoy():											#Clase que guarda el encargado de la: 
	bno = '---'  													#Baño, cocina, y sala
	csn = '---'
	sla = '---'
	
lun = tareaDeHoy()											#Agrego a cada dia una clase que contiene los encargados]
mar = tareaDeHoy()
mie = tareaDeHoy()
jue = tareaDeHoy()
vie = tareaDeHoy()
sab = tareaDeHoy()


semana = [lun ,mar ,mie , jue ,vie, sab ]					#Lista para la semana #Posciciones:	para lunes -> 0. # martes -> 1  # sabado -> 5


main()
