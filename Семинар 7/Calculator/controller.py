import model
import view
import ask


def button_click():
    numb = ask.numbers()
    if numb == 1:
        value_a = view.get_value_complex(1)
        value_b = view.get_value_complex(2)
        model.init(value_a, value_b)
        act = ask.action()
        result = model.do_it(act)
        view.view_data(result, act)
        return (value_a, value_b, act, result)
    else:
        value_a = view.get_value_fraction(1)
        value_b = view.get_value_fraction(2)
        model.init(value_a, value_b)
        act = ask.action()
        result = model.do_it(act)
        view.view_data(result, act)
        return (value_a, value_b, act, result)
