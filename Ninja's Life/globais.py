# -*-coding utf-8-*-
'Definir o tamanho da tela'
WIDTH = 1320
HEIGHT = 1080

'Elementos do personagem'
KUNAI_SPEED = 25 'Velocidade que a kunai do personagem vai ter ao ser lançada'
KUNAI_RELOAD = 30 'Tempo de espera do personagem para atirar uma nova kunai'
POS_X = 0 'Posição inicial do personagem no eixo x(eixo horizontal)'
POS_Y = 0 'Posição inicial do personagem no eixo y(eixo vertical'
CARACTER_JUMP = 110 'Altura máxima do pulo do personagem'
CARACTER_SPEED = 15 'Velocidade que o personagem vai ter ao andar'
CARACTER_WIDTH = 105 'Altura do personagem'
CARACTER_HEIGHT = 130 'Largura do personagem'
CARACTER_LIVE = 3 'Quantidade inicial de vidas do personagem'
ATTACK_RELOAD = 15 'Tempo de espera para realizar um novo ataque básico'
SPECIAL_ATTACK_RELOAD = 45 'Tempo de espera para realizar um novo ataque especial'

'Definir a posição inicial do personagem e que vai indicar qual a posição atual do personagem'
CARACTER_STATUS = 0

'Características gerais do jogo'
GRAVITY = 100 'Gravidade que atua no jogo'
SCORE = 0 'Pontuação do personagem no jogo'
GAME_STATE = 0 'Qual plano de fundo deve aparecer no jogo'
SCROLL_SPEED = 300 'Velocidade com que o fundo passa a se mover quando o personagem atinge um ponto na tela'

'Características dos inimigos'
NINJA_ENEMY_LV1_SPEED = -10 'Velocidade do ninja inimigo do level 1, como ele vai começar indo em direção ao personagem deve estar com uma velocidade com sinal contraria ao personagem'
NINJA_ENEMY_LV1_WIDTH = 105 'Altura do ninja inimigo do level 1'
NINJA_ENEMY_LV1_HEIGHT = 130 'Largura do ninja inimigo do level 1'
NINJA_ENEMY_LV1_POS_X = 0 'Posição inicial do ninja inimigo do level 1 no eixo horizontal'
NINJA_ENEMY_LV1_POS_Y = 0 'Posição inicial do ninja inimigo do level 1 no eixo vertical'
NINJA_ENEMY_LV1_ATTACK_RELOAD = 20 'Recarga do ataque do ninja inimigo do level 1'

'Elementos do solo'
GROUND_HEIGHT = 0 'Altura do solo'
GROUND_STATE = 0 'Qual o solo que deve aparecer no jogo'

'Elementos do fundo'
BACKGROUND_IMAGE = 0
