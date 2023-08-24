import cv2 

cap = cv2.VideoCapture("imagens\Video Vacas.mp4")

# Verifica se o vídeo foi aberto com sucesso
if cap.isOpened():
    while True:
        # Lê um quadro do vídeo
        ret, frame = cap.read()

        # Verifica se o quadro foi lido com sucesso
        if ret:
            # Mostra o quadro na tela
            cv2.imshow("Vídeo", frame)

            # Aguarda o usuário pressionar uma tecla
            cv2.waitKey(1)
        else:
            # O quadro não foi lido com sucesso
            break