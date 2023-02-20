#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import traceback


# Print exception error message
def catch_exception(e):    
    print(str(e))
    print(traceback.format_exc())
    
    
# Generate a warning message for candidates with a tied score
def create_tie_warning_message(number_of_tied_candidates):
    message = "ATENCIÓ: Existeixen {number} candidats amb la mateixa puntuació ".format(number =
                                                              number_of_tied_candidates) + \
              "en aquesta especialitat i aquí apareixen ordenats per ordre alfabètic. " + \
              "Per a obtenir un nombre de posició més acurat, " + \
              "consulteu els criteris de desempat de la convocatòria."
    return message
