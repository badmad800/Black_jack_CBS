SUITS = ['heart', 'diamond', 'club', 'spade']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
PRINTED = {
    'ace':
        """*********
*   ^   *
*  / \  *
* /___\ *
*/     \*
*********""",
    'king':
"""*********
* |  /  *
* | /   *
* | \   *
* |  \  *
*********""",
    'queen':
"""*********
* ----- *
* |   | *
* |   | *
* |___|b*
*********""",
    'jack':
"""*********
*  ---- *
*     | *
*     | *
* |___| *
*********""",
    '10':
"""*********
* | |--|*
* | |  |*
* | |  |*
* | |__|*
*********""",
    '9':
"""*********
* ----- *
* |___| *
*     | *
* |___| *
*********""",
    '8':
"""*********
*|----| *
*|____| *
*|    | *
*|____| *
*********""",
    '7':
"""*********
* ----- *
* |   | *
*    -| *
*     | *
*********""",

    '6':
"""*********
* ----- *
* |     *
* |----| *
* |____|*
*********""",
    '5':
"""*********
*  ---- *
* |     *
*  ----|*
*  ____|*
*********""",
    '4':
"""*********
*       *
* |    |*
*  ----|*
*      |*
*********""",
    '3':
"""*********
* -----|*
* _____|*
*      |*
* _____|*
*********""",
    '2':
"""*********
* ----- *
* |  /  *
*   /   *
*  /___|*
*********"""

}

MESSAGE = {
    'ask_start': 'Want to play?(y/n) ',
    'ask_card': 'Want new card?(y/n) ',
    'eq': '{player} player has {points} points so it eq with dealer points\n {player} bid will be back',
    'win': '{} player are win',
    'lose': '{} player are lose',
    'rerun': 'Do you want to play again ?(y/n)'
}

NAMES = ['John', 'Jack', 'Vasya', 'Alex']