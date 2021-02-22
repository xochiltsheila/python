importar  sys

clientes  = [
    {
        'nombre' : 'Pablo' ,
        'empresa' : 'Google' ,
        'email' : 'pablo@google.com' ,
        'position' : 'Ingeniero de software' ,
     }
     {
         'nombre' : 'Ricardo' ,
         'empresa' : 'Facebook' ,
         'correo electrónico' : 'ricardo@facebook.com' ,
         'position' : 'Date enginee' ,
     }      
]

def  create_client ( cliente ):
     clientes globales

    si el  cliente  no está  en los  clientes :
        Clientes . añadir ( cliente )
    otra cosa :
        imprimir ( 'cliente ya está en cliente \' s list' )
        
def  list_clients ():
    para  idx , cliente  en  enumerar ( clientes ):
        print ( '{uid} │ {nombre} │ {empresa} │ {correo electrónico} │ {posición}' . formato (
            uid = idx ,
            nombre = cliente [ 'nombre' ],
            empresa = cliente [ 'empresa' ],
            email = cliente [ 'email' ],
            posición = cliente [ 'posición' ]))

def  update_client ( client_name , Update_Name ):
     clientes globales

    si  client_name  en los  clientes :
        índice  =  clientes . índice ( nombre_cliente )
        clientes [ índice ] =  nombre_actualizado
    otra cosa :
         imprimir ( 'Cliente no en los clientes \' s list' )
         
def  delete_client ( nombre_cliente ):
     clientes globales

    si  client_name  en los  clientes :
        clientes  eliminan ( nombre_cliente )
    otra cosa :
        imprimir ( 'Cliente no en los clientes \' s list' )

def  search_client ( nombre_cliente ):
    para  cliente  en  clientes :
        if  client  ! =  client_name :
            Seguir
        otra cosa :
            volver  verdadero

def  _get_client_field ( nombre_campo ):
    campo  =  Ninguno

    mientras  no es  campo :
        campo  =  entrada ( '¿Qué es el cliente {}?' . formato ( nombre_campo ))

     campo de retorno   

def  _get_client_name ():
    client_name  =  Ninguno

    mientras  no sea  client_name :
        client_name  =  input ( '¿Cuál es el nombre del cliente?' )

        si  nombre_cliente  ==  'salir' :
            client_name  =  Ninguno
            descanso
     si  no es  client_name :
         sys . salir ()

     devolver  nombre_cliente    



def  _print_Welcome ():
    print ( 'Bienvenido A PLATZI VENTAS' )
    imprimir ( '*'  *  50 )
    print ( '¿Qué te gustaría hacer hoy?' )
    print ( '[C] reate cliente' )
    print ( '[L] ist clientes' )
    print ( '[U] pdate cliente' )
    print ( '[D] elete cliente' )
    print ( '[S] earch client' )


if  __name__  ==  '__main__' :
    _print_Welcome ()

    comando  =  entrada ()
    comando  =  comando . superior ()

    si  comando  ==  'C' :
        cliente  = {
            'nombre' : _get_client_field ( 'nombre' ),
            'empresa' : _get_client_field ( 'empresa' ),
            'email' : _get_client_field ( 'email' ),
            'posición' : _get_client_field ( 'posición' ),
        }
        create_client ( cliente )
        list_clients ()
     comando  elif ==  'L' :
        list_clients ()
     comando  elif ==  'U' :
        nombre_cliente  =  _get_client_name ()
        nombre_actualizado  =  input ( '¿Cuál es el nombre del nuevo cliente?' )

        cliente_actualizado ( nombre_cliente , nombre_actualizado )
        list_clients ()
     comando  elif ==  'D' :
        nombre_cliente  =  _get_client_name ()
        update_client_name  =  input ( '¿Cuál es el nombre de cliente actualizado?' )
        update_client ( nombre_cliente , update_client_name )
        list_clients ()
         si se  encuentra :
          print ( "El cliente en la lista de clientes" )

       otra cosa :
          print ( 'El cliente: {} no está en nuestra lista de clientes' , formato ( nombre_cliente ))
 
    otra cosa :
        print ( 'Comando no válido' )