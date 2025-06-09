import pygame
import sys

from beatc import parse_program

# Inicializa o pygame
pygame.init()

# Configura o mixer para baixa latência
pygame.mixer.init(buffer=512)
"""

- K - Kick Drum
- S - Snare Drum
- H - Hi-Hat (closed)
- O - Hi-Hat (open)
- T - High Tom
- M - Mid Tom
- L - Low Tom (or Floor Tom)
- C - Crash Cymbal
- R - Ride Cymbal
- B - Bell of the Ride Cymbal 
"""

# Mapeamento de LETRAS para arquivos de som
sound_mapping = {
    'K': "kick.wav",        # Bumbo
    'S': "snare.wav",       # Caixa 
    'H': "hihat-closed.wav",  # Hi-Hat fechado
    'O': "hihat-open.wav",    # Hi-Hat aberto
    'T': "tom-h.wav",         # Tom alto
    'M': "tom-m.wav",         # Tom médio
    'L': "tom-l.wav",         # Tom baixo
    'C': "crash.wav",         # Prato de ataque
    'R': "ride.wav",          # Prato de condução
    'B': "rim.wav",           # Bell do prato de condução
    # 'clap.wav',        # Palmas (não definido)
    # 'conga-h.wav',     # Conga alta (não definido)
    # 'conga-l.wav',     # Conga baixa (não definido)
    # 'cowb-h.wav',      # Cowbell alto (não definido)
    # 'cowb-l.wav',      # Cowbell baixo (não definido)
    # 'timbal.wav',      # Timbal (não definido)
    
}

# Carrega os sons
sounds = {key: pygame.mixer.Sound("audio_files/"+file) for key, file in sound_mapping.items()}

# Configura a janela
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Bateria Virtual")

def virtual_drum():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                key_char = chr(event.key).upper()  # Converte a tecla pressionada em um caractere maiúsculo
                
                if key_char in sounds:
                    sounds[key_char].play() 

        # Atualiza a tela (opcional, apenas para manter a janela aberta)
        screen.fill((0, 0, 0))
        pygame.display.flip()

def main():
    # Exemplo de programa de bateria
    # Carrega o arquivo de programa
    with open("sample.rbp", "r") as file:
        program_code = file.read()
    
    # Parseia o programa
    program = parse_program(program_code) 
    patterns= program['patterns']  
    # 1 minuto tem 60 segundos
    # x BPM tem 60/x segundos por batida
    
    beat_time= 60 / (program['BPM'] * program['beats'])  # Tempo de cada batida em segundos
    print(f"beat_time: {beat_time} seconds")

    current_pattern = 'main'
    pattern_stack = []
    current_beat = 0
    
    while True:
        if not current_pattern in patterns:
            print(f"Pattern '{current_pattern}' not found in patterns.")
            break

        if current_beat >= len(patterns[current_pattern]):
            if len(pattern_stack) == 0:
                break 
            
            popped_patern=pattern_stack.pop()
            current_beat = popped_patern['beat'] + 1  # Incrementa o beat para continuar de onde parou
            current_pattern = popped_patern['pattern'] 
            continue
            
        beat = patterns[current_pattern][current_beat]
        print(f"Current Pattern: {current_pattern}, Current Beat: {current_beat}, Beat: {beat}")

        if beat.startswith('@'): 
            # Push the current pattern onto the stack
            pattern_stack.append({
                'pattern': current_pattern,
                'beat': current_beat
            })
            # Switch to the new pattern
            current_pattern = beat[1:]
            current_beat = 0
        else:
            # Toca o som correspondente à batida
            for char in beat.strip():
                if char=='-': continue  # Ignora traços
                if char in sounds:
                    sounds[char].play()
                else:
                    print(f"Sound for '{char}' not found in sound mapping.") 
            pygame.time.delay(int(beat_time * 1000))  # Espera o tempo de cada batida
            current_beat += 1

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): 
                break
                    
        screen.fill((0, 0, 0))
        pygame.display.flip()
    pygame.quit()
    sys.exit() 


if __name__ == "__main__":
    main()