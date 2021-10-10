from PIL import Image, ImageColor

# CONST
r0 = 0  # offsetX
r1 = 0  # offsetY
r2 = 0  # x0
r3 = 0  # y0
r4 = 0  # x1
r5 = 0  # y1
r6 = 0
# VAR
r7 = 0
r9 = 0
r10 = 0


def absolute(x):
    if x > 0:
        return x
    else:
        return -x


def drawCircle(xc, yc, x, y):
    # result.append((xc+x, yc+y))
    # result.append((xc-x, yc+y))
    # result.append((xc+x, yc-y))
    # result.append((xc-x, yc-y))
    # result.append((xc+y, yc+x))
    # result.append((xc-y, yc+x))
    # result.append((xc+y, yc-x))
    # result.append((xc-y, yc-x))
    coords = xc + x
    coords = coords + offsetX
    tmp = yc + y
    tmp = tmp + offsetY
    tmp = tmp << 8
    coords = coords + tmp
    memmory[coords] = 1

    coords = xc - x
    coords = coords + offsetX
    tmp = yc + y
    tmp = tmp + offsetY
    tmp = tmp << 8
    coords = coords + tmp
    memmory[coords] = 1

    coords = xc + x
    coords = coords + offsetX
    tmp = yc - y
    tmp = tmp + offsetY
    tmp = tmp << 8
    coords = coords + tmp
    memmory[coords] = 1

    coords = xc - x
    coords = coords + offsetX
    tmp = yc - y
    tmp = tmp + offsetY
    tmp = tmp << 8
    coords = coords + tmp
    memmory[coords] = 1

    coords = xc+y
    coords = coords + offsetX
    tmp = yc+x
    tmp = tmp + offsetY
    tmp = tmp << 8
    coords = coords + tmp
    memmory[coords] = 1

    coords = xc-y
    coords = coords + offsetX
    tmp = yc+x
    tmp = tmp + offsetY
    tmp = tmp << 8
    coords = coords + tmp
    memmory[coords] = 1

    coords = xc+y
    coords = coords + offsetX
    tmp = yc-x
    tmp = tmp + offsetY
    tmp = tmp << 8
    coords = coords + tmp
    memmory[coords] = 1

    coords = xc-y
    coords = coords + offsetX
    tmp = yc-x
    tmp = tmp + offsetY
    tmp = tmp << 8
    coords = coords + tmp
    memmory[coords] = 1


def circleBres(xc, yc, r):
    x = 0
    y = r
    tmp = r << 1
    d = 3 - tmp
    drawCircle(xc, yc, x, y)
    while y >= x:
        x = x + 1

        if (d > 0):
            y = y - 1
            d = d + 10
            tmp = x - y
            tmp = tmp << 2
            d = d + tmp
        else:
            d = d + 6
            tmp = x << 2
            d = d + tmp
        drawCircle(xc, yc, x, y)


def plotLine(x0, y0, x1, y1):
    eval = x1-x0
    eval = absolute(eval)
    tmp = y1-y0
    tmp = absolute(tmp)
    if eval > tmp:
        eval = 1
    else:
        eval = 0
    if not eval:
        tmp = x0
        x0 = y0
        y0 = tmp
        tmp = x1
        x1 = y1
        y1 = tmp

    dx = x1 - x0
    dy = y1 - y0
    yi = 1
    if dy < 0:
        yi = -1
        dy = -dy
    dif = dy - dx
    D = dy + dif
    y = y0

    for x in range(x0, x1+1):
        if eval:
            coords = x + offsetX
            tmp = y + offsetY
            tmp = tmp << 8
            coords = coords + tmp
        else:
            coords = y + offsetX
            tmp = x + offsetY
            tmp = tmp << 8
            coords = coords + tmp
        memmory[coords] = 1
        if D > 0:
            y = y + yi
            D = D + dif
            D = D + dif
        else:
            D = D + dy
            D = D + dy


def draw(char):
    if (char == 'A'):
        plotLine(0, 0, 4, 0)
        plotLine(0, 3, 4, 3)
        plotLine(0, 0, 0, 4)
        plotLine(4, 0, 4, 4)
    elif (char == 'B'):
        plotLine(0, 0, 3, 0)  # -
        plotLine(0, 2, 4, 2)  # -
        plotLine(0, 4, 4, 4)  # -
        plotLine(0, 0, 0, 4)  # |
        plotLine(3, 0, 3, 2)  # |
        plotLine(4, 2, 4, 4)  # |
    elif (char == 'C'):
        plotLine(0, 0, 4, 0)  # -
        plotLine(0, 4, 4, 4)  # -
        plotLine(0, 0, 0, 4)  # |
    elif (char == 'D'):
        plotLine(0, 0, 0, 4)  # |
        plotLine(4, 1, 4, 3)  # |
        plotLine(0, 0, 4, 1)  # -
        plotLine(0, 4, 4, 3)  # -
    elif (char == 'E'):
        plotLine(0, 0, 4, 0)  # -
        plotLine(0, 2, 4, 2)  # -
        plotLine(0, 4, 4, 4)  # -
        plotLine(0, 0, 0, 4)  # |
    elif (char == 'F'):
        plotLine(0, 0, 4, 0)  # -
        plotLine(0, 2, 4, 2)  # -
        plotLine(0, 0, 0, 4)  # |
    elif (char == 'G'):
        plotLine(0, 0, 4, 0)  # -
        plotLine(2, 2, 4, 2)  # -
        plotLine(0, 4, 4, 4)  # -
        plotLine(0, 0, 0, 4)  # |
        plotLine(4, 2, 4, 4)  # |
    elif (char == 'H'):
        plotLine(0, 2, 4, 2)  # -
        plotLine(0, 0, 0, 4)  # |
        plotLine(4, 0, 4, 4)  # |
    elif (char == 'I'):
        plotLine(0, 0, 4, 0)  # -
        plotLine(0, 4, 4, 4)  # -
        plotLine(2, 0, 2, 4)  # |
    elif (char == 'M'):
        plotLine(0, 0, 0, 4)  # |
        plotLine(4, 0, 4, 4)  # |
        plotLine(0, 0, 2, 3)  # |
        plotLine(4, 0, 2, 3)  # |
    elif (char == 'N'):
        plotLine(0, 0, 0, 4)  # |
        plotLine(4, 0, 4, 4)  # |
        plotLine(0, 0, 4, 4)  # |
    elif (char == 'S'):
        plotLine(0, 0, 0, 2)  # |
        plotLine(4, 2, 4, 4)  # |
        plotLine(0, 0, 4, 0)  # -
        plotLine(0, 4, 4, 4)  # -
        plotLine(0, 2, 4, 2)  # -
    elif (char == 'T'):
        plotLine(0, 0, 4, 0)  # -
        plotLine(2, 0, 2, 4)  # |
    elif (char == 'U'):
        plotLine(0, 0, 0, 4)  # |
        plotLine(4, 0, 4, 4)  # |
        plotLine(0, 4, 4, 4)  # -
    elif (char == 'O'):
        plotLine(0, 0, 0, 4)  # |
        plotLine(4, 0, 4, 4)  # |
        plotLine(0, 4, 4, 4)  # -
        plotLine(0, 0, 4, 0)  # -
    elif (char == '1'):
        circleBres(5, 5, 5)  # O
        plotLine(0, 0, 10, 10)  # |
        plotLine(10, 0, 10, 10)  # |
        plotLine(5, 0, 5, 10)  # |
        plotLine(0, 0, 0, 10)  # |
        plotLine(0, 5, 10, 5)  # |


X_DIM = 2**8
Y_DIM = 2**8
SIZE = 6

memmory = {x: 0 for x in range(X_DIM*Y_DIM)}

file = open("test.txt")

text = file.read()

offsetX = 0
offsetY = 0
for c in text:
    coords = draw(c)
    offsetX = offsetX + SIZE
    tmp = offsetX + SIZE
    if tmp > X_DIM:
        offsetX = 0
        offsetY = offsetY + SIZE


# _________________________________/ALTO NIVEL/_________________________________
im = Image.new('1', (X_DIM, Y_DIM))
for posY in range(Y_DIM):
    for posX in range(X_DIM):
        if (memmory[posX+posY*X_DIM]):
            color = ImageColor.getcolor('white', '1')
        else:
            color = ImageColor.getcolor('black', '1')
        im.putpixel((posX, posY), color)

im.save('out.png')
