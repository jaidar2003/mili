import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_bear_face():
    # Crear la figura y los ejes
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_aspect('equal')
    ax.axis('off')  # Quitar los ejes

    # Cara (círculo grande)
    face = patches.Circle((0.5, 0.5), 0.4, edgecolor='black', facecolor='#d2a679')
    ax.add_patch(face)

    # Oreja izquierda (círculo grande y pequeño)
    left_ear_outer = patches.Circle((0.2, 0.75), 0.15, edgecolor='black', facecolor='#d2a679')
    left_ear_inner = patches.Circle((0.2, 0.75), 0.1, edgecolor='black', facecolor='#8b4513')
    ax.add_patch(left_ear_outer)
    ax.add_patch(left_ear_inner)

    # Oreja derecha (círculo grande y pequeño)
    right_ear_outer = patches.Circle((0.8, 0.75), 0.15, edgecolor='black', facecolor='#d2a679')
    right_ear_inner = patches.Circle((0.8, 0.75), 0.1, edgecolor='black', facecolor='#8b4513')
    ax.add_patch(right_ear_outer)
    ax.add_patch(right_ear_inner)

    # Ojo izquierdo (círculo blanco y negro)
    left_eye_white = patches.Circle((0.35, 0.55), 0.06, edgecolor='black', facecolor='white')
    left_eye_black = patches.Circle((0.35, 0.55), 0.03, edgecolor='black', facecolor='black')
    ax.add_patch(left_eye_white)
    ax.add_patch(left_eye_black)

    # Ojo derecho (círculo blanco y negro)
    right_eye_white = patches.Circle((0.65, 0.55), 0.06, edgecolor='black', facecolor='white')
    right_eye_black = patches.Circle((0.65, 0.55), 0.03, edgecolor='black', facecolor='black')
    ax.add_patch(right_eye_white)
    ax.add_patch(right_eye_black)

    # Nariz (elipse negra)
    nose = patches.Ellipse((0.5, 0.4), 0.1, 0.07, edgecolor='black', facecolor='black')
    ax.add_patch(nose)

    # Boca (líneas)
    ax.plot([0.5, 0.5], [0.37, 0.34], color='black')
    ax.plot([0.5, 0.47], [0.34, 0.31], color='black')
    ax.plot([0.5, 0.53], [0.34, 0.31], color='black')

    # Mostrar la figura
    plt.show()

# Llamar a la función para dibujar la cara del osito
draw_bear_face()

##
