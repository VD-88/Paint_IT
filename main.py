import pygame
import figures
import interface

pygame.init()

FPS = 120

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH = 1024
HEIGHT = 768


main_screen = pygame.display.set_mode((WIDTH, HEIGHT))
main_screen.set_alpha(128)


screen_layer = pygame.Surface((WIDTH, HEIGHT))
screen_layer.set_alpha(1)

interface_layer = pygame.Surface((WIDTH, 50))


pygame.display.set_caption("Paint_IT")
pygame.display.set_icon(pygame.image.load("paint.png"))
clock = pygame.time.Clock()


### Types of possible figures & colors
figure_type = [figures.Brush, figures.Line, figures.Rect, figures.Circle]
fig_id = 0
color = [BLACK, WHITE, RED, GREEN, BLUE]
clr_id = 0
thickness = 5

### text
font = pygame.font.SysFont("arial", 40)
text_thicknes_plus = font.render("+", 1, BLACK)
text_thicknes_minus = font.render("-", 1, BLACK)
text_save = font.render("save", 1, BLACK)
start_drawing = False

### White paper screen
pygame.draw.rect(main_screen, WHITE, (0, 50, WIDTH, HEIGHT - 50))

### interface
pygame.draw.rect(interface_layer, (127, 127, 127), (0, 0, WIDTH, 50))

for k in interface.figures_buttons:
    k.draw(interface_layer)

for l in interface.colors_buttons:
    l.draw(interface_layer)


#interface.Interface.draw_interface(interface_layer)
interface.thickness_button_minus.draw(interface_layer)
interface.thickness_button_plus.draw(interface_layer)
interface.brush_button.pressed(interface_layer)
interface.save_button.draw(interface_layer)
figure = figure_type[fig_id](0, 0, 0, 0, 0, WHITE)
interface.black_color_button.pressed(interface_layer)

brush = pygame.image.load("images\\brush.png").convert_alpha()
rect = pygame.image.load("images\\rect.png").convert_alpha()
line = pygame.image.load("images\\line.png").convert_alpha()
circle = pygame.image.load("images\\circle.png").convert_alpha()

main_screen.blit(interface_layer, (0, 0))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            start_drawing = True
            mouse_position_1 = event.pos
            
            ### figure selection
            if 5 <= mouse_position_1[0] <= 45 and 5 <= mouse_position_1[1] <= 45:
               for k in interface.figures_buttons:
                    k.draw(interface_layer)
               interface.brush_button.pressed(interface_layer)
               fig_id = 0
            if 50 <= mouse_position_1[0] <= 90 and 5 <= mouse_position_1[1] <= 45:
                for k in interface.figures_buttons:
                    k.draw(interface_layer)
                interface.rect_button.pressed(interface_layer)
                fig_id = 2
            if 95 <= mouse_position_1[0] <= 135 and 5 <= mouse_position_1[1] <= 45:
                for k in interface.figures_buttons:
                    k.draw(interface_layer)
                interface.line_button.pressed(interface_layer)
                fig_id = 1
            if 140 <= mouse_position_1[0] <= 180 and 5 <= mouse_position_1[1] <= 45:
                for k in interface.figures_buttons:
                    k.draw(interface_layer)
                interface.circle_button.pressed(interface_layer)
                fig_id = 3
            
            ### colors selection
            if WIDTH - 225 <= mouse_position_1[0] <= WIDTH - 180 and 5 <= mouse_position_1[1] <= 45:
                for l in interface.colors_buttons:
                    l.draw(interface_layer)
                interface.black_color_button.pressed(interface_layer)
                clr_id = 0
            if WIDTH - 180 <= mouse_position_1[0] <= WIDTH - 140 and 5 <= mouse_position_1[1] <= 45:
                for l in interface.colors_buttons:
                    l.draw(interface_layer)
                interface.white_color_button.pressed(interface_layer)
                clr_id = 1
            if WIDTH - 135 <= mouse_position_1[0] <= WIDTH - 95 and 5 <= mouse_position_1[1] <= 45:
                for l in interface.colors_buttons:
                    l.draw(interface_layer)
                interface.red_color_button.pressed(interface_layer)
                clr_id = 2
            if WIDTH - 90 <= mouse_position_1[0] <= WIDTH - 50 and 5 <= mouse_position_1[1] <= 45:
                for l in interface.colors_buttons:
                    l.draw(interface_layer)
                interface.green_color_button.pressed(interface_layer)
                clr_id = 3
            if WIDTH - 45 <= mouse_position_1[0] <= WIDTH - 5 and 5 <= mouse_position_1[1] <= 45:
                for l in interface.colors_buttons:
                    l.draw(interface_layer)
                interface.blue_color_button.pressed(interface_layer)
                clr_id = 4

            ### save button
            if WIDTH / 2 - 40 <= mouse_position_1[0] <= WIDTH / 2 + 40 and 5 <= mouse_position_1[1] <= 45:
                interface.save_button.pressed(interface_layer)
                pygame.image.save(main_screen, "Saves\\temp.jpeg")

            ### thickness buton
            if 185 <= mouse_position_1[0] <= 225 and 5 <= mouse_position_1[1] <= 45:
                interface.thickness_button_minus.pressed(interface_layer)
                if thickness <= 40: thickness += 5
            if 275 <= mouse_position_1[0] <= 315 and 5 <= mouse_position_1[1] <= 45:
                interface.thickness_button_plus.pressed(interface_layer)
                if thickness >= 10: thickness -= 5
        ### drawing
        if event.type == pygame.MOUSEMOTION and start_drawing:
            mouse_position_2 = event.pos
            figure = figure_type[fig_id](mouse_position_1[0], mouse_position_1[1], mouse_position_2[0], mouse_position_2[1], thickness, color[clr_id])     # figure object creation by parameters

            if fig_id > 0:
                pygame.draw.rect(screen_layer, WHITE, (0, 50, WIDTH, HEIGHT - 50))
                figure.draw(screen_layer)
                #print("start drawing on layer")
                
                ### dynamic drawing
                main_screen.blit(screen_layer, (0, 0))
                
                print("visualization of layer")
            else:
                figure.draw(main_screen)
               
        if event.type == pygame.MOUSEBUTTONUP:
            start_drawing = False
            #print("end drawing")
            if fig_id > 0:
                figure.draw(main_screen)
                #print("on the main screen")
            else:
                pass
            interface.save_button.draw(interface_layer)
            interface.thickness_button_minus.draw(interface_layer)
            interface.thickness_button_plus.draw(interface_layer)
    
    ### interface visualization
    interface.thickness_button_value.draw(interface_layer)
    text_thickness_value = font.render(f"{thickness}", 1, BLACK)
    interface_layer.blit(brush, (8, 9))
    interface_layer.blit(rect, (54, 8))
    interface_layer.blit(line, (98, 8))
    interface_layer.blit(circle, (143, 8))
    interface_layer.blit(text_thicknes_plus, (196, 0))
    interface_layer.blit(text_thicknes_minus, (289, 0))
    interface_layer.blit(text_thickness_value, (240, 0)) if thickness == 5 else interface_layer.blit(text_thickness_value, (231, 0))
    interface_layer.blit(text_save, (WIDTH / 2 - 35, 0))

    main_screen.blit(interface_layer, (0, 0))        
    pygame.display.update(0, 0, WIDTH, HEIGHT)
    
    clock.tick(FPS)