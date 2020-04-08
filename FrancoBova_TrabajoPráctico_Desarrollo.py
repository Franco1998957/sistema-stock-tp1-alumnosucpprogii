from tkinter import*
from tkinter import messagebox

window=Tk()
window.title(" Despensa el Gringo ")
window.geometry('880x650')
window.configure(background="darkgreen")

producto1= Lapiz
producto2= Aspirina
producto3= Borrador
producto4= Pan

tiposDeProductos= {(list=Papeleria, Supermercado, Drogueria)}

mercaderiaEnBodega1= 30
mercaderiaEnBodega2= 20
mercaderiaEnBodega3= 25
mercaderiaEnBodega4= 15

precioPorUnidad1= 0
precioPorUnidad2= 0
precioPorUnidad3= 0
precioPorUnidad4= 0

venta1= txtventa1.get()
venta2= txtventa2.get()
venta3= txtventa3.get()
venta4= txtventa3.get()

cantidadMinima1= 10
cantidadMinima2= 7
cantidadMinima3= 9
cantidadMinima4= 8

cantidadMaxima1= 5
cantidadMaxima2= 5
cantidadMaxima3= 5
cantidadMaxima4= 5

ivaPapeleria= 16/100
ivaSupermercado= 4/100
ivaDrogueria= 12/100

def tiposDeProductos():
    Papeleria=["Papeleria"]
    Supermercado=["Supermercado"]
    Drogueria=["Drogueria"]
    
def mercaderiaEnBodega1():
    if mercaderiaEnBodega1<=cantidadMinima1:
        messagebox.showinfo(title=("Mercaderia", message(f"No hay producto en la {mercaderiaEnBodega1}"))
    elif mercaderiaEnBodega1>cantidadMinima1:
        messagebox.showinfo(title=("Mercaderia", message(f"Si hay producto en la {mercaderiaEnBodega1}"))

def mercaderiaEnBodega2():
     if mercaderiaEnBodega2<=cantidadMinima2:
        messagebox.showinfo(title=("Mercaderia", message(f"No hay producto en la {mercaderiaEnBodega2}"))
    elif mercaderiaEnBodega2>cantidadMinima2:
        messagebox.showinfo(title=("Mercaderia", message(f"Si hay producto en la {mercaderiaEnBodega2}"))

def mercaderiaEnBodega3():
     if mercaderiaEnBodega3<=cantidadMinima3:
        messagebox.showinfo(title=("Mercaderia", message(f"No hay producto en la {mercaderiaEnBodega3}"))
    elif mercaderiaEnBodega3>cantidadMinima3:
        messagebox.showinfo(title=("Mercaderia", message(f"Si hay producto en la {mercaderiaEnBodega3}"))

def mercaderiaEnBodega4():
     if mercaderiaEnBodega4<=cantidadMinima4:
        messagebox.showinfo(title=("Mercaderia", message(f"No hay producto en la {mercaderiaEnBodega4}"))
    elif mercaderiaEnBodega4>cantidadMinima4:
        messagebox.showinfo(title=("Mercaderia", message(f"Si hay producto en la {mercaderiaEnBodega4}"))
    
def precioPorUnidad1():
    if precioPorUnidad12==0:
        messagebox.showinfo(title=("Precio", message(f"El producto no tiene el  {precioPorUnidad1}"))
    else precioPorUnidad1>0:
        messagebox.showinfo(title=("Precio", message(f"El producto no tiene el  {precioPorUnidad1}"))
        
def precioPorUnidad2():
    if precioPorUnidad2!=10:
        messagebox.showinfo(title=("Precio", message(f"El producto no tiene el  {precioPorUnidad2}"))
    elif precioPorUnidad3>0:
        messagebox.showinfo(title=("Precio", message(f"El producto no tiene el  {precioPorUnidad2}")):
    
def precioPorUnidad3():
    if precioPorUnidad3==0:
        messagebox.showinfo(title=("Precio", message(f"El producto no tiene el  {precioPorUnidad3}"))
    else precioPorUnidad3>0:
       messagebox.showinfo(title=("Precio", message(f"El producto no tiene el  {precioPorUnidad3}"))

def precioPorUnidad4():
    if precioPorUnidad4!=10:
        messagebox.showinfo(title=("Precio", message(f"El producto no tiene el  {precioPorUnidad4}"))
    elif precioPorUnidad4>0:
        messagebox.showinfo(title=("Precio", message(f"El producto no tiene el  {precioPorUnidad4}")):

def realizar():
    lapiz.configure(window, text=cambiarProducto1)
    cambio.destroy()

Tipo = Label(window, text=" Tipo ", font=("Arial Black", 10), fg="red", bg="white")
Tipo_cambio=entry(cambio,width=15).place(x=0, y=0)
mercaderiaEnBodega= Label(window, text=" Tipo ", font=("Arial Black", 10), fg="red", bg="white")
mercaderiaEnBodega_cambio=entry(cambio,width=15).place(x=0, y=0)
precioPorUnidad= Label(window, text=" Tipo ", font=("Arial Black", 10), fg="red", bg="white")
precioPorUnidad_cambio=entry(cambio,width=15).place(x=0, y=0)
cantidadMinima= Label(window, text=" Tipo ", font=("Arial Black", 10), fg="red", bg="white")
cantidadMinima_cambio=entry(cambio,width=15).place(x=0, y=0)

def realizar():
    aspirina.configure(window, text=cambiarProducto2)
    cambio.destroy()

Tipo = Label(window, text=" Tipo ", font=("Arial Black", 10), fg="red", bg="white")
Tipo_cambio=entry(cambio,width=15).place(x=0, y=0)
mercaderiaEnBodega= Label(window, text=" Tipo ", font=("Arial Black", 10), fg="red", bg="white")
mercaderiaEnBodega_cambio=entry(cambio,width=15).place(x=0, y=0)
precioPorUnidad= Label(window, text=" Tipo ", font=("Arial Black", 10), fg="red", bg="white")
precioPorUnidad_cambio=entry(cambio,width=15).place(x=0, y=0)
cantidadMinima= Label(window, text=" Tipo ", font=("Arial Black", 10), fg="red", bg="white")
cantidadMinima_cambio=entry(cambio,width=15).place(x=0, y=0)

def realizar():
    borrador.configure(window, text=cambiarProducto3)
    cambio.destroy()

Tipo = Label(window, text=" Tipo ", font=("Arial Black", 10), fg="red", bg="white")
Tipo_cambio=entry(cambio,width=15).place(x=0, y=0)
mercaderiaEnBodega= Label(window, text=" Tipo ", font=("Arial Black", 10), fg="red", bg="white")
mercaderiaEnBodega_cambio=entry(cambio,width=15).place(x=0, y=0)
precioPorUnidad= Label(window, text=" Tipo ", font=("Arial Black", 10), fg="red", bg="white")
precioPorUnidad_cambio=entry(cambio,width=15).place(x=0, y=0)
cantidadMinima= Label(window, text=" Tipo ", font=("Arial Black", 10), fg="red", bg="white")
cantidadMinima_cambio=entry(cambio,width=15).place(x=0, y=0)

def realizar():
    pan.configure(window, text=cambiarProducto4)
    cambio.destroy()

Tipo = Label(window, text=" Tipo ", font=("Arial Black", 10), fg="red", bg="white")
Tipo_cambio=entry(cambio,width=15).place(x=0, y=0)
mercaderiaEnBodega= Label(window, text=" Tipo ", font=("Arial Black", 10), fg="red", bg="white")
mercaderiaEnBodega_cambio=entry(cambio,width=15).place(x=0, y=0)
precioPorUnidad= Label(window, text=" Tipo ", font=("Arial Black", 10), fg="red", bg="white")
precioPorUnidad_cambio=entry(cambio,width=15).place(x=0, y=0)
cantidadMinima= Label(window, text=" Tipo ", font=("Arial Black", 10), fg="red", bg="white")
cantidadMinima_cambio=entry(cambio,width=15).place(x=0, y=0)

def venta1():
    global mercaderiaEnBodega1
    global cantidadMinima1
    global venta1
    def guardarVenta():
        global venta1
        global mercaderiaEnBodega1
        venta = int(valorVendidos.cget("text"))
        cantidad = int(valorCantidad.cget("text"))
        res = str(cantidad-1)
        valorTotal = str(valor+1)
        valorVendidos.configure(text=valorTotal)
        valorCantidad.configure(text=res)
        if res==0:
            messagebox.showinfo(title=("No hay más stock del producto que necesita"), message="advertencia")
        else:
            venta1=Tk()
            venta1.title("Vender")
            venta1.geometry("400x90")
            venta1.mainloop()

def venta2():
    global mercaderiaEnBodega2
    global cantidadMinima2
    global venta2
    def guardarVenta():
        global venta2
        global mercaderiaEnBodega2
        venta = int(valorVendidos.cget("text"))
        valorTotal = str(valor+1)
        valorVendidos1.configure(text=valorTotal)
     else:
         venta2=Tk()
         venta2.title("Vender")
         venta2.geometry("400x90")
         venta2.mainloop()
    
def venta3():
    global mercaderiaEnBodega3
    global cantidadMinima3
    global venta3
    def guardarVenta():
        global venta3
        global mercaderiaEnBodega3
        venta = int(valorVendidos.cget("text"))
        cantidad = int(valorCantidad.cget("text"))
        res = str(cantidad-1)
        valorTotal = str(valor+1)
        valorVendidos.configure(text=valorTotal)
        valorCantidad.configure(text=res)
        if res==0:
            messagebox.showinfo(title=("No hay más stock del producto que necesita"), menssage="advertencia")
        else:
            venta3=Tk()
            venta3.title("Vender")
            venta3.geometry("400x90")
            venta3.mainloop()

def venta4():
    global mercaderiaEnBodega4
    global cantidadMinima4
    global venta4
    def guardarVenta():
        global venta4
        global mercaderiaEnBodega4
        venta = int(valorVendidos.cget("text"))
        valorTotal = str(valor+1)
        valorVendidos1.configure(text=valorTotal)
    else:
        venta4=Tk()
        venta4.title("Vender")
        venta4.geometry("400x90")
        venta4.destroy()
        venta4.mainloop()

def abastecimiento1():
    if bodega1<cantidadMínima1:
        window2=Tk()
        window2.title(" Despensa el Gringo ")
        window2.geometry('120x180')
        window2.configure(background="red")
        lbl = Label(window, text=" Hace falta abastecer la bodega ", font=("Arial Black", 10), fg="red", bg="white")
        lbl.place(x=0, y=0)
        txt=entry(window,width=15)
        txt.place(x=0, y=0)
        btn= Button(window, text=" Guardar Cambios ", command=guardar)
        btn.place(x=0, y=0)
        window2.mainloop()
    else:
        messagebox.showinfo(title=("No hay suficiente mercaderia necesita abastecer el producto"))

def abastecimiento2():
    if bodega2<cantidadMínima2:
        window2=Tk()
        window2.title(" Despensa el Gringo ")
        window2.geometry('120x180')
        window2.configure(background="red")
        lbl = Label(window, text=" Hace falta abastecer la bodega ", font=("Arial Black", 10), fg="red", bg="white")
        lbl.place(x=0, y=0)
        txt=entry(window,width=15)
        txt.place(x=0, y=0)
        btn= Button(window, text=" Guardar Cambios ", command=guardar)
        btn.place(x=0, y=0)
        window2.mainloop()
    else:
        messagebox.showinfo(title=("No hay suficiente mercaderia necesita abastecer el producto"))

def abastecimiento3():
    if bodega3<cantidadMínima3:
        window2=Tk()
        window2.title(" Despensa el Gringo ")
        window2.geometry('120x180')
        window2.configure(background="red")
        lbl = Label(window, text=" Hace falta abastecer la bodega ", font=("Arial Black", 10), fg="red", bg="white")
        lbl.place(x=0, y=0)
        txt=entry(window,width=15)
        txt.place(x=0, y=0)
        btn= Button(window, text=" Guardar Cambios ", command=guardar)
        btn.place(x=0, y=0)
        window2.mainloop()
    else:
        messagebox.showinfo(title=("No hay suficiente mercaderia necesita abastecer el producto"))

def abastecimiento4():
    if bodega4<cantidadMínima4:
        window2=Tk()
        window2.title(" Despensa el Gringo ")
        window2.geometry('120x180')
        window2.configure(background="red")
        lbl = Label(window, text=" Hace falta abastecer la bodega ", font=("Arial Black", 10), fg="red", bg="white")
        lbl.place(x=0, y=0)
        txt=entry(window,width=15)
        txt.place(x=0, y=0)
        btn= Button(window, text=" Guardar Cambios ", command=guardar)
        btn.place(x=0, y=0)
        window2.mainloop()
    else:
        messagebox.showinfo(title=("No hay suficiente mercaderia necesita abastecer el producto"))

def cambiarProducto1():
    cambios=Tk()
    cambios.title("Cambiar Producto")
    cambios.geometry("400x150")

    nuevoNombre_prod=Label(cambios, text="Nuevo nombre", font=("Arial", 13), borderwidth=2, width=15, relief="groove")
    nuevoNombre_prod.place(x=0, y=0)
    nuevoNombreProd=Entry(cambios, width=20)
    nuevoNombreProd.place(x=230, y=0)

    nuevoTipo_producto=Label(cambios, text="Tipo producto", font=("Arial", 13), borderwidth=2, width=15, relief="groove")
    nuevoTipo_producto.place(x=0, y=20)
    nuevoTipoProd=ttk.Combobox(cambios, width=20)
    nuevoTipoProd.place(x=230, y=20)
    nuevoTipoProd["values"]=Tipos

    precioUnitario_nuevo_producto=Label(cambios, text="Precio Unitario", font=("Arial", 13), borderwidth=2, width=15, relief="groove")
    precioUnitario_nuevo_producto.place(x=0, y=40)
    precioUNuevoProd=Entry(cambios, width=20)
    precioUNuevoProd.place(x=230, y=40)

    cantidadEnBodega_nuevo_producto=Label(cambios, text="Mercaderia en Bodega", font=("Arial", 13), borderwidth=2, width=15, relief="groove")
    cantidadEnBodega_nuevo_producto.place(x=0, y=60)
    cantEnBodNewProd=Entry(cambios, width=20)
    cantEnBodNewProd.place(x=230, y=60)

    cantidadMinima_nuevo_producto=Label(cambios, text="Cantidad Minima", font=("Arial", 13), borderwidth=2, width=15, relief="groove")
    cantidadMinima_nuevo_producto.place(x=0, y=80)
    cantMinNuevoProd=Entry(cambios, width=20)
    cantMinNuevoProd.place(x=230, y=80)

    def guardar_cambios():
        prodLapiz.configure(nuevoNombreProd.get()) 
        Tipo1.configure(nuevoTipoProd.get()) 
        precioUnitario1.configure(precioUNuevoProd.get()) 
        cantidadEnbodega1.configure(cantBodNuevoProd.get()) 
        cantidadMinimo1.configure(cantMinNuevi¿oProd.get()) 
        messagebox.showinfo(text="Cambios", message="Los cambios se realizaron correctamente")
        cambios.destroy()
        
def cambiarProducto2():
    cambios=Tk()
    cambios.title("Cambiar Producto")
    cambios.geometry("400x150")

    nuevoNombre_prod=Label(cambios, text="Nuevo nombre", font=("Arial", 13), borderwidth=2, width=15, relief="groove")
    nuevoNombre_prod.place(x=0, y=0)
    nuevoNombreProd=Entry(cambios, width=20)
    nuevoNombreProd.place(x=230, y=0)

    nuevoTipo_producto=Label(cambios, text="Tipo producto", font=("Arial", 13), borderwidth=2, width=15, relief="groove")
    nuevoTipo_producto.place(x=0, y=20)
    nuevoTipoProd=ttk.Combobox(cambios, width=20)
    nuevoTipoProd.place(x=230, y=20)
    nuevoTipoProd["values"]=Tipos

    precioUnitario_nuevo_producto=Label(cambios, text="Precio Unitario", font=("Arial", 13), borderwidth=2, width=15, relief="groove")
    precioUnitario_nuevo_producto.place(x=0, y=40)
    precioUNuevoProd=Entry(cambios, width=20)
    precioUNuevoProd.place(x=230, y=40)

    cantidadEnBodega_nuevo_producto=Label(cambios, text="Mercaderia en Bodega", font=("Arial", 13), borderwidth=2, width=15, relief="groove")
    cantidadEnBodega_nuevo_producto.place(x=0, y=60)
    cantEnBodNewProd=Entry(cambios, width=20)
    cantEnBodNewProd.place(x=230, y=60)

    cantidadMinima_nuevo_producto=Label(cambios, text="Cantidad Minima", font=("Arial", 13), borderwidth=2, width=15, relief="groove")
    cantidadMinima_nuevo_producto.place(x=0, y=80)
    cantMinNuevoProd=Entry(cambios, width=20)
    cantMinNuevoProd.place(x=230, y=80)

    def guardar_cambios():
        prodLapiz.configure(nuevoNombreProd.get()) 
        Tipo1.configure(nuevoTipoProd.get()) 
        precioUnitario2.configure(precioUNuevoProd.get()) 
        cantidadEnbodega2.configure(cantBodNuevoProd.get()) 
        cantidadMinimo2.configure(cantMinNuevi¿oProd.get()) 
        messagebox.showinfo(text="Cambios", message="Los cambios se realizaron correctamente")
        cambios.destroy()

def cambiarProducto3():
    cambios=Tk()
    cambios.title("Cambiar Producto")
    cambios.geometry("400x150")

    nuevoNombre_prod=Label(cambios, text="Nuevo nombre", font=("Arial", 13), borderwidth=2, width=15, relief="groove")
    nuevoNombre_prod.place(x=0, y=0)
    nuevoNombreProd=Entry(cambios, width=20)
    nuevoNombreProd.place(x=230, y=0)

    nuevoTipo_producto=Label(cambios, text="Tipo producto", font=("Arial", 13), borderwidth=2, width=15, relief="groove")
    nuevoTipo_producto.place(x=0, y=20)
    nuevoTipoProd=ttk.Combobox(cambios, width=20)
    nuevoTipoProd.place(x=230, y=20)
    nuevoTipoProd["values"]=Tipos

    precioUnitario_nuevo_producto=Label(cambios, text="Precio Unitario", font=("Arial", 13), borderwidth=2, width=15, relief="groove")
    precioUnitario_nuevo_producto.place(x=0, y=40)
    precioUNuevoProd=Entry(cambios, width=20)
    precioUNuevoProd.place(x=230, y=40)

    cantidadEnBodega_nuevo_producto=Label(cambios, text="Mercaderia en Bodega", font=("Arial", 13), borderwidth=2, width=15, relief="groove")
    cantidadEnBodega_nuevo_producto.place(x=0, y=60)
    cantEnBodNewProd=Entry(cambios, width=20)
    cantEnBodNewProd.place(x=230, y=60)

    cantidadMinima_nuevo_producto=Label(cambios, text="Cantidad Minima", font=("Arial", 13), borderwidth=2, width=15, relief="groove")
    cantidadMinima_nuevo_producto.place(x=0, y=80)
    cantMinNuevoProd=Entry(cambios, width=20)
    cantMinNuevoProd.place(x=230, y=80)

    def guardar_cambios():
        prodLapiz.configure(nuevoNombreProd.get()) 
        Tipo1.configure(nuevoTipoProd.get()) 
        precioUnitario3.configure(precioUNuevoProd.get()) 
        cantidadEnbodega3.configure(cantBodNuevoProd.get()) 
        cantidadMinimo3.configure(cantMinNuevi¿oProd.get()) 
        messagebox.showinfo(text="Cambios", message="Los cambios se realizaron correctamente")
        cambios.destroy()

def cambiarProducto4():
    cambios=Tk()
    cambios.title("Cambiar Producto")
    cambios.geometry("400x150")

    nuevoNombre_prod=Label(cambios, text="Nuevo nombre", font=("Arial", 13), borderwidth=2, width=15, relief="groove")
    nuevoNombre_prod.place(x=0, y=0)
    nuevoNombreProd=Entry(cambios, width=20)
    nuevoNombreProd.place(x=230, y=0)

    nuevoTipo_producto=Label(cambios, text="Tipo producto", font=("Arial", 13), borderwidth=2, width=15, relief="groove")
    nuevoTipo_producto.place(x=0, y=20)
    nuevoTipoProd=ttk.Combobox(cambios, width=20)
    nuevoTipoProd.place(x=230, y=20)
    nuevoTipoProd["values"]=Tipos

    precioUnitario_nuevo_producto=Label(cambios, text="Precio Unitario", font=("Arial", 13), borderwidth=2, width=15, relief="groove")
    precioUnitario_nuevo_producto.place(x=0, y=40)
    precioUNuevoProd=Entry(cambios, width=20)
    precioUNuevoProd.place(x=230, y=40)

    cantidadEnBodega_nuevo_producto=Label(cambios, text="Mercaderia en Bodega", font=("Arial", 13), borderwidth=2, width=15, relief="groove")
    cantidadEnBodega_nuevo_producto.place(x=0, y=60)
    cantEnBodNewProd=Entry(cambios, width=20)
    cantEnBodNewProd.place(x=230, y=60)

    cantidadMinima_nuevo_producto=Label(cambios, text="Cantidad Minima", font=("Arial", 13), borderwidth=2, width=15, relief="groove")
    cantidadMinima_nuevo_producto.place(x=0, y=80)
    cantMinNuevoProd=Entry(cambios, width=20)
    cantMinNuevoProd.place(x=230, y=80)

    def guardar_cambios():
        prodLapiz.configure(nuevoNombreProd.get()) 
        Tipo1.configure(nuevoTipoProd.get()) 
        precioUnitario4.configure(precioUNuevoProd.get()) 
        cantidadEnbodega4.configure(cantBodNuevoProd.get()) 
        cantidadMinimo4.configure(cantMinNuevi¿oProd.get()) 
        messagebox.showinfo(text="Cambios", message="Los cambios se realizaron correctamente")
        cambios.destroy()

def productoMásVendido():
    global prodLapiz
    global prodAspirina
    global prodBorrador
    global prodPan
    textoLapiz = prodLapiz.cget('text')
    textoAspirina=prodAspirina.cget('text')
    textoBorrador=prodBorrador.cget('text')
    textoPan=prodPan.cget('text')
    if venta1<venta2 and venta1<venta3 and venta1<venta4:
        messagebox.showinfo(title=("Producto Más Vendido", message(f"El producto más vendido es el {producto1}"))
    elif venta2<venta1 and venta2<venta3 and venta2<venta4:
       messagebox.showinfo(title=("Producto Más Vendido", message(f"El producto más vendido es el {producto2}"))
    elif venta3<venta1 and venta3<venta2 and venta3<venta4:
       messagebox.showinfo(title=("Producto Más Vendido", message(f"El producto más vendido es el {producto3}"))
    else:
       messagebox.showinfo(title=("Producto Más Vendido", message(f"El producto más vendido es el {producto4}"))
  
def productoMenosVendido():
    global prodLapiz
    global prodAspirina
    global prodBorrador
    global prodPan
    textoLapiz = prodLapiz.cget('text')
    textoAspirina=prodAspirina.cget('text')
    textoBorrador=prodBorrador.cget('text')
    textoPan=prodPan.cget('text')
    if venta1<venta2 and venta1<venta3 and venta1<venta4:
        messagebox.showinfo(title=("Producto Menos Vendido", message(f"El producto menos vendido es el {producto1}"))
    elif venta2<venta1 and venta2<venta3 and venta2<venta4:
       messagebox.showinfo(title=("Producto Menos Vendido", message(f"El producto menos vendido es el {producto2}"))
    elif venta3<venta1 and venta3<venta2 and venta3<venta4:
       messagebox.showinfo(title=("Producto Menos Vendido", message(f"El producto menos vendido es el {producto3}"))
    else:
       messagebox.showinfo(title=("Producto Menos Vendido", message(f"El producto menos vendido es el {producto4}"))

def promedioVentas():
    global venta1
    global venta2
    global venta3
    global venta4
    sum= venta1 + venta2 + venta3 + venta4
    prom = sum/4
    messagebox.showinfo(title=("El promedio de ventas es ", prom))
                        
def dineroEnCaja():
    global venta1
    global venta2
    global venta3
    global venta4
    sum = venta1 + venta2 + venta3 + venta4
    messagebox.showinfo(message=("El monto que hay en caja es de ", sum)

lblProducto1 = Label(window, text=" Lapíz ", font=("Arial Black", 10), fg="red", bg="white")
lblProducto1.place(x=105, y=10)
lblTipo = Label(window, text=" Tipo ", font=("Arial Black", 10), fg="black", bg="white")
lblTipo.place(x=10, y=50)
lblMercaderiaEnBodega = Label(window, text=" Mercaderia en Bodega ", font=("Arial Black", 10), fg="black", bg="white")
lblMercaderiaEnBodega.place(x=10, y=75)
lblPrecioPorUnidad = Label(window, text=" Precio por Unidad ", font=("Arial Black", 10), fg="black", bg="white")
lblPrecioPorUnidad.place(x=10, y=100)
lblMercaderiaVendida = Label(window, text=" Mercaderia Vendida ", font=("Arial Black", 10), fg="black", bg="white")
lblMercaderiaVendida.place(x=10, y=125)
lblCantidadMinima = Label(window, text=" Cantidad Minima ", font=("Arial Black", 10), fg="black", bg="white")
lblCantidadMinima.place(x=10, y=150)

txtProducto1= Entry(window,width=15)
txtProducto1.place(x=190, y=50)
txtMercaderia_en_Bodega= Entry(window,width=15)
txtMercaderia_en_Bodega.place(x=190, y=75)
txtPrecio_por_Unidad= Entry(window,width=15)
txtPrecio_por_Unidad.place(x=190, y=100)
txtMercaderiaVendida= Entry(window,width=15)
txtMercaderiaVendida.place(x=190, y=125)
txtCantidadMínima= Entry(window, width=15)
txtCantidadMínima.place(x=190, y=150)

lblProducto2 = Label(window, text=" Aspirína ", font=("Arial Black", 10), fg="red", bg="white")
lblProducto2.place(x=620, y=10)
lblTipo = Label(window, text=" Tipo ", font=("Arial Black", 10), fg="blue", bg="white")
lblTipo.place(x=535, y=50)
lblMercaderiaEnBodega = Label(window, text=" Mercaderia en Bodega ", font=("Arial Black", 10), fg="blue", bg="white")
lblMercaderiaEnBodega.place(x=535, y=75)
lblPrecioPorUnidad = Label(window, text=" Precio por Unidad ", font=("Arial Black", 10), fg="blue", bg="white")
lblPrecioPorUnidad.place(x=535, y=100)
lblPrecioPorMayor = Label(window, text=" Precio por Mayor ", font=("Arial Black", 10), fg="blue", bg="white")
lblPrecioPorMayor.place(x=535, y=125)
lblMercaderiaVendida = Label(window, text=" Mercaderia Vendida ", font=("Arial Black", 10), fg="blue", bg="white")
lblMercaderiaVendida.place(x=535, y=125)
lblCantidadMínima = Label(window, text=" Cantidad Minima ", font=("Arial Black", 10), fg="blue", bg="white")
lblCantidadMínima.place(x=535, y=150)

txtProducto= Entry(window,width=15)
txtProducto.place(x=720, y=50)
txtMercaderia_en_Bodega= Entry(window,width=15)
txtMercaderia_en_Bodega.place(x=720, y=75)
txtPrecio_por_Unidad= Entry(window,width=15)
txtPrecio_por_Unidad.place(x=720, y=100)
txtMercaderiaVendida= Entry(window,width=15)
txtMercaderiaVendida.place(x=720, y=125)
txtCantidadMínima= Entry(window, width=15)
txtCantidadMínima.place(x=720, y=150)

lblProducto3 = Label(window, text=" Borrador ", font=("Arial Black", 10), fg="red", bg="white")
lblProducto3.place(x=105, y=300)
lblTipo = Label(window, text=" Tipo ", font=("Arial Black", 10), fg="orange", bg="white")
lblTipo.place(x=10, y=325)
lblMercaderiaEnBodega = Label(window, text=" Mercaderia en Bodega ", font=("Arial Black", 10), fg="orange", bg="white")
lblMercaderiaEnBodega.place(x=10, y=350)
lblPrecioPorUnidad = Label(window, text=" Precio por Unidad ", font=("Arial Black", 10), fg="orange", bg="white")
lblPrecioPorUnidad.place(x=10, y=375)
lblMercaderiaVendida = Label(window, text=" Mercaderia Vendida ", font=("Arial Black", 10), fg="orange", bg="white")
lblMercaderiaVendida.place(x=10, y=400)
lblCantidadMinima = Label(window, text=" Cantidad Minima ", font=("Arial Black", 10), fg="orange", bg="white")
lblCantidadMinima.place(x=10, y=425)

txtProducto= Entry(window,width=15)
txtProducto.place(x=190, y=325)
txtMercaderia_en_Bodega= Entry(window,width=15)
txtMercaderia_en_Bodega.place(x=190, y=350)
txtPrecio_por_Unidad= Entry(window,width=15)
txtPrecio_por_Unidad.place(x=190, y=375)
txtMercaderiaVendida= Entry(window,width=15)
txtMercaderiaVendida.place(x=190, y=400)
txtCantidadMínima= Entry(window, width=15)
txtCantidadMínima.place(x=190, y=425)

lblProducto4 = Label(window, text=" Pan ", font=("Arial Black", 10), fg="red", bg="white")
lblProducto4.place(x=620, y=300)
lblTipo = Label(window, text=" Tipo ", font=("Arial Black", 10), fg="green", bg="white")
lblTipo.place(x=535, y=325)
lblMercaderiaEnBodega = Label(window, text=" Mercaderia en Bodega ", font=("Arial Black", 10), fg="green", bg="white")
lblMercaderiaEnBodega.place(x=535, y=350)
lblPrecioPorUnidad = Label(window, text=" Precio por Unidad ", font=("Arial Black", 10), fg="green", bg="white")
lblPrecioPorUnidad.place(x=535, y=375)
lblMercaderiaVendida = Label(window, text=" Mercaderia Vendida ", font=("Arial Black", 10), fg="green", bg="white")
lblMercaderiaVendida.place(x=535, y=400)
lblCantidadMinima = Label(window, text=" Cantidad Minima ", font=("Arial Black", 10), fg="green", bg="white")
lblCantidadMinima.place(x=535, y=425)

txtProducto= Entry(window,width=15)
txtProducto.place(x=720, y=325)
txtMercaderia_en_Bodega= Entry(window,width=15)
txtMercaderia_en_Bodega.place(x=720, y=350)
txtPrecio_por_Unidad= Entry(window,width=15)
txtPrecio_por_Unidad.place(x=720, y=375)
txtMercaderiaVendida= Entry(window,width=15)
txtMercaderiaVendida.place(x=720, y=400)
txtCantidadMínima= Entry(window, width=15)
txtCantidadMínima.place(x=720, y=425)


btn= Button(window, text=" Abastecimiento ", command=abastecimiento1)
btn.place(x=5, y=240)
btn= Button(window, text=" Vender Mercadería ", command=venta1)
btn.place(x=110, y=240)
btn= Button(window, text=" Cambiar Producto ", command=cambiarProducto1)
btn.place(x=230, y=240)

btn= Button(window, text=" Abastecimiento ", command=abastecimiento2)
btn.place(x=535, y=240)
btn= Button(window, text=" Vender Mercadería ", command=venta2)
btn.place(x=640, y=240)
btn= Button(window, text=" Cambiar Producto ", command=cambiarProducto2)
btn.place(x=760, y=240)

btn= Button(window, text=" Abastecimiento ", command=abastecimiento3)
btn.place(x=5, y=520)
btn= Button(window, text=" Vender Mercadería ", command=venta3)
btn.place(x=110, y=520)
btn= Button(window, text=" Cambiar Producto ", command=cambiarProducto3)
btn.place(x=230, y=520)

btn= Button(window, text=" Abastecimiento ", command=abastecimiento4)
btn.place(x=535, y=520)
btn= Button(window, text=" Vender Mercadería ", command=venta4)
btn.place(x=640, y=520)
btn= Button(window, text=" Cambiar Producto ", command=cambiarProducto4)
btn.place(x=760, y=520)

lblNumero= Label(window, text="OPCIONES", font=("Arial Black", 10), fg="red", bg="white")
lblNumero.place(x=400, y=565)

btn= Button(window, text=" Productos Más Vendidos ", command=productoMásVendidos)
btn.place(x=20, y=600)
btn= Button(window, text=" Productos Menos Vendidos ", command=productoMenosVendido)
btn.place(x=200, y=600)
btn= Button(window, text=" Promedio Ventas ", command=promedioVentas)
btn.place(x=360, y=600)
btn= Button(window, text=" Dinero En Caja ", command=dineroEnCaja)
btn.place(x=540, y=600)

window.mainloop()
