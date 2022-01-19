# https://app.betrybe.com/course/live-lectures/sd-cohort-9#aula-352-recursividade-e-estrategias-para-solucao-de-problemas


def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False
    array_string = list(word)
    reverse_word = "".join(inverse_recursive(array_string))

    if reverse_word != word:
        return False
    return True


def inverse_recursive(array_string):
    if len(array_string) == 0:
        return array_string
    return [array_string[-1]] + inverse_recursive(
        array_string[: len(array_string) - 1]
    )


if __name__ == "__main__":
    word = "ANA"
    print(is_palindrome_recursive(word, 0, len(word) - 1))
    word = "AGUA"
    print(is_palindrome_recursive(word, 0, len(word) - 1))
