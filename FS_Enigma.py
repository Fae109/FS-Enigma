import random

# Two-letter mapping as specified
two_letter_map = {
    'XI': ':', 'ZX': '*', 'XL': '0', 'XE': ')', 'YA': '3', 'YO': '4', 'YI': 'z',
    'ZF': 'y', 'YR': '[', 'YU': 'b', 'ZN': '%', 'YE': '6', 'YT': 'p', 'ZD': '7',
    'ZP': 'h', 'ZW': 'j', 'ZE': '#', 'YH': ';', 'YB': 'd', 'XG': '8', 'YX': 'g',
    'YZ': '$', 'ZI': 'm', 'XM': '"', 'YM': '/', 'YK': '|', 'YY': '?', 'YJ': "'",
    'ZS': '}', 'YQ': 'q', 'ZA': 'f', 'XA': '{', 'YV': 'e', 'YN': 'w', 'ZC': 'l',
    'YP': '+', 'ZG': 's', 'ZK': '`', 'ZT': 'u', 'ZH': 'n', 'ZQ': '9', 'YD': 'o',
    'ZY': '!', 'ZZ': '&', 'ZM': '(', 'YS': '\\', 'ZL': 'c', 'ZB': ']', 'XF': '@',
    'XC': 'i', 'YF': '~', 'ZO': '5', 'XD': '2', 'ZU': '1', 'XJ': 'a', 'XK': 'r',
    'YC': 'k', 'YG': '-', 'ZR': 't', 'XB': 'x', 'YW': '_', 'YL': '^', 'XH': '=',
    'ZJ': '.', 'WD': ',', 'WL': 'A', 'WQ': 'B', 'WR': 'C', 'WJ': 'D', 'WG': 'E',
    'WM': 'F', 'WY': 'G', 'WE': 'H', 'WT': 'I', 'WP': 'J', 'WH': 'K', 'WX': 'L',
    'WF': 'M', 'WI': 'N', 'WU': 'O', 'WC': 'P', 'WS': 'Q', 'VA': 'R', 'WZ': 'S',
    'WV': 'T', 'WA': 'U', 'WO': 'V', 'WB': 'W', 'WW': 'X', 'WN': 'Y', 'WK': 'Z', 'XX':'v'
}
# Reverse mapping for encoding
encode_map = {v: k for k, v in two_letter_map.items()}

def encode_message(text: str) -> str:
    """Encode plaintext to custom code, inserting a random letter for spaces."""
    encoded = ''
    for ch in text:
        if ch in encode_map:
            encoded += encode_map[ch]
        elif ch.upper() in encode_map:  # Added this elif to handle uppercase
            encoded += encode_map[ch.upper()]
        elif ch == ' ':
            encoded += random.choice('ABCDEFGHIJKLMNOPQRSTU')
        else:
            encoded += ch
    return encoded

def decode_message(code: str) -> str:
    """Decode custom code to plaintext, removing random single-letter separators."""
    i = 0
    decoded = ''
    starts = {k[0] for k in two_letter_map}
    while i < len(code):
        if code[i] in starts and i + 1 < len(code):
            pair = code[i:i+2]
            if pair in two_letter_map:
                decoded += two_letter_map[pair]
                i += 2
                continue
        # Skip noise
        i += 1
        # If next starts a valid pair, add space
        if i < len(code) and code[i] in starts:
            decoded += ' '
    return decoded

def main():
    mode = input("Choose mode: (E)ncode or (D)ecode? ").strip().upper()
    if mode == 'E':
        msg = input("Enter text to encode: ")
        print("\nEncoded output:\n" + encode_message(msg))
    elif mode == 'D':
        msg = input("Enter code to decode: ")
        print("\nDecoded output:\n" + decode_message(msg))
    else:
        print("Invalid option. Run again and choose E or D.")

if __name__ == '__main__':
    main()


# Brought to you by Fae Studios (2025)
