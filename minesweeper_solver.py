# import cv2 as cv
from PIL import Image
import subprocess
import math

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
    subprocess.call(["xwd", "-out", "minefield.xwd", "-name", "Mines"])
    subprocess.call(["convert", "minefield.xwd", "minefield.png"])

    minefield = Image.open( 'minefield.png' )
    width = minefield.size[0]
    height = minefield.size[1]
    gs_minefield = minefield.convert( "L" )

    # encontra borda do campo (pixel mais escuro)
    xy = ( 1, 1 )
    curr_pixel = gs_minefield.getpixel( xy )
    prev_pixel = gs_minefield.getpixel( ( xy[0]-1, xy[1]-1 ) )
    while xy[0] < width and xy[1] < height and curr_pixel >= prev_pixel:
        xy = ( xy[0]+1, xy[1]+1 )
        prev_pixel = curr_pixel
        curr_pixel = gs_minefield.getpixel( xy )
    
    # encontra canto superior esquerdo do campo (pixel mais claro)
    pixel_above = gs_minefield.getpixel( ( xy[0], xy[1]-1 ) )
    while pixel_above <= curr_pixel:
        curr_pixel = pixel_above
        xy = ( xy[0], xy[1]-1 )
        pixel_above = gs_minefield.getpixel( ( xy[0], xy[1]-1 ) )

    pixel_left = gs_minefield.getpixel( ( xy[0]-1, xy[1] ) )
    while pixel_left <= curr_pixel:
        curr_pixel = pixel_left
        xy = ( xy[0]-1, xy[1] )
        pixel_left = gs_minefield.getpixel( ( xy[0]-1, xy[1] ) )

    top_left_corner = xy

    # encontra canto superior direito
    pixel_right = gs_minefield.getpixel( ( xy[0]+1, xy[1] ) )
    while pixel_right <= curr_pixel:
        curr_pixel = pixel_right
        xy = ( xy[0]+1, xy[1] )
        pixel_right = gs_minefield.getpixel( ( xy[0]+1, xy[1] ) )

    top_right_corner = xy
    xy = top_left_corner

    # estima a largura do campo em celulas
    curr_pixel = gs_minefield.getpixel( xy )
    prev_pixel = gs_minefield.getpixel( ( xy[0]-1, xy[1]-1 ) ) 
    while curr_pixel <= prev_pixel:     # encontra a primeira celula (pixel mais claro)
        xy = ( xy[0]+1, xy[1]+1 )
        prev_pixel = curr_pixel
        curr_pixel = gs_minefield.getpixel( xy )
            
    first_cell_coordinates = xy

    # encontra o tamanho da celula (pixel mais escuro)
    pixel_right = gs_minefield.getpixel( ( xy[0]+1, xy[1] ) )
    cell_width = 0
    while pixel_right >= curr_pixel:        
        cell_width += 1
        curr_pixel = pixel_right
        xy = ( xy[0]+1, xy[1] )
        pixel_right = gs_minefield.getpixel( ( xy[0]+1, xy[1] ) )

    # encontra o tamanho do espaço entre cada célula (pixel mais claro)
    spacing = 0
    while pixel_right <= curr_pixel:
        spacing += 1
        curr_pixel = pixel_right
        xy = ( xy[0]+1, xy[1] )
        pixel_right = gs_minefield.getpixel( ( xy[0]+1, xy[1] ) )

    field_width = top_right_corner[0] - top_left_corner[0]
    field_cell_width = math.floor( field_width / ( cell_width + spacing ) )

    # estima a altura do campo em celulas
    xy = top_left_corner

    # encontra canto inferior esquedo
    curr_pixel = gs_minefield.getpixel( xy )
    pixel_below = gs_minefield.getpixel( ( xy[0], xy[1]+1 ) )
    while pixel_below <= curr_pixel:
        curr_pixel = pixel_below
        xy = ( xy[0], xy[1]+1 )
        pixel_below = gs_minefield.getpixel( ( xy[0], xy[1]+1 ) )

    bottom_left_corner = xy

    field_height = bottom_left_corner[1] - top_left_corner[1]
    field_cell_height = math.floor( field_height / ( cell_width + spacing ) )


if __name__ == "__main__":
    main()
