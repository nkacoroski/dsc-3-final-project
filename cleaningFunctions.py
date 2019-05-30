def select_features(dataframe, dtype, exclude_list):
    """Returns list of columns names to include as features"""
    columns = list(dataframe.select_dtypes(include=dtype).columns.values)
    features = [e for e in columns if e not in exclude_list]
    return features

def common_value(x):
    """Return most common value"""
    if ',' in x:
        return x.split(',')[0]
    else:
        return x
    
def bin_category(x):
    """Return categories with low value counts in a bin"""
    if (x == 'Dicot') or (x == 'Monocot') or (x == 'Gymnosperm'):
        return x
    else:
        return 'Other'
    
def num_of_growth_seasons(x):
    """Return growth period length"""
    one_season = ['Spring', 'Summer', 'Fall']
    two_seasons = ['Spring and Summer', 'Summer and Fall', 'Spring and Fall']
    three_seasons = ['Spring, Summer, Fall', 'Fall, Winter and Spring']
    if x in one_season:
        return 'one'
    elif x in two_seasons:
        return 'two'
    elif x in three_seasons:
        return 'three'
    else:
        return 'four'

def binarize_bloat(x):
    """Return one if any bloat and zero if none"""
    if x == 'None':
        return 0
    else:
        return 1
    
def binarize_foliage_color(x):
    """Return one if green and zero if not green"""
    not_green = ['White-Gray', 'Red']
    if x in not_green:
        return 0
    else:
        return 1
    
def binarize_nitrogen_fixation(x):
    """Return one if a nitrogen fixer and zero if not"""
    if x == 'None':
        return 0
    else:
        return 1
    
def erect_shape(x):
    """Return one if shape erect and zero if not"""
    erect = ['Erect', 'Semi-Erect']
    if x in erect:
        return 1
    else:
        return 0
    
def binarize_toxicity(x):
    """Return one if toxic and zero if not"""
    if x == 'None':
        return 0
    else:
        return 1
    
def bloom_period(x):
    """Return generalized bloom period"""
    spring = ['Late Spring', 'Mid Spring', 'Spring', 'Early Spring']
    summer = ['Summer', 'Early Summer', 'Mid Summer', 'Late Summer']
    if x in spring:
        return 'spring'
    elif x in summer:
        return 'summer'
    else:
        return 'other'
    
def seed_abundance(x):
    """Return seed abundance with low and none as one category"""
    if (x =='Low') or (x == 'None'):
        return 'low_none'
    else:
        return x
    
def seed_start(x):
    """Return seed start with year round and winter as one category"""
    if (x =='Year Round') or (x == 'Winter'):
        return 'other'
    else:
        return x
    
def seed_end(x):
    """Return seed end with year round and winter as one category"""
    if (x =='Year Round') or (x == 'Winter'):
        return 'other'
    else:
        return x
    
