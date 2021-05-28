# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define k1 = Character("Pelajar")


# The game starts here.

label start:

    # Menunjukkan paparan latarbelakang

    scene fizik

    # Karakter

    show pelajar

    # These display lines of dialogue.

    k1 "You've created a new Ren'Py game."

    k1 "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
