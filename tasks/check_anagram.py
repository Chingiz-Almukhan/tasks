def check_anagram(string: str, anagram_string: str) -> bool:
    string = string.lower().replace(' ', '')
    anagram_string = anagram_string.lower().replace(' ', '')

    if len(string) != len(anagram_string):
        return False

    sorted_strings = [sorted(list(string)), sorted(list(anagram_string))]

    if sorted_strings[0] == sorted_strings[1]:
        return True
    else:
        return False


base_string = "Silent"
string_to_check = "Listen"

if check_anagram(base_string, string_to_check):
    print(f"{base_string} && {string_to_check} - anagram")
else:
    print(f"{base_string} && {string_to_check} - doesnt anagram")