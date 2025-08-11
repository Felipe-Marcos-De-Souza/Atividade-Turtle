import turtle # Importa a biblioteca que permite os desenhos
t = turtle.Turtle()

#Esse método conterá as informações da caneta bem como a cor e grossura da linha:
def informacoesCaneta(t, cor, tamanho):
    t.color(cor)
    t.width(tamanho)

informacoesCaneta(t, 'blue', 3)

#Esse método cria um quadrado:
def quadrado():
    t.down()
    for i in range(4):
        t.forward(100)
        t.left(90)
    t.up()

quadrado()
informacoesCaneta(t, 'red', 4)

for i in range(2):
    t.forward(100)
    
#Esse método cria um triângulo equilátero:
def triangulo ():
    t.down()
    for i in range(3):
        t.forward(100)
        t.left(120)
    t.up()

triangulo()
informacoesCaneta(t, 'yellow', 5)

t.right(90)
t.forward(100)

#Esse método cria um Circulo compelto (360 graus):
def circulo():
    t.down()
    t.circle(50, 360)

circulo()
informacoesCaneta(t, 'green', 6)

t. right(90)
t.up()
t.forward(100)
t.down()

#Esse método cria um Hexagono regular:
def hexagono():
    for i in range(6):
        t.forward(50)
        t.left(60)
        
hexagono()

# Manter a janela aberta
turtle.done()



