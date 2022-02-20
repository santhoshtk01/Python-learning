# Program to read and write binary files using Pickle module
import pickle


# Function to iterate through the nested iterables..
def iterate(values: tuple) -> None:
    """
    Iterates through the nested `tuple` and prints out each value in the tuple
    in an recursive way..

    Args:
         values: The iterable to be iterated `tuple`..
    """
    for val in values:
        if isinstance(val, tuple):
            iterate(val)
        else:
            print(val)


data = ('More Mayhem',
          'IMelda May',
          '2011',
          ((1, 'Pulling the Rug'),
           (2, 'Psycho'),
           (3, 'Mayhem'),
           (4, 'Kentish Town Waltz')))

# Code to serialize an object to the file..
with open('songs.pickle', mode='wb') as songs:
    pickle.dump(data, file=songs)

# Code to read the serialized object in the same form as we stored
with open('songs.pickle', mode='rb') as songs_pickle:
    songs_data = pickle.load(songs_pickle)

# iterate(songs_data)
