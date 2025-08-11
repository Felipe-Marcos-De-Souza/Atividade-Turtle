import turtle # Importa a biblioteca que permite os desenhos
t = turtle.Turtle()

#Como dito na atividade anterior esse método dá as informações da caneta:
def informacoesCaneta(t, cor, tamanho):
    t.color(cor)
    t.width(tamanho)

informacoesCaneta(t, 'gold', 3)

#Esse método cria uma estrela de 5 pontas:
def Star():
    for i in range(5):
        t.forward(100)
        t.right(144)

Star()

# Manter a janela aberta
turtle.done()

