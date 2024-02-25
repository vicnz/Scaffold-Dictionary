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
    if(type == 'ps_ext'):
        word_type = "Existential"
    if(type == 'ps_part'):
        word_type = "Participle"
    if(type == 'ps_pron'):
        word_type = "Pronoun"
    if(type == 'ps_cntrc'):
        word_type = "Contraction"
    if(type == 'ps_cntc'):
        word_type = "Contraction"
    if(type == 'ps_cntrc_neg'):
        word_type = "Negative Contraction"
    if(type == 'ps_tm_mk'):
        word_type = "Time Marker"
    if(type == 'ps_excl'):
        word_type = "Exclamation"
    if(type == 'ps_mk'):
        word_type = "Marker"
    if(type == 'ps_rlr'):
        word_type = "Relator"
    if(type == 'ps_sfx'):
        word_type = "Suffix"
    if(type == 'ps_pfx'):
        word_type = "Prefix"
    if(type == 'ps_afx'):
        word_type = "Affix"
    if(type == 'ps_num'):
        word_type = "Number"
    if(type == 'ps_ord_num'):
        word_type = "Ordinal Number"
    if(type == 'ps_intg'):
        word_type = "Interrogative Particle"
    if(type == 'ps_quant'):
        word_type = "Quantifier"
    if(type == 'ps_dei'):
        word_type = "Deictic"
    if(type == 'ps_exp'):
        word_type = "Expression"
    if(type == 'ps_tm'):
        word_type = "Time"
    if(type == 'ps_comm'):
        word_type = "Command"
    if(type == 'ps_com'):
        word_type = "Compound"
    if(type == 'ps_lmt'):
        word_type = "Limitizer"
    
    return word_type