"""Typing test implementation"""

from utils import *
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    ret=[x for x in paragraphs if select(x)]
    if k>=len(ret):
        return ''
    else:
        return ret[k]
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    def about_select(string):
        match=[]
        a=topic
        string=remove_punctuation(string)
        string=lower(string)
        strung_x=split(string)
        while len(a)>0:
            match+=[x for x in strung_x if x==a[0]]
            a=a[1:]
        if match:
            return True
        else:
            return False
    return about_select
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    total=0
    denom=0
    ty=typed_words
    ref=reference_words
    while len(typed_words)>0:
        if len(reference_words)==0:
            denom+=1
            break
        x=typed_words[0]
        if x==reference_words[0]:
            total+=1
        denom+=1
        typed_words=typed_words[1:]
        reference_words=reference_words[1:]
    if len(ty)==0:
        ty+=[1]
    return 100*total/len(ty)
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    return (len(typed)/5)/(elapsed/60)
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    if user_word in valid_words:
        return user_word
    a=min(valid_words,key=lambda word: diff_function(user_word,word,limit))
    if diff_function(user_word,a,limit)>limit:
            return user_word
    else:
        return a
    '''for x in valid_words:
        if diff_function(user_word,x,limit)==0:
            return user_word
        elif diff_function(user_word,x,limit)>limit:
            return user_word
        else:
            a=min(valid_words,key=lambda word:diff_function(user_word,word,limit))
            return a'''
    # END PROBLEM 5


def swap_diff(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    if len(start)==0:
        return len(goal)
    if len(goal)==0:
        return len(start)
    if start==goal:
        return 0
    if limit==0:
        return 1
    if start[0]==goal[0]:
        return 0+swap_diff(start[1:], goal[1:], limit)
    else:
        return 1+swap_diff(start[1:], goal[1:], limit-1)
    # END PROBLEM 6

def edit_diff(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    if start==goal: # Fill in the condition
        # BEGIN
        return 0
        # END
    if len(start)==0:
        return len(goal)
    if len(goal)==0:
        return len(start)
    elif limit==0: # Feel free to remove or add additional cases
        # BEGIN
        return 1
        # END
    elif start[0]==goal[0]:
        return 0+edit_diff(start[1:], goal[1:], limit)
    else:
        add_diff = 1+edit_diff(goal[0]+start, goal, limit-1)  # Fill in these lines
        remove_diff = 1+edit_diff(start[1:], goal, limit-1)
        substitute_diff = 1+edit_diff(goal[0]+start[1:], goal, limit-1)
        # BEGIN
        return min(add_diff,remove_diff,substitute_diff)
        # END


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'




###########
# Phase 3 #
###########


def report_progress(typed, prompt, id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    right_count=0
    p=prompt
    while len(typed)>0:
        if typed[0]!=prompt[0]:
            break
        else:
            right_count+=1
            typed=typed[1:]
            prompt=prompt[1:]
    a=right_count/len(p)
    send({'id': id, 'progress': a})
    return a
    # END PROBLEM 8


def fastest_words_report(word_times):
    """Return a text description of the fastest words typed by each player."""
    fastest = fastest_words(word_times)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report

'clement.messeri@berkeley.edu'
def fastest_words(word_times, margin=1e-5):
    """A list of which words each player typed fastest."""
    n_players = len(word_times)
    n_words = len(word_times[0]) - 1
    assert all(len(times) == n_words + 1 for times in word_times)
    assert margin > 0
    # BEGIN PROBLEM 9

    def helper_time(index,player):
        return elapsed_time(word_times[player][index]) - elapsed_time(word_times[player][index-1])

    def shortest_time(word):
        list=[helper_time(word,player) for player in range(len(word_times))]

        return min(list)

    the_result=[]

    for player in range(len(word_times)):
        player_list=[]
        for word_num in range(1,len(word_times[0])):

            if helper_time(word_num,player) < shortest_time(word_num) + margin:
                player_list += [word(word_times[0][word_num])]
        the_result += [player_list]


    return the_result





    """da_result=[]
    list_of_time_differences=[]
    for word in range(1,len(word_times[0])):
        shortest_time=float('inf')
        for player in range(len(word_times)):
            time_difference=helper_time(word_times[player][word],word_times[player][word-1])

            if shortest_time>time_difference:
                shortest_time=time_difference












        #for player in range(len(word_times)):
            # list_of_word=[word_times[player][word] for player in range(len(word_times))]
            list_of_time_differences+=[[player, helper_time(word_times[player][word],word_times[player][word-1] for player in range(len(word_times))]
        #------- this should return a list of elements where each element is a list of two elements. The 0th element is the player number and the 1st element is the time difference (a number)
        #this is a list for every word, for every player, so [player0 word1, player1word1, player0 word2, player1 word2...]
                #shortest_time=min([list_of_time_differences[player][1] for player in range(word_times)])
            #    if shortest_time==list_of_time_differences[player][1]:
            #        then player_fastest
            for player in range(len(word_times)):
            player_fastest=
            da_result+=player_fastest








        #fastest_player_for_word=[min(word_times[player],key=lambda x: helper_time(word_times[player][word],word_times[player][word-1])==player)]


            player_fastest=
            da_result+=player_fastest


    return da_result
    """

    # END PROBLEM 9


def word_time(word, elapsed_time):
    """A data abstrction for the elapsed time that a player finished a word."""
    return [word, elapsed_time]


def word(word_time):
    """An accessor function for the word of a word_time."""
    return word_time[0]


def elapsed_time(word_time):
    """An accessor function for the elapsed time of a word_time."""
    return word_time[1]


enable_multiplayer = False  # Change to True when you


##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)
