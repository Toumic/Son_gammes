# -*- coding: utf-8 -*-
# vicenté quantic cabviva

import inspect
from typing import Callable

# lineno() Pour consulter le programme grâce au suivi des print’s
lineno: Callable[[], int] = lambda: inspect.currentframe().f_back.f_lineno


class audio_bin:
    """"""

    def __init__(self, binary, mode, tri):
        self.data = binary  # Clé = Tuple (Colonne. Ligne). Ligne = 0 = Nom de la gamme. Une colonne = Une gamme.

        print("FONCTION : binomes_audio.audio_bin : ", self.data, "mode", mode, len(mode), "tri", tri)
        pass
