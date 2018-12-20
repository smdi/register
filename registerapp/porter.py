LOCATION_CHOICES = (

    ('Hyd', 'Hyderabad'),
    ('Chi', 'Chennai'),
    ('Bgn', 'Banglore'),
    ('Msr', 'Mysore')

)

GENDER_CHOICES = (

    ('M', 'Male'),
    ('F', 'Female')

)


YEARS = range(1990,2010)



def is_empty(any_structure):
    if any_structure:
        print('Structure is not empty.')
        return False
    else:
        print('Structure is empty.')
        return True










