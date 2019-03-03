from collections import defaultdict


def max_composed_number(positive_list_numbers: list):
    _default_data = lambda: defaultdict(_default_data)
    data = _default_data()

    for number in positive_list_numbers:
        number = str(number)
        i = 0
        eval_string = 'data'
        while i < len(number):
            eval_string += f'[number[{str(i)}]]'
            i += 1
        need_str = str(int(number[0]) - 0.5)
        eval_string += '[need_str] = number'
        exec(eval_string)

    def create_chain(input_dict):
        result_dict = {'result_str': ''}

        def _create_chain(input_dict):
            for key in reversed(sorted(input_dict)):
                if key is None or not isinstance(input_dict[key], defaultdict):
                    result_dict['result_str'] += input_dict[key]
                    continue
                _create_chain(input_dict[key])

        _create_chain(input_dict)

        return result_dict['result_str']

    return create_chain(data)


print(max_composed_number([95, 198, 1, 10, 23, 1000]))
print(max_composed_number([859, 858, 857, 85]))
