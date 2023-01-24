import turtle
kilpikonna = turtle.Turtle()
kilpikonna.shape("turtle")

print("Mihin suuntaan haluat siirtää kilpikonnaa?")
print("Kirjoita oikea, vasen, alas tai ylös")

suunta = input()
 
if suunta == "oikea":
  kilpikonna.forward(50)

if suunta == "vasen":
  kilpikonna.left(180)
  kilpikonna.forward(50)

if suunta == "ylös":
  kilpikonna.left(90)
  kilpikonna.forward(50)
  
if suunta == "alas":
  kilpikonna.right(90)
  kilpikonna.forward(50)