def GetGenitive(base_form, polish):
    '''Tworzy forme dopelniacza formy bazowej (base_form)'''
    if polish: # nazwa polska (miejscowosc na obszarze Polski)
        return _getpolishgenitive(base_form)
    else: # miejscowosc poza granicami Polski
        return _getforeigngenitive(base_form)

def _getpolishgenitive(base_form):    
    '''Tworzy forme dopelniacza nazwy polskiej'''
    if base_form[-1] == 'a': 
        return _getforeigngenitive(base_form)
    elif base_form[-2:] in ['ak', 'ik']: # typ Babiak, Barak
        return base_form + 'a'
    elif base_form[-4:] == 'niek': # typ Bieniek
        return base_form[:-4] + 'ńka'
    elif base_form[-4:] == 'ciek': # typ Bociek
        return base_form[:-4] + 'ćka'
    elif base_form[-4:] == 'siek' and base_form != 'Osiek' and base_form != 'Przysiek': # typ Dysiek
        return base_form[:-4] + 'śka'
    elif base_form[-4:] == 'ziek': # typ Bruziek
        return base_form[:-4] + 'źka'
    elif base_form[-2:] in ['ek']: # typ Borek, Baranek
        return base_form[:-2] + 'ka'
    elif base_form[-1] in ['ż', 'c', 'j', 'l'] or base_form[-2:] in ['dz', 'cz', 'sz', 'dż', 'rz']: # typ Bagicz, Czekaj, Modzel
        return base_form + 'a'
    elif base_form[-1] in ['b', 'p', 'd', 't', 'f', 'w', 'v', 'h', 'm', 'n', 'r', 'z', 's', 'q', 'x']: # typ Garb, Czop
        return base_form + 'u'
    elif base_form[-1] in ['k', 'g']: # typ Blok, Bruk
        return base_form + 'u'
    elif base_form[-3:] in ['ice', 'yce']: # typ Czechowice
        return base_form[:-1]
    elif base_form[-1] == 'e': # typ Pole, Błocie
        return base_form[:-1] + 'a'
    elif base_form[-1] == 'i': # typ Baściki, Bąki
        return base_form[:-1] + 'ów'
    else: # pozostale nieodmienne
        return base_form

def _getforeigngenitive(base_form):
    '''Tworzy forme dopelniacza nazwy zagranicznej'''
    if base_form[-1] == 'a' and base_form != 'Tonga, Samoa':
        if base_form[-2] in ['b', 'p', 'c', 'd', 't', 'f', 'w', 'v', 'h', 'm', 'n', 'r', 'z', 's', 'q', 'x']: # typ Kanada, Valetta
            return base_form[:-1] + 'y'
        elif base_form[-2] in ['k', 'g', 'l']: # typ Haga, Hagi
            return base_form[:-1] + 'i'
        elif base_form[-2] == 'j': # typ Azja, Azji; Achaja, Achai
            if base_form[-3] in ['a', 'e', 'i', 'o', 'u', 'y']:
                return base_form[:-2] + 'i' # Achaja, Achai
            else:
                return base_form[:-1] + 'i' # Azja, Azji
        elif base_form[-2:] in ['ea', 'ua', 'oa', 'ia']: # typ Korea, Nikaragua, Kalifornia 
            return base_form[:-1] + 'i'
        else: 
            return base_form
    else: 
        return base_form
