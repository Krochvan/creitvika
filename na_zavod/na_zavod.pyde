number=0
def setup():
    #создаю условия для картинок
    global img1,img2,korobka,img3,img4,img5
    img1 = loadImage("zavod2.png")
    img4 = loadImage("zavod3.png")
    img2 = loadImage("fon1.png")
    korobka = loadImage("korobka.png")
    img3 = loadImage("fon2.jpg")
    img5 = loadImage("achiv.png")
    size(400,400)
    noStroke()
def draw():
    rectMode(CENTER)
    global number,img1,img2,korobka,img3,img4,img5
    #делаю условия для самой игры
    if number>-1:
        number+=0.0001
        fill("#6C6969")
        image(img2,0,0,400,400)
    image(korobka,0,0,100,100)
    if number <=500:
        rect(random(90,120),random(90,50),random(10,50),random(10,50))
        rect(random(100,150),random(50,20),random(10,50),random(10,50))
        fill('#FFFFFF')
        image(img1,40,100,200,200)
    if number>50:
        number+=0.01
    if number>200:
        number+=0.01
    if number>500:
        number+=0.1
        image(img3,0,0,400,400)
        image(img4,40,100,200,200)
        fill("#6C6969")
        rect(random(105,115),random(130,140),random(5,20),random(10,50))
        rect(random(105,115),random(100,110),random(10,50),random(10,50))
        rect(random(145,170),random(150,160),random(20,60),random(20,60))
        rect(random(145,170),random(120,130),random(20,60),random(20,60))
    if number>3000:
        number+=1
        image(img5,0,0,400,100)
    #текст в игре
    fill("#CB0E0E")
    ellipse(200,200,50,50)
    fill("#FFFFFF")
    textSize(32)
    text(number, 10, 30)
    textSize(15)
    fill("#FFFFFF")
    text("upgrade=50",250,245)
    text("upgrade=200",250,200)
    text("upgrade=500",250,150)
    text("upgrade=3000",250,100)
    textSize(11)
    text(u'работать',175,200)
def mouseClicked():
    #регистрирование нажатия
    mX=mouseX
    mY=mouseY
    global number
    if sqrt((mX-200)*(mX-200)+(mY-200)*(mY-200))<=50:
        fill("#CB0E0E")
        ellipse(200,200,50,50)
        number+=1
    if number>50:
        number+=5
    if number>200:
        number+=15
    if number>500:
        number+=40
    if number>3000:
        number+=500
    fill("#CB0E0E")
    textSize(32)
    text(number, 10, 30)
    fill("#CB0E0E")
    ellipse(200,200,50,50)
    #79 строк кода
