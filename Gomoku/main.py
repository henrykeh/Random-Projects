import pygame

pygame.init()

screen = pygame.display.set_mode((1800, 1000))
run = True

black_piece = pygame.image.load("Gomoku\Assets\purple_black.png").convert_alpha()
black_piece_scaled = pygame.transform.scale(black_piece, (46, 46))
white_piece = pygame.image.load("Gomoku\Assets\purple_white.png").convert_alpha()
white_piece_scaled = pygame.transform.scale(white_piece, (46, 46))

bg_colour = (245, 195, 142)
board_bg_colour = (199, 133, 48)

board_bg_rect = pygame.Rect((500,100,800,800))

board_pos_coords = []
for i in range(1, 226):
    board_pos_coords.append([ 600 + (i % 15 - 1) * 50, 150 + ((i-1) // 15) * 50])

board_pos_check = [ [] for _ in range(225) ]

board_pos_rects = []
for i in range(len(board_pos_coords)):
    board_pos_rects.append(pygame.Rect(board_pos_coords[i][0] - 23, board_pos_coords[i][1] - 23, 46, 46))

turn = "black"

placed_pieces = []
def place_piece():
    global turn
    for board_pos in board_pos_rects:
        if board_pos.collidepoint(mouse_pos):
            collided_rect_pos = board_pos.topleft #find position of the rect that has been collided with
            collided_board_pos = [collided_rect_pos[0] + 23, collided_rect_pos[1] + 23] #turns the collided rect pos into board pos
            board_pos_coords_index = board_pos_coords.index(collided_board_pos) #finds the index of this board pos
            if len(board_pos_check[board_pos_coords_index]) == 0: #if placeable (list at index is empty)
                board_pos_check[board_pos_coords_index].append(turn)
                placed_pieces.append([turn, (board_pos[0], board_pos[1])])
                if turn == "black":
                    turn = "white"
                else:
                    turn = "black"

def hover(mousepos):
    for board_pos in board_pos_rects:
        if board_pos.collidepoint(mouse_pos):
            if turn == "black":
                screen.blit(black_piece_scaled, board_pos)
            else:
                screen.blit(white_piece_scaled, board_pos)

while run:
    
    screen.fill(bg_colour)
    pygame.draw.rect(screen, (board_bg_colour), board_bg_rect)

    for i in range(1,16):
        #horiztonal line
        pygame.draw.line(screen, "black", (500+50, 100+i*50), (500+850-2*50, 100+i*50))

        #vertical line
        pygame.draw.line(screen, "black", (500+i*50, 100+50), (500+i*50, 100+850-2*50))

    #black circles
    pygame.draw.circle(screen, "black", (900, 500), 6.0) #centre
    pygame.draw.circle(screen, "black", (500+4*50, 100+4*50), 6.0) #top-left
    pygame.draw.circle(screen, "black", (500+12*50, 100+4*50), 6.0) #top-right
    pygame.draw.circle(screen, "black", (500+4*50, 100+12*50), 6.0) #bottom-left
    pygame.draw.circle(screen, "black", (500+12*50, 100+12*50), 6.0) #botttom-right

    for i in placed_pieces:
        if i[0] == "black":
            screen.blit(black_piece_scaled, i[1])
        else:
            screen.blit(white_piece_scaled, i[1])

    mouse_pos = pygame.mouse.get_pos()

    hover(mouse_pos)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            place_piece()
            
        if event.type ==  pygame.QUIT:
            run = False
        
    pygame.display.flip()

pygame.QUIT