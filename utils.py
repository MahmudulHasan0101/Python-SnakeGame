import pygame 

class Text:
    def __init__(self, text, font_size, color, x = 0, y = 0):
        self.text = text
        self.font_size = font_size
        self.color = color
        self.font = pygame.font.Font(None, font_size)
        self.surface = self.font.render(self.text, True, self.color)
        self.rect = self.surface.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.surface, self.rect)

    def setRect(self, rect):
        self.rect = rect

    def updateText(self, text):
        self.surface = self.font.render(text, True, self.color)


class Button:
    def __init__(self, x, y, width, height, inactive_color, active_color, text = Text):
        self.rect = pygame.Rect(x - width // 2, y - height // 2, width, height)
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.color = inactive_color
        self.text_obj = text

        text.setRect(text.surface.get_rect(center=self.rect.center))

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        self.text_obj.draw(screen)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.color = self.active_color
            else:
                self.color = self.inactive_color

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
            
        return False
    


class ScrollSwitch:
    def __init__(self, x, y, width, height, min_val = 1, max_val = 20,
                switch_color = pygame.Color('black'), switch_active_color = pygame.Color('blue'),
                scroll_color = pygame.Color('white'), scroll_active_color = pygame.Color('white')
                ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.switch_color = switch_color
        self.switch_active_color = switch_active_color
        self.switch_is_active = False

        self.scroll_minval = min_val
        self.scroll_maxval = max_val
        self.scroll_width = 15
        self.scroll_height = height
        self.scroll_x = x
        self.scroll_y = y
        self.scroll_color = scroll_color
        self.scroll_active_color = scroll_active_color
        self.scroll_is_dragged = False

        self.value = 0

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.scroll_x <= event.pos[0] <= self.scroll_x + self.scroll_width and self.scroll_y <= event.pos[1] <= self.scroll_y + self.scroll_height:
                    self.scroll_is_dragged = True

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.scroll_is_dragged = False
                
        elif event.type == pygame.MOUSEMOTION:
            if self.scroll_is_dragged:
                self.scroll_x = max(self.x, min(event.pos[0] - self.scroll_width / 2, self.x + self.width - self.scroll_width))
                self.value = int((self.scroll_x - self.x) / (self.width - self.scroll_width) * 100)
        
        return self.scroll_is_dragged
    
    def get_scroll_val(self):
        return int((self.value / self.width) * self.scroll_maxval + self.scroll_minval)

    def update(self):
        self.switch_color = self.switch_active_color if self.switch_is_active else self.switch_color
        self.scroll_color = self.scroll_active_color if self.scroll_is_dragged else self.scroll_color

    def draw(self, screen):
        pygame.draw.rect(screen, self.switch_color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, self.scroll_color, (self.scroll_x, self.scroll_y, self.scroll_width, self.scroll_height))
 

