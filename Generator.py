from PIL import Image, ImageDraw, ImageFont
from math import pi

class Generator():

    @classmethod
    def GenerateMinister(self, WIDTH, HEIGHT, FONT_TITLE, FONT_TITLE_SIZE, FONT_SUBTITLE, FONT_SUBTITLE_SIZE, FONT_SPACE, FONT_HEIGHT,LEFT_DISTANCE, BOTTOM_DISTANCE, LINE_THICK, PADDING, PADDING_RIGHT, title, subtitle, exit=""):
        DIM = (WIDTH, HEIGHT)
        WHITE = (255,255,255)

        # Imagem
        print(DIM)
        image = Image.new("RGBA", DIM, (0,0,0,0))
        draw = ImageDraw.Draw(image)

        # Definindo texto, altura e largura da linha
        font_title = ImageFont.truetype(FONT_TITLE, FONT_TITLE_SIZE)
        font_subtitle = ImageFont.truetype(FONT_SUBTITLE, FONT_SUBTITLE_SIZE) 

        text_title_size = draw.textlength(title, font=font_title)
        text_subtitle_size = draw.textlength(subtitle, font=font_subtitle)

        line_height = 2 * LINE_THICK + 2 * PADDING + FONT_HEIGHT
        line_width = 2 * LINE_THICK + 2 * PADDING + max(text_subtitle_size, text_title_size) + PADDING_RIGHT

        # Texto
        tmdim = (
            LEFT_DISTANCE, 
            HEIGHT - BOTTOM_DISTANCE + (line_height-PADDING-LINE_THICK)/2 - FONT_SPACE/2
        )
        tddim = (
            LEFT_DISTANCE, 
            HEIGHT - BOTTOM_DISTANCE + (line_height-PADDING-LINE_THICK)/2 + FONT_SPACE/2
        )

        text_title = draw.text(tmdim, title, fill=WHITE, font=font_title)
        text_subtitle = draw.text(tddim, subtitle, fill=WHITE, font=font_subtitle)


        # Borda esquerda
        dim = (
            LEFT_DISTANCE - line_height/2, 
            HEIGHT - BOTTOM_DISTANCE, 
            LEFT_DISTANCE + line_height/2, 
            HEIGHT - BOTTOM_DISTANCE + line_height
        )
        draw.arc(dim, 90, -90, fill=WHITE, width=LINE_THICK*2)

        # 2 retângulos
        dim = (
            LEFT_DISTANCE , 
            HEIGHT - BOTTOM_DISTANCE, 
            LEFT_DISTANCE + line_width + line_height/2,
            HEIGHT - BOTTOM_DISTANCE + LINE_THICK,
        )
        draw.rectangle(dim, fill=WHITE)

        dim = (
            LEFT_DISTANCE, 
            HEIGHT - BOTTOM_DISTANCE + line_height, 
            LEFT_DISTANCE + line_width + line_height/2,
            HEIGHT - BOTTOM_DISTANCE + LINE_THICK + line_height,
        )
        draw.rectangle(dim, fill=WHITE)

        # Borda direita
        dim = (
            LEFT_DISTANCE + line_width, 
            HEIGHT - BOTTOM_DISTANCE, 
            LEFT_DISTANCE + line_height + line_width, 
            HEIGHT - BOTTOM_DISTANCE + line_height
        )
        draw.arc(dim, -90, 90, fill=WHITE, width=LINE_THICK*2)

        # Fim
        image.save(f"{exit}{title}_{subtitle}.png", "PNG")
    
    @classmethod
    def generateMusic(self, WIDTH, HEIGHT, FONT_TITLE,FONT_TITLE_SIZE,FONT_SUBTITLE,FONT_SUBTITLE_SIZE,FONT_SPACE,FONT_HEIGHT,LEFT_DISTANCE,BOTTOM_DISTANCE,LINE_THICK,PADDING,PADDING_RIGHT, title, subtitle, exit=""):
        DIM = (WIDTH, HEIGHT)
        WHITE = (255,255,255)

        # Imagem
        image = Image.new("RGBA", DIM, (0,0,0,0))
        draw = ImageDraw.Draw(image)

        # Definindo texto, altura e largura da linha
        font_title = ImageFont.truetype(FONT_TITLE, FONT_TITLE_SIZE)
        font_subtitle = ImageFont.truetype(FONT_SUBTITLE, FONT_SUBTITLE_SIZE) 

        text_title_size = draw.textlength(title, font=font_title)
        text_subtitle_size = draw.textlength(subtitle, font=font_subtitle)

        line_height = 2 * LINE_THICK + 2 * PADDING + FONT_HEIGHT
        line_width = 2 * LINE_THICK + 2 * PADDING + max(text_subtitle_size, text_title_size) + PADDING_RIGHT

        title_line_width = PADDING + text_title_size
        subtitle_line_width = PADDING + text_subtitle_size

        # Nota musical
        song = Image.open('music.png')
        dim = (
            LEFT_DISTANCE - int(line_height/2) - 10, 
            HEIGHT - BOTTOM_DISTANCE - int(song.height/2)+10
        )
        image.paste(song, box=dim)

        # Texto
        tmdim = (
            LEFT_DISTANCE + PADDING/2, 
            HEIGHT - BOTTOM_DISTANCE + (line_height-PADDING-LINE_THICK)/2 - FONT_SPACE/2
        )
        tddim = (
            LEFT_DISTANCE + PADDING/2, 
            HEIGHT - BOTTOM_DISTANCE + (line_height-PADDING-LINE_THICK)/2 + FONT_SPACE/2
        )

        text_title = draw.text(tmdim, title, fill=WHITE, font=font_title)
        text_subtitle = draw.text(tddim, subtitle, fill=WHITE, font=font_subtitle)

        # Borda esquerda
        dim = (
            LEFT_DISTANCE - line_height/2, 
            HEIGHT - BOTTOM_DISTANCE, 
            LEFT_DISTANCE + line_height/2, 
            HEIGHT - BOTTOM_DISTANCE + line_height
        )
        draw.arc(dim, 90, -90, fill=WHITE, width=LINE_THICK*2)

        # 2 retângulos
        dim = (
            LEFT_DISTANCE + title_line_width , 
            HEIGHT - BOTTOM_DISTANCE, 
            LEFT_DISTANCE + line_width + line_height/2,
            HEIGHT - BOTTOM_DISTANCE + LINE_THICK,
        )
        draw.rectangle(dim, fill=WHITE)

        dim = (
            LEFT_DISTANCE + subtitle_line_width, 
            HEIGHT - BOTTOM_DISTANCE + line_height, 
            LEFT_DISTANCE + line_width + line_height/2,
            HEIGHT - BOTTOM_DISTANCE + LINE_THICK + line_height,
        )
        draw.rectangle(dim, fill=WHITE)

        # Borda direita
        dim = (
            LEFT_DISTANCE + line_width, 
            HEIGHT - BOTTOM_DISTANCE, 
            LEFT_DISTANCE + line_height + line_width, 
            HEIGHT - BOTTOM_DISTANCE + line_height
        )
        draw.arc(dim, -90, 90, fill=WHITE, width=LINE_THICK*2)

        # Fim
        image.save(f"{exit}{title}_{subtitle}.png", "PNG")