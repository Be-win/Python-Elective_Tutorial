def count_words(text):
    words = text.split()
    return len(words)

def count_sentences(text):
    punctuations = ['.', '?', '!']
    count = 0
    flag = False
    for char in text:
        if char in punctuations:
            count += 1
            flag = False
        else:
            flag = True
    if flag:
        count += 1
    return count

def count_syllables(word):
    word = word.lower()
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    if len(word) <= 3:
        return 1
    if word[-2:] == 'es' or word[-2:] == 'ed':
        word = word[:-2]
    elif word[-1:] == 'e':
        if word[-2:] != 'le':
            word = word[:-1]
    for i in range(len(word)):
        if word[i] in vowels:
            count += 1
            if i>=0 and word[i-1] in vowels:
                count -= 1
    return count

def total_syllables(text):
    total_count = 0
    for word in text.split():
        total_count += count_syllables(word)
    return total_count

def find_flesch_index(words, sentences, syllables):
    if words == 0 or sentences == 0:
        return 0
    flesch_index = 206.835 - 1.015 * (words / sentences) - 84.6 * (syllables / words)
    return flesch_index

def find_grade(words, sentences, syllables):
    if words == 0 or sentences == 0:
        return 0
    grade_level = 0.39 * (words / sentences) + 11.8 * (syllables / words) - 15.59
    return grade_level


file = open('input.txt', 'r')
text = file.read()

words = count_words(text)
sentences = count_sentences(text)
syllables = total_syllables(text)

flesch_index = find_flesch_index(words, sentences, syllables)
grade = find_grade(words, sentences, syllables)

print("Flesch Index : " + f"{flesch_index:.2f}")
print("Grade : " + f"{grade:.2f}")

if flesch_index >= 90:
    print("Readability : 4th Grade")
elif flesch_index >= 50:
    print("Readability : High School")
else:
    print("Readability : College")

file.close()