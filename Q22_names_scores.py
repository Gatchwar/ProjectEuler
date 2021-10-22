def main():
    score = 0  # track the overall score
    index = 1  # track the index of the sorted list which is multiplied against the name score
    with open('external_files/names.txt', 'r') as f:
        # read the text in the file , remove the quotations with replace and split into a list using the commas
        sorted_names = sorted(f.read().replace('\"', '').split(','))
        for name in sorted_names:
            name_score = 0
            for letter in name:
                name_score += ord(letter) - 64  # ord() gets ASCII value of the letter, subtract 64 to get value
            score += name_score * index
            index += 1
    f.close()
    print(score)


if __name__ == "__main__":
    main()
