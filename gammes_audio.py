# -*- coding: utf-8 -*-
# vicenté quantic cabviva

import inspect
from typing import Callable

# lineno() Pour consulter le programme grâce au suivi des print’s
lineno: Callable[[], int] = lambda: inspect.currentframe().f_back.f_lineno


class audio_gam:
    """"""

    def __init__(self, gammes, mode):
        self.data = gammes  # Clé = Tuple (Colonne. Ligne). Ligne = 0 = Nom de la gamme. Une colonne = Une gamme.

        print("FONCTION : gammes_audio.audio_gam :", self.data, "mode", mode)
        pass
