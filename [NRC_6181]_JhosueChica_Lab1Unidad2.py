'''
Se pretende solventar el problema del desempleo por medio del desarrollo de una
aplicación, en la cual una persona desempleada se pueda registrar y buscar trabajo
por medio de diferentes categorías para poder tener en cuenta. En esta aplicación
las empresas podrán ingresar como cuentas de empresa, para poder publicar
modificar propuestas de trabajo (con sus respectivas indicaciones), las cuales serán
visibles para el resto de usuarios dentro de la aplicación.
'''

from time import localtime, asctime

def Menu():
    '''
    Para la creacion del menu principal se hace la utiliza de un bucle While 
    con condicion de True la cual pobroca bucle infinito, en el cual si ingresa
    una opcion mal siguira pidiendo el dato hasta que ingrese uno correcto.
    1. Como primera opcion se registra una cuenta de usuario en la aplicacion
    2. Como segunda opcion se llama al metodo de iniciar sesion,
       para despues continuar con el menu de pedidos
    3. Como tercera opcion se ejecuta un break y se cierra el programa
    '''
    while(True): # bucle infinito mientras que el valor de la condicion devuelva false
        print("==============================================")
        print("||             MULTI-TRABAJO                ||")
        print("==============================================")
        print("|| 1.- ENTRAR COMO ASPIRANTE                ||")
        print("|| 2.- ENTRAR COMO EMPRESA                  ||")
        print("|| 3.- SALIR                                ||")
        print("==============================================")
        opcion=int(input("Bienvenido, ¿Qué desea realizar hoy?: "))
        if(opcion == 1):
            while(True): # bucle infinito mientras que el valor de la condicion devuelva false
                print("==============================================")
                print("||           ENTRAR COMO ASPIRANTE          ||")
                print("==============================================")
                print("|| 1.- INGRESAR SESION - ASPIRANTE          ||")
                print("|| 2.- CREAR CUENTA - ASPIRANTE             ||")
                print("|| 3.- VOLVER ATRAS                         ||")
                print("==============================================")
                opcion=int(input("Bienvenido, ¿Qué desea realizar hoy?: "))
                if(opcion == 1):
                    '''Como primera opcion se llama al metodo de iniciar sesion,
                    para despues continuar con el menu'''
                    # INGRESAR SESION ASPIRANTE
                    
                elif(opcion == 2):
                    '''Como segunda opcion se registra una cuenta de Aspirante en la aplicacion'''
                    # CREAR CUENTA ASPIRANTE
                    
                elif(opcion == 3):
                    '''Como tercera opcion se ejecuta un break y se cierra el programa'''
                    print("Gracias por visitarnos :)")
                    break
                else:
                    print("Opcion incorrecta, pruebe de  nuevo.")
            
        elif(opcion == 2):
            while(True): # bucle infinito mientras que el valor de la condicion devuelva false
                print("==============================================")
                print("||           ENTRAR COMO EMPRESA            ||")
                print("==============================================")
                print("|| 1.- INGRESAR SESION - EMPRESA            ||")
                print("|| 2.- CREAR CUENTA - EMPRESA               ||")
                print("|| 3.- VOLVER ATRAS                         ||")
                print("==============================================")
                opcion=int(input("Bienvenido, ¿Qué desea realizar hoy?: "))
                if(opcion == 1):
                    '''Como primera opcion se llama al metodo de iniciar sesion,
                    para despues continuar con el menu'''
                    # INGRESAR SESION EMPRESA
                    
                elif(opcion == 2):
                    '''Como segunda opcion se registra una cuenta de Aspirante en la aplicacion'''
                    # CREAR CUENTA EMPRESA
                    
                elif(opcion == 3):
                    '''Como tercera opcion se ejecuta un break y se cierra el programa'''
                    print("Gracias por visitarnos :)")
                    break
                else:
                    print("Opcion incorrecta, pruebe de  nuevo.")
            
        elif(opcion == 3):
            ''' como tercera opcion se ejecuta un break y se cierra el programa'''
            print("Gracias por visitarnos :)")
            break
        else:
            print("Opcion incorrecta, pruebe de  nuevo.")


class Usuario():
    ''' 
    Clase en donde se guardaran todos los datos que ingresa el 
    Clienta como el usuario y la clave de este mismo.
    ...
    Atributos
    ----------
    nombre : str
        Nombre del usuario registrado en el sistema
    telefono : int
        Telefono del usuario registrado en el sistema 
    direccion : str
        Direccion del usuario registrado en el sistema en la cual el
        pedido del delibery sera entregado
    email : str
        E-mail de contacto del usuario registrado en el sistema 
    tiempo : lista
        Registro de las acciones realizadas por el usuario
    ...
    Metodos
    -------
    __init__(self):
        Construye todos los atributos necesarios para el objeto Usuario.
    registro_tiempo(self,accion):
        Metodo que añade una accion al registro del tiempo. Retorna la ultima accion realizada.
    registro_acciones(self):
        Metodo que presenta la lista de acciones registradas por tiempo.
    '''
    
    def __init__(self, nombre, telefono, direccion, email):
        ''' 
        Construye todos los atributos necesarios para el objeto Cliente.
        '''
        # atributo protegido
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.email = email
        self.tiempo=[]
        
    def registro_tiempo(self,accion):
        '''
        Metodo que añade una accion al registro del tiempo. 
        ...
        Parametros
        ----------
        accion : str
            Accion que se registra en el tiempo determinada.
        ...
        Retorna
        ----------
        return registro
            Retorna la ultima accion realizada.
        '''
        registro=accion+": "+asctime(localtime())
        self.tiempo.append(registro)
        return registro
        
    def registro_acciones(self):
        '''
        Metodo que presenta la lista de acciones registradas por tiempo.
        ...
        Parametros
        ----------
        *No tiene parametros*
        '''
        for i in range (0,len(self.tiempo)):
            print(self.tiempo[i])

if __name__ == '__main__':
    '''Instanciar objeto de la clase Aspirante'''
    aspirante1=Usuario(0,0,0,0) 
    '''Instanciar objeto de la clase Empresa'''
    empresa1=Usuario(0,0,0,0)
    Menu()
