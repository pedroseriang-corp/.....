import pygame
import time

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Love Of My Life')

black = (0, 0, 0)
green = (0, 255, 0)
font_size = 30
font = pygame.font.SysFont('Arial', font_size)

def display_text(text, delay=50):
    screen.fill(black)
    x, y = 10, 10
    for i in range(len(text) + 1):
        screen.fill(black)
        rendered_text = font.render(text[:i], True, green)
        screen.blit(rendered_text, (x, y))
        pygame.display.flip()
        pygame.time.wait(delay)
    pygame.time.wait(2000)

def main():
    running = True
    for message in [
    "[PESAN AKAN MULAI DALAM 3 DETIK]",
            "[3]...",
            "[2]...",
            "[1]...",
            "Hai, cantik",
            "saya mau ngomong nih sama kamu",
            "jujur, sebenarnya aku itu...",
            "dari dulu udah suka sama kamu",
            "soalnya...",
            "saat pertama kali aku melihatmu",
            "aku merasa, seperti aku telah menemukan...",
            "sesuatu yang berharga,",
            "sesuatu yg selama ini aku cari tanpa aku sadari",
            "dan setiap kali saat aku melihatmu",
            "senyum...",
            "marah...",
            "ketawa...",
            "dan bicara...",
            "hal-hal tersebut selalu membuatku",
            "ketika berada di dekatmu...",
            "aku merasa nyaman dan tau arti kata...",
            "bahagia:)",
            "walaupun perasaan itu hanya sesaat",
            "namun hal itu selalu berhasil...",
            "membuat hariku lebih berwarna",
            "karena tanpamu...",
            "aku merasa seperti...",
            "gambar yang kehilangan warna",
            "maaf jika tiba-tiba aku bilang ini ke kamu...",
            "soalnya aku dah terlanjur suka",
            "karena kamu itu kayak rokok...",
            "bikin candu dan ketagihan..",
            "seolah setiap detik bersamamu adalah...",
            "tarikan nafas yang tak pernah cukup",
            "dah gitu aja...",
            "[PESAN AKAN MATI DALAM 3 DETIK]",
            "[3]...",
            "[2]...",
            "eh... tunggu sebentar!",
            "hampir lupa...",
            "I Love You ",
            "bye cantik...",
            "[1]...",
            ""
    ]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if not running:
            break
        display_text(message)
    
    pygame.quit()

if __name__ == '__main__':
    main()