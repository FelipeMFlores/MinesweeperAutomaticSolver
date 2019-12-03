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
    x = gs_minefield.size
    print ( x[0] )
    print ( x[1] ) 


    # encontra borda do campo (pixel mais escuro)
    xy = ( 1, 1 )

    # pula a barra do menu
    curr_pixel = gs_minefield.getpixel( xy )
    prev_pixel = gs_minefield.getpixel( ( xy[0], xy[1] ) )
    while curr_pixel <= prev_pixel:
        xy = ( xy[0], xy[1]+1 )
        prev_pixel = curr_pixel
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
    
    first_cell_coordinates = ( xy[0]-1, xy[1] ) 

    xy = top_right_corner
    curr_pixel = gs_minefield.getpixel( xy )
    prev_pixel = gs_minefield.getpixel( ( xy[0]+1, xy[1]-1 ) )
    while curr_pixel <= prev_pixel:
        xy = ( xy[0]-1, xy[1]+1 )
        prev_pixel = curr_pixel
        curr_pixel = gs_minefield.getpixel( xy )
            
    last_cell_coordinates = ( xy[0]+2, xy[1] ) 

    xy = first_cell_coordinates
    # encontra o tamanho da celula (pixel mais escuro)
    pixel_right = gs_minefield.getpixel( ( xy[0]+1, xy[1] ) )
    cell_width = 0
    while pixel_right >= curr_pixel:        
        cell_width += 1
        curr_pixel = pixel_right
        xy = ( xy[0]+1, xy[1] )
        pixel_right = gs_minefield.getpixel( ( xy[0]+1, xy[1] ) )
    
    cell_width += 2
    print ( cell_width )

    field_width = last_cell_coordinates[0] - first_cell_coordinates[0]
    field_cell_width = math.floor( field_width / cell_width )

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

    curr_pixel = gs_minefield.getpixel( xy )
    prev_pixel = gs_minefield.getpixel( ( xy[0]-1, xy[1]+1 ) )
    while curr_pixel <= prev_pixel:
        xy = ( xy[0]+1, xy[1]-1 )
        prev_pixel = curr_pixel
        curr_pixel = gs_minefield.getpixel( xy )
    bottom_cell_coordinates = xy

    field_height = bottom_cell_coordinates[1] - first_cell_coordinates[1]
    field_cell_height = math.floor( field_height / cell_width ) + 1

    black_pixel = ( 0, 0, 0 )
    seven_pixel = black_pixel
    six_pixel = ( 0, 128, 128 )
    five_pixel = ( 128, 0, 0 )
    four_pixel = ( 0, 0, 128 )
    three_pixel = ( 255, 0, 0 )
    two_pixel = ( 0, 128, 0 )
    one_pixel = ( 0, 0, 255 )

    field_matrix = [[0 for x in range( field_cell_width )] for y in range( field_cell_height )]
    for i in range( 0, field_cell_height ):
        for j in range( 0, field_cell_width ):
            y = i * cell_width
            x = j * cell_width + math.floor( cell_width / 2 )
            xy = ( first_cell_coordinates[0] + x, first_cell_coordinates[1] + y )
            color = 0
            for k in range( 0, cell_width ):
                cell_pixel = minefield.getpixel( xy )
                if color == 3 and cell_pixel == black_pixel:      # bandeira
                    color = -1
                elif cell_pixel == seven_pixel:
                    color = 7
                elif cell_pixel == six_pixel:
                    color = 6
                elif cell_pixel == five_pixel:
                    color = 5
                elif cell_pixel == four_pixel:
                    color = 4
                elif cell_pixel == three_pixel:
                    color = 3
                elif cell_pixel == two_pixel:
                    color = 2
                elif cell_pixel == one_pixel:
                    color = 1
                xy = ( xy[0], xy[1] + 1 )
            field_matrix[i][j] = color



if __name__ == "__main__":
    main()
