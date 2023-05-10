# Flash Cards for Language Learning
Flash cards project created using Python and the Tkinter library.  
The program loads a card containing a random word in French from a file and
waits for 3 seconds until showing the answer in English. The user can click one of two
buttons.  
By clicking the ✅ button, the user signals that they have already learned
that word, therefore the word is taken out of the pool of potential words.  
By clicking the ❌ button, the user signals that they haven't learned
that word, therefore the word remains in the pool of potential words.  
The words the user still hasn't learned are saved in words_to_learn.csv once the
program is closed.