def wordType(type):
    word_type = None
    if(type == 'ps_v'):
        word_type = 'Verb'
    if(type == 'ps_n'):
        word_type = 'Noun'
    if(type == 'ps_lk'):
        word_type = 'Linker'
    if(type == 'ps_mod'):
        word_type = 'Modifier'
    if(type == 'ps_rhet'):
        word_type = "Rhetorical"
    if(type == 'ps_neg'):
        word_type = "Negative"
    if(type == 'ps_neg_ext'):
        word_type = "Negative Existential"
    
    return word_type