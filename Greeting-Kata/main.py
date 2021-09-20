import greet
import sys


def array_input_form_cl():
    arguments_list_length = len(sys.argv[1])
    return sys.argv[1][1:arguments_list_length - 1].split(',')


def single_string_input_from_cl():
    return sys.argv[1]


def take_input_from_cl():
    if sys.argv[1][0] == "[":
        input_arguments = array_input_form_cl()
    else:
        input_arguments = single_string_input_from_cl()
    person = greet.Greet(input_arguments)
    print(person.greet())


if __name__ == '__main__':
    take_input_from_cl()
