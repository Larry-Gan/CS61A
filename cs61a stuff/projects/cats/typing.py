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
    "*** YOUR CODE HERE ***"

    list=[paragraphs[i] for i in range(0,len(paragraphs)) if select(paragraphs[i]) ]

    if k >= len(list):
        return ''
    return list[k]
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
    "*** YOUR CODE HERE ***"

    def select(para):
        check = split(lower(remove_punctuation(para)))
        for i in range(0,len(topic)):
            if topic[i] in check:
                return True
        return False
    return select
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
    "*** YOUR CODE HERE ***"
    if min(len(typed_words),len(reference_words))==0:
        return 0.0
    result = 0
    for words in range(min(len(typed_words),len(reference_words))):
        if typed_words[words] == reference_words[words]:
            result += 1
    result = result/len(typed_words) * 100
    return result
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"

    characters= len(typed)
    words = characters/5
    wpm = words/elapsed * 60
    return wpm
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    if user_word in valid_words:
        return user_word
    best_diff = float('inf')
    best_word = user_word
    for word in valid_words:
        this_word_diff = diff_function(user_word,word, limit)
        if this_word_diff <= limit:
            if best_diff > this_word_diff:
                best_word = word
                best_diff = this_word_diff
    return best_word
    # END PROBLEM 5


def swap_diff(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6

# do a recursion where you add 1 if something changed
    if start == goal:
        return 0
    if start == '':
        return len(goal)
    if goal == '':
        return len(start)
    if limit == 0:
        return 1

    if start[0] == goal[0]:
        return swap_diff(start[1:],goal[1:],limit)
    return 1 + swap_diff(start[1:],goal[1:],limit - 1)

    """
    from operator import abs

    if start==goal:
        return 0
    def helper_swap(word1,word2,index,limit):
        if index>=min(len(word1),len(word2)):
            return abs(len(word1)-len(word2))
        if limit==0:
            return 1


        if word1[index]==word2[index]:
            return helper_swap(word1,word2,index+1,limit)
        return 1+helper_swap(word1,word2,index+1,limit-1)
    return helper_swap(start,goal,0,limit)
    """
    # END PROBLEM 6

def edit_diff(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""


    if start == goal: # Fill in the condition
        # BEGIN
        return 0
        # END

    elif start == '' or goal == '':
        return max(len(start),len(goal))
    elif limit == 0:
        return 1

    #if the 0 index is the same, make the call on [1:]
    elif start[0] == goal[0]:
        return edit_diff(start[1:],goal[1:],limit)
#start from the left and just go!
    else:
        add_diff = 1 + edit_diff(start,goal[1:],limit - 1)  # Fill in these lines -----------------I don't think I am doing the recursive calls right... help?
        remove_diff = 1 + edit_diff(start[1:],goal,limit - 1)
        substitute_diff = 1 + edit_diff(start[1:],goal[1:],limit - 1)#----if index 0 matches,
        # BEGIN
        return min(add_diff,remove_diff, substitute_diff,swap_diff(start,goal,limit))
        # END


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""





###########
# Phase 3 #
###########


def report_progress(typed, prompt, id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
#returning the right value -- actually I'll just shove the creation and sending in there as well, cause i'm not sure how to use break yet
    for index in range(0,len(typed)):
        if typed[index] != prompt[index]:
            progress = index/len(prompt)
            message = {'id':id, 'progress':progress} #----- bad dictionary syntax I think
            send(message)
            return progress
    send({'id':id, 'progress':len(typed)/len(prompt)})
    return len(typed)/len(prompt)
    # END PROBLEM 8


def fastest_words_report(word_times):
    """Return a text description of the fastest words typed by each player."""
    fastest = fastest_words(word_times)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report

"lbgan2000@berkeley.edu"
def fastest_words(word_times, margin=1e-5):
    """A list of which words each player typed fastest."""
    n_players = len(word_times)
    n_words = len(word_times[0]) - 1
    assert all(len(times) == n_words + 1 for times in word_times)
    assert margin > 0
    # BEGIN PROBLEM 9
    #create a helper function that spits out the time takne for each word.
    # we have 'row' vectors, we want to compare them in 'column' + caveat, the margin!
    # let's do this!
    def helper_time(index,player):
        return elapsed_time(word_times[player][index]) - elapsed_time(word_times[player][index-1])

    def shortest_time(word):
        list = [helper_time(word,player) for player in range(len(word_times))]

        return min(list)

    the_result = []

    for player in range(len(word_times)):
        player_list = []
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
