import textjumbler


def main():

    print("------------------")
    print("| codedrome.com  |")
    print("| Jumbled Text   |")
    print("------------------\n")

    sample = "It doesn't matter in what order the letters in a word are, the only important thing is that the first and last letter be at the right place. The rest can be a total mess and you can still read it without problem. This is because the human mind doss not read every letter by itself, but the word as a whole."

    Ozymandias = 'I met a Traveller from an antique land\nWho said: Two vast and trunkless legs of stone\nStand in the desart.  Near them, on the sand,\nHalf sunk, a shattered visage lies, whose frown,\nAnd wrinkled lip, and sneer of cold command,\nTell that its sculptor well those passions read\nWhich yet survive, stamped on these lifeless things,\nThe hand that mocked them and the heart that fed:\nAnd on the pedestal these words appear:\n"My name is Ozymandias, king of kings:\nLook on my works, ye Mighty, and despair!"\nNothing beside remains.  Round the decay\nOf that colossal wreck, boundless and bare\nThe lone and level sands stretch far away.'

    TaleOfTwoCities = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way — in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only."

    jumbled = textjumbler.jumble(sample, 0.3)

    print(jumbled)


if __name__ == "__main__":

    main()
