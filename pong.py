import pygame
import sys

pygame.init()

# ===================== CONFIGURAÇÕES =====================
class Config:
    """Classe responsável por armazenar configurações globais do jogo."""
    LARGURA = 800
    ALTURA = 600
    COR_FUNDO = (0, 0, 0)
    COR_OBJETOS = (255, 255, 255)
    FPS = 60


# ===================== ENTIDADES =====================
class Raquete:
    """Representa uma raquete (jogador ou IA)."""

    def __init__(self, x, y, largura=10, altura=60, velocidade=5):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.velocidade = velocidade

    def mover_cima(self):
        """Move a raquete para cima."""
        if self.rect.top > 0:
            self.rect.y -= self.velocidade

    def mover_baixo(self):
        """Move a raquete para baixo."""
        if self.rect.bottom < Config.ALTURA:
            self.rect.y += self.velocidade

    def desenhar(self, tela):
        """Desenha a raquete na tela."""
        pygame.draw.rect(tela, Config.COR_OBJETOS, self.rect)


class Bola:
    """Representa a bola do jogo."""

    def __init__(self):
        self.rect = pygame.Rect(
            Config.LARGURA // 2,
            Config.ALTURA // 2,
            7,
            7
        )
        self.vel_x = 5
        self.vel_y = 5

    def mover(self):
        """Atualiza a posição da bola."""
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def inverter_x(self):
        """Inverte direção horizontal."""
        self.vel_x *= -1

    def inverter_y(self):
        """Inverte direção vertical."""
        self.vel_y *= -1

    def resetar(self):
        """Reposiciona a bola no centro."""
        self.rect.center = (Config.LARGURA // 2, Config.ALTURA // 2)
        self.inverter_x()

    def desenhar(self, tela):
        """Desenha a bola."""
        pygame.draw.circle(tela, Config.COR_OBJETOS, self.rect.center, self.rect.width)


# ===================== LÓGICA DO JOGO =====================
class Game:
    """Controla toda a lógica do jogo."""

    def __init__(self, tela):
        self.tela = tela
        self.clock = pygame.time.Clock()
        self.reset()

    def reset(self):
        """Inicializa ou reinicia o jogo."""
        self.player1 = Raquete(15, Config.ALTURA // 2 - 30)
        self.player2 = Raquete(Config.LARGURA - 25, Config.ALTURA // 2 - 30)
        self.bola = Bola()
        self.score1 = 0
        self.score2 = 0

    def tratar_eventos(self):
        """Captura eventos do sistema."""
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def entrada_usuario(self):
        """Captura input do jogador."""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.player1.mover_cima()
        if keys[pygame.K_DOWN]:
            self.player1.mover_baixo()

    def mover_ia(self):
        """Controla a IA do jogador 2."""
        if self.player2.rect.centery < self.bola.rect.centery:
            self.player2.mover_baixo()
        else:
            self.player2.mover_cima()

    def verificar_colisoes(self):
        """Gerencia colisões da bola."""
        if self.bola.rect.colliderect(self.player1.rect) or \
           self.bola.rect.colliderect(self.player2.rect):
            self.bola.inverter_x()

        if self.bola.rect.top <= 0 or self.bola.rect.bottom >= Config.ALTURA:
            self.bola.inverter_y()

    def verificar_pontos(self):
        """Atualiza pontuação."""
        if self.bola.rect.left <= 0:
            self.score2 += 1
            self.bola.resetar()

        if self.bola.rect.right >= Config.LARGURA:
            self.score1 += 1
            self.bola.resetar()

        if self.score1 >= 1 or self.score2 >= 1:
            return True  # volta para o menu

        return False

    def atualizar(self):
        """Atualiza o estado do jogo."""
        self.bola.mover()
        self.verificar_colisoes()
        self.mover_ia()
        return self.verificar_pontos()

    def desenhar(self):
        """Renderiza todos os elementos."""
        self.tela.fill(Config.COR_FUNDO)

        self.player1.desenhar(self.tela)
        self.player2.desenhar(self.tela)
        self.bola.desenhar(self.tela)

        font = pygame.font.SysFont(None, 36)
        texto = font.render(f"{self.score1} - {self.score2}", True, Config.COR_OBJETOS)
        self.tela.blit(texto, texto.get_rect(center=(Config.LARGURA // 2, 30)))

        pygame.display.flip()

    def rodar(self):
        """Loop principal do jogo."""
        while True:
            self.tratar_eventos()
            self.entrada_usuario()

            if self.atualizar():
                return

            self.desenhar()
            self.clock.tick(Config.FPS)


# ===================== MENU =====================
class Menu:
    """Responsável pela tela inicial."""

    def __init__(self, tela):
        self.tela = tela

    def mostrar(self):
        """Exibe o menu até o jogador iniciar."""
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                    return

            self.tela.fill(Config.COR_FUNDO)

            font = pygame.font.SysFont(None, 50)
            titulo = font.render("Pong", True, Config.COR_OBJETOS)
            self.tela.blit(titulo, titulo.get_rect(center=(Config.LARGURA // 2, 150)))

            font2 = pygame.font.SysFont(None, 26)
            texto = font2.render("Pressione ESPAÇO para jogar", True, Config.COR_OBJETOS)
            self.tela.blit(texto, texto.get_rect(center=(Config.LARGURA // 2, 350)))

            pygame.display.flip()


# ===================== MAIN =====================
def main():
    """Função principal do sistema."""
    tela = pygame.display.set_mode((Config.LARGURA, Config.ALTURA))
    pygame.display.set_caption("Pong")

    menu = Menu(tela)
    game = Game(tela)

    while True:
        menu.mostrar()
        game.reset()
        game.rodar()


if __name__ == "__main__":
    main()