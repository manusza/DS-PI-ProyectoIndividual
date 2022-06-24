import pandas as pd 

archivo= input("Que archivo delta va a ingresar? Clientes, Ventas, Compras, Proovedores, Localidades, Precio o Sucursales?")
nombre_archivo=input("Ingrese el nombre de su archivo con su extension, EJ: Clientes.csv")



def concat_archivos(archivo, nombre_archivo):
    
    if archivo.lower() == "clientes":

        df = pd.read_csv(nombre_archivo, sep=';')
        df.to_csv('Clientes.csv', index= False , sep= ';', header= None, mode='a')

        #aplicamos un drop duplicate row en caso de que el delta venga con duplicados, me quedo con la ultima informacion en caso que el cliente haya cambiado algo de su ficha tecnica

        df1= pd.read_csv('Clientes.csv', sep= ';')
        df1= df1.drop_duplicates(subset=['ID'], keep='last')
        df1.to_csv('Clientes.csv', index= False, sep=';')
        print(df1.dtypes)

    elif archivo.lower() == "ventas":

        df = pd.read_csv(nombre_archivo, sep=',')
        df.to_csv('Venta.csv', index= False, sep= ',', header= None, mode='a')
        df1= pd.read_csv('Venta.csv', sep=',')
        df1= df1.drop_duplicates(subset=['IdVenta'], keep='first')
        df1.to_csv('Venta.csv', index= False, sep=',')

    elif archivo.lower() == "compras":

        df = pd.read_csv(nombre_archivo, sep=',')
        df.to_csv('Compra.csv', index= False, sep= ',', header= None, mode='a')
        df1= pd.read_csv('Compra.csv')
        df1= df1.drop_duplicates(subset=['IdCompra'], keep='first')
        df1.to_csv('Compra.csv', index= False, sep=',')

    elif archivo.lower() == "proveedores":

        df = pd.read_csv(nombre_archivo, sep=',')
        df.to_csv('Proveedores.csv', index= False, sep= ',', header= None, mode='a')
        df1= pd.read_csv('Proveedores.csv',encoding = "Latin-1")
        df1= df1.drop_duplicates(subset=['IDProveedor'], keep='first')
        df1.to_csv('Proveedores.csv', index= False, sep=',')

    elif archivo.lower() == "sucursales":

        df = pd.read_csv(nombre_archivo, sep=',')
        df.to_csv('Sucursales.csv', index= False, sep= ',', header= None, mode='a')
        df1= pd.read_csv('Sucursales.csv')
        df1= df1.drop_duplicates(subset=['ID'], keep='first')
        df1.to_csv('Sucursales.csv', index= False, sep=',')

    elif archivo.lower() == "gasto":

        df = pd.read_csv(nombre_archivo, sep=',')
        df.to_csv('Gasto.csv', index= False, sep= ',', header= None, mode='a')
        df1= pd.read_csv('Gasto.csv')
        df1= df1.drop_duplicates(subset=['IdGasto'], keep='first')
        df1.to_csv('Gasto.csv', index= False, sep=',')

    elif archivo.lower() == "localidades":

        df = pd.read_csv(nombre_archivo, sep=',')
        df.to_csv('Localidades.csv', index= False, sep= ',', header= None, mode='a')
        df1= pd.read_csv('Localidades.csv')
        df1= df1.drop_duplicates(subset=['categoria'], keep='first')
        df1.to_csv('Localidades.csv', index= False, sep=',')


concat_archivos(archivo, nombre_archivo)
print("Sus archivos han sido actualizados!")

#creamos un input asi no se nos cierra directamente el script
input("")