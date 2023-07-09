import solara
import random 

emojis = ["𓃥", "𓃠", "𓃰", "𓃱", "𓃯", "𓃭", "𓃸", "𓃵", "𓃗", "𓃘", "𓃙",\
    "𓃟", "𓄀", "𓄁", "𓄂", "𓄃", "𓃚", "𓃛", "𓃜", "𓃝", "𓃞", "𓃒",
    "𓃓", "𓃔", "𓃕", "𓃖", "𓃡", "𓃢", "𓃦", "𓃩", "𓃫", "𓃬", "𓃮", 
    "𓃲", "𓃴", "𓃶", "𓃷", "𓃹", "𓃻", "𓃽", "𓃾", "𓃿", "𓄄", "𓄅", "𓄆", 
    "𓄇", "𓆇", "𓆈", "𓆉", "𓆌", "𓆏", "𓆗", "𓆘", "𓆙", "𓆚", "𓆐", "𓆑", 
    "𓆒", "𓆓", "𓆔", "𓆕", "𓆖", "𓆊", "𓆍", "𓆣", "𓆤", "𓆥", "𓆦", "𓆧", 
    "𓆨", "𓆛", "𓆜", "𓆝", "𓆞", "𓆟", "𓆠", "𓆡", "𓆢", "𓄿", "𓅀", "𓅁", 
    "𓅂", "𓅃", "𓅄", "𓅅", "𓅆", "𓅇", "𓅈", "𓅉", "𓅊", "𓅋", "𓅌", "𓅍", 
    "𓅎", "𓅏", "𓅐", "𓅑", "𓅒", "𓅓", "𓅔", "𓅕", "𓅖", "𓅗", "𓅘", "𓅙", 
    "𓅚", "𓅛", "𓅜", "𓅝", "𓅞", "𓅟", "𓅠", "𓅡", "𓅢", "𓅣", "𓅤", "𓅥", 
    "𓅦", "𓅧", "𓅨", "𓅩", "𓅪", "𓅫", "𓅬", "𓅭", "𓅮", "𓅯", "𓅰", "𓅱", 
    "𓅲", "𓅳", "𓅴", "𓅵", "𓅶", "𓅷", "𓅸", "𓅹", "𓅺", "𓅻", "𓅼", "𓅽", 
    "𓅾", "𓅿", "𓆀", "𓆁", "𓆂", "𓆃", "𓆆", "🦓", "🦬", "🦣", "🦒", "🦦", "🦥", 
    "🦘", "🦌", "🐢", "🦝", "🦭", "🦫", "🐆", "🐅", "🦎", "🐍", "🐘", "🦙", "🐫", 
    "🐪", "🐏", "🐐", "🦛", "🦏", "🐂", "🐃", "🐎", "🐑", "🐒", "🦇", "🐖", "🐄", 
    "🐛", "🐝", "🦧", "🦍", "🐜", "🐞", "🐌", "🦋", "🪳", "🪲", "🪱", "🪰", "🦟", 
    "🦂", "🕷️", "🦗", "🐨", "🐯", "🦁", "🐮", "🐰", "🐻", "🐻‍❄️", "🐼", "🐶", "🐱", 
    "🐭", "🐹", "🐗", "🐴", "🐽", "🐷", "🐣", "🐥", "🐺", "🦊", "🐔", "🐧", "🐦", 
    "🐤", "🐋", "🐊", "🐸", "🐵", "🐡", "🐬", "🦈", "🐳", "🦐", "🦪", "🐠", "🐟", 
    "🐙", "🦑", "🦞", "🦀", "🦅", "🕊️", "🦃", "🐓", "🦉", "🦤", "🦢", "🦆", "🪶", 
    "🦜", "🦚", "🦩", "🐩", "🐕‍🦺", "🦮", "🐕", "🐁", "🐀", "🐇", "🐈", "🦔", "🦡", 
    "🦨", "🐿️", ]

row_count = 5
col_count= 5

def reset_state(state): 
    """Reset state"""
    for row in state: 
        for cell in row: 
            cell.set("-")
    
def get_init_state(how_many_moles = 0): 
    """
    Get initial game state of a non-started whacamole game
    Args:
        how_many_moles (int, optional): How many moles to include. Defaults to 0.
    Returns:
        (object)): state of the game
    """
    init_matrix = []
    
    for i in range(row_count): 
        row = []
        for j in range(col_count): 
            row.append("-")
        init_matrix.append(row)    

    state = build_state_from_matrix(init_matrix)
    place_moles(state, how_many_moles)
    return state

def build_state_from_matrix(init_matrix): 
    state = []
    for init_row in init_matrix: 
        row = []
        for value in init_row: 
            row.append(solara.reactive(value))
        state.append(row)
    return state    

def place_moles(state, how_many_moles = 0): 
    """Place moles"""
    for _ in range(how_many_moles): 
        row_i = random.randint(0, row_count - 1)
        col_i = random.randint(0, col_count - 1)
        emoji_i = random.randint(0, len(emojis) - 1)
        #print(row_i, col_i, emoji_i)
        state[row_i][col_i].set(emojis[emoji_i])

def refresh_state(state, how_many_moles = 0):
    """Refresh state"""
    for row in state: 
        for cell in row: 
            cell.set("-")
    place_moles(state, how_many_moles)
    