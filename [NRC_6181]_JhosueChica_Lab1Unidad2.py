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
                    '''Como primera opcion se ingresan los datos de aspirante y se
                    llama al metodo de iniciar sesion, para despues continuar con el menu'''
                    # INGRESAR SESION ASPIRANTE
                    while True:
                        usuarioIngresado=str(input( "Ingrese su usuario de Apirante: " ))
                        claveIngresado=str(input( "Ingrese su clave: " ))                            
                        if (aspirante1.iniciarSesionAspirante(usuarioIngresado,claveIngresado)):
                            print("Usuario y clave registrado correctamente")
                            break
                        else:
                            print("Usuario o clave registrado incorrectamente")
                    
                elif(opcion == 2):
                    '''Como segunda opcion se registra una cuenta de Aspirante en la aplicacion'''
                    #CREAR CUENTA ASPIRANTE
                    nombreAsp=str(input("Ingrese su nombre completo: "))
                    while True:
                        edadAsp=int(input( "Ingrese su edad: "))
                        if (edadAsp>18):
                            break
                        else:
                            print("Valor no valido, la edad ingresada es incorrecta")
                    while True:
                        cedulaAsp=str(input( "Ingrese su Cedula: " ))
                        if (len(cedulaAsp)==10):
                            break
                        else:
                            print("Valor no valido, la cedula ingresada es incorrecta")
                    while True:
                        telefonoAsp=str(input( "Ingrese su Telefono: "))
                        if (len(telefonoAsp)==10):
                            break
                        else:
                            print("Valor no valido, el telefono ingresado es incorrecto")
                    provinciaAsp=str(input("Ingrese su provincia de recidencia: "))
                    direccionAsp=str(input("Ingrese su direccion de domicilio: "))
                    emailAsp=str(input("Ingrese su correo de trabajo: "))
                    aspirante1=Aspirante(nombreAsp, edadAsp, cedulaAsp, telefonoAsp, provinciaAsp, direccionAsp, emailAsp)
                    print(aspirante1.crearCuentaAspirante())
                    print(aspirante1.registro_tiempo("Regitro de cuenta de Aspirante"))
                    
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
                    '''Como primera opcion se ingresan los datos de empresa y se
                    llama al metodo de iniciar sesion, para despues continuar con el menu Empresa'''
                    # INGRESAR SESION EMPRESA
                    while True:
                        usuarioIngresado=str(input( "Ingrese su usuario de empresa: " ))
                        claveIngresado=str(input( "Ingrese su clave: " ))                            
                        if (empresa1.iniciarSesionEmpresa(usuarioIngresado,claveIngresado)):
                            print("Usuario y clave registrado correctamente")
                            break
                        else:
                            print("Usuario o clave registrado incorrectamente")

                elif(opcion == 2):
                    '''Como segunda opcion se registra una cuenta de Empresa en la aplicacion'''
                    # CREAR CUENTA EMPRESA
                    nombreEmp=str(input("Ingrese su nombre completo: "))
                    while True:
                        RUCEmp=str(input( "Ingrese su RUC de empresa: " ))
                        if (len(RUCEmp)==10):
                            break
                        else:
                            print("Valor no valido, la cedula ingresada es incorrecta")
                    while True:
                        telefonoEmp=str(input( "Ingrese su Telefono: "))
                        if (len(telefonoEmp)==10):
                            break
                        else:
                            print("Valor no valido, el telefono ingresado es incorrecto")
                    provinciaEmp=str(input("Ingrese su provincia de recidencia: "))
                    direccionEmp=str(input("Ingrese su direccion de domicilio: "))
                    emailEmp=str(input("Ingrese su correo de trabajo: "))
                    empresa1=Empresa(nombreEmp, RUCEmp, telefonoEmp, provinciaEmp, direccionEmp, emailEmp)
                    print(empresa1.crearCuentaEmpresa())
                    print(empresa1.registro_tiempo("Regitro de cuenta de Empresa"))

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
    provincia : str
        Priovincia del usuario registrado en el sistema en la cual el
        se encuentra el aspirante o la sede de la empresa.
    direccion : str
        Direccion del usuario registrado en el sistema en la cual el
        se encuentra el aspirante o la sede de la empresa.
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
    
    def __init__(self, nombre, telefono, provincia, direccion, email):
        ''' 
        Construye todos los atributos necesarios para el objeto Cliente.
        '''
        # atributo protegido
        self.nombre = nombre
        self.telefono = telefono
        self.provincia = provincia
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

class Aspirante(Usuario):
    ''' 
    Clase en donde se guardaran todos los datos que ingresa el 
    usuario como un Aspirante y la clave de este mismo.
    ...
    Atributos
    ----------
    nombre : str
        Nombre del usuario registrado en el sistema
    edad : int
        Edad del usuario registrado en el sistema
    cedula : int
        Documento de Identidad del apirante registrado en el sistema
    telefono : int
        Telefono del usuario registrado en el sistema 
    provincia : str
        Priovincia del usuario registrado en el sistema en la cual el
        se encuentra el aspirante.
    direccion : str
        Direccion del usuario registrado en el sistema en la cual el
        se encuentra el aspirante o la sede de la empresa.
    email : str
        E-mail de contacto del usuario registrado en el sistema
    _usuarioAsp: str
        El usuario del cliente asignada por el sistema a partir del
        resto de datos ingresados por el usuario
    _claveAsp: str
        La clave del cliente asignada por el sistema a partir del
        resto de datos ingresados por el usuario
    ...
    Metodos
    -------
    __init__(self):
        Construye todos los atributos necesarios para el objeto Aspirante.
    crearCuentaAspirante(self):
        Se realizan el ingreso de los datos principales del cliente para
        poder crear el usuario y la clave a partir de estos datos.
    iniciarSesionAspirante(self, usuarioIngresado, claveIngresado):
        Se realiza el ingreso de usuario y la clave, y se los compara con
        los valores de usuario y clave anteriormente registrados en el sistema
    '''
    def __init__(self, nombre, edad, cedula, telefono, provincia, direccion, email):
        ''' 
        Construye todos los atributos necesarios para el objeto Aspirante.
        '''
        self.edad = edad
        self.cedula = cedula
        super().__init__(nombre, telefono, provincia, direccion, email)
        '''atributo protegido'''
        self._usuarioAsp = "usuario"
        self._claveAsp = "clave"
        
    def crearCuentaAspirante(self):
        '''
        Se realizan el ingreso de los datos principales del usuario para
        poder crear la cuenta de aspirante y la clave a partir de estos datos.
        ...
        Parametros
        ----------
        *No tiene parametros*
        ...
        Retorna
        ----------
        return "Su usuario sera: ", self._usuarioAsp,". Su clave sera: ", self._claveAsp
            Retorna si el usuario y la clave han sido procesados.
        '''
        self._usuarioAsp=self.nombre+self.provincia[:3]+self.cedula[7:]
        self._claveAsp=self.direccion[:3]+self.telefono[6:8]+self.cedula[7:]
        return "Su usuario sera: ", self._usuarioAsp,". Su clave sera: ", self._claveAsp
        
    def iniciarSesionAspirante(self, usuarioIngresado, claveIngresado):
        '''
        Se realiza el ingreso de usuario y la clave, y se los compara con
        los valores de usuario y clave anteriormente registrados en el sistema.
        ...
        Parametros
        ----------
        usuarioIngresado : str
            Ususario ingresado para combrobar si es el mismo que el registrado en el sistema.
        claveIngresado : str
            Clave ingresada para combrobar si es el mismo que el registrado en el sistema.
        ...
        Retorna
        ----------
        return False
            Retorna False si la usuario o la clave estan mal ingresado.
        return True
            Retorna True si la usuario y la clave estan bien ingresado.
        '''
        if usuarioIngresado!=self._usuarioAsp:
            return False
        elif claveIngresado!=self._claveAsp:
            return False
        else:
            return True

class Empresa(Usuario):
    ''' 
    Clase en donde se guardaran todos los datos que ingresa el 
    usuario como un Empresa y la clave de este mismo.
    ...
    Atributos
    ----------
    nombre : str
        Nombre de la Empresa registrada en el sistema
    RUC : str
        Registro Único de Contribuyentes de la Empresa registrada en el sistema
    telefono : int
        Telefono de la Empresa registrada en el sistema 
    provincia : str
        Priovincia de la Empresa registrada en el sistema en la cual el
        se encuentra la sede de la empresa.
    direccion : str
        Direccion de la Empresa registrada en el sistema en la cual el
        se encuentra la sede de la empresa.
    email : str
        E-mail de contacto de la Empresa registrada en el sistema
    _usuarioEmp: str
        El usuario del cliente asignada por el sistema a partir del
        resto de datos ingresados por el usuario
    _claveEmp: str
        La clave del cliente asignada por el sistema a partir del
        resto de datos ingresados por el usuario
    ...
    Metodos
    -------
    __init__(self):
        Construye todos los atributos necesarios para el objeto Empresa.
    crearCuentaEmpresa(self):
        Se realizan el ingreso de los datos principales de la Empresa para
        poder crear el usuario y la clave a partir de estos datos.
    iniciarSesionEmpresa(self, usuarioIngresado, claveIngresado):
        Se realiza el ingreso de usuario y la clave, y se los compara con
        los valores de usuario y clave anteriormente registrados en el sistema
    '''
    def __init__(self, nombre, RUC, telefono, provincia, direccion, email):
        ''' 
        Construye todos los atributos necesarios para el objeto Empresa.
        '''
        self.RUC = RUC
        super().__init__(nombre, telefono, provincia, direccion, email)
        '''atributo protegido'''
        self._usuarioEmp = "usuario"
        self._claveEmp = "clave"
        
    def crearCuentaEmpresa(self):
        '''
        Se realizan el ingreso de los datos principales del usuario para
        poder crear la cuenta de aspirante y la clave a partir de estos datos.
        ...
        Parametros
        ----------
        *No tiene parametros*
        ...
        Retorna
        ----------
        return "Su usuario sera: ", self._usuarioAsp,". Su clave sera: ", self._claveAsp
            Retorna si el usuario y la clave han sido procesados.
        '''
        self._usuarioEmp=self.nombre+self.provincia[:3]+self.RUC[7:]
        self._claveEmp=self.direccion[:3]+self.telefono[6:8]+self.RUC[7:]
        return "Su usuario sera: ", self._usuarioEmp,". Su clave sera: ", self._claveEmp
        
    def iniciarSesionEmpresa(self, usuarioIngresado, claveIngresado):
        '''
        Se realiza el ingreso de usuario y la clave, y se los compara con
        los valores de usuario y clave anteriormente registrados en el sistema.
        ...
        Parametros
        ----------
        usuarioIngresado : str
            Ususario ingresado para combrobar si es el mismo que el registrado en el sistema.
        claveIngresado : str
            Clave ingresada para combrobar si es el mismo que el registrado en el sistema.
        ...
        Retorna
        ----------
        return False
            Retorna False si la usuario o la clave estan mal ingresado.
        return True
            Retorna True si la usuario y la clave estan bien ingresado.
        '''
        if usuarioIngresado!=self._usuarioEmp:
            return False
        elif claveIngresado!=self._claveEmp:
            return False
        else:
            return True



if __name__ == '__main__':
    '''Instanciar objeto de la clase Aspirante'''
    aspirante1=Aspirante(0,0,0,0,0,0,0) 
    '''Instanciar objeto de la clase Empresa'''
    empresa1=Empresa(0,0,0,0,0,0)
    Menu()
