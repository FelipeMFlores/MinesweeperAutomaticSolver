# import cv2 as cv
from PIL import Image

def main():
    #mainloop:
        # window to image
        # image to matrix
        # matrix to best play and mine
        # click to flag mines
        # click the play on the game
        # check if end game
    print("lets sweep")

    # converte tela para png
    minefield = Image.open( 'minefield.jpg' )
    minefield.save( 'minefield.png' )

    minefield = Image.open( 'minefield.png' )
    width = minefield.size[0]
    height = minefield.size[1]
    gs_minefield = minefield.convert( "L" )

    # encontra borda do campo
    xy = ( 0, 0 )
    previous_pixel = gs_minefield.getpixel( xy )
    curr_pixel = previous_pixel
    while xy[0] < width and xy[1] < height and curr_pixel >= previous_pixel:
        curr_pixel = gs_minefield.getpixel( xy )
        if curr_pixel >= previous_pixel:
            xy = ( xy[0]+1, xy[1]+1 )
            previous_pixel = curr_pixel
    
    # encontra campo superior esquerdo do campo
    curr_pixel = gs_minefield.getpixel( xy )
    pixel_above = gs_minefield.getpixel( ( xy[0], xy[1]-1 ) )
    while pixel_above <= curr_pixel:
        xy = ( xy[0], xy[1]-1 )
        curr_pixel = gs_minefield.getpixel( xy )
        pixel_above = gs_minefield.getpixel( ( xy[0], xy[1]-1 ) )

    pixel_left = gs_minefield.getpixel( ( xy[0]-1, xy[1] ) )
    while pixel_left <= curr_pixel:
        xy = ( xy[0]-1, xy[1] )
        curr_pixel = gs_minefield.getpixel( xy )
        pixel_left = gs_minefield.getpixel( ( xy[0]-1, xy[1] ) )

    # encontra quantas células o campo tem em largura

    
    # encontra quantas células o campo tem em altura


    # descobre onde ha minas
    mined = [[False for i in range(width)] for j in range(height)]


if __name__ == "__main__":
    main()
