from test_helper import run_common_tests, failed, passed, import_task_file, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if placeholder == "":       # TODO: your condition here
        passed()
    else:
        failed()

def test_var_used():
    window = get_answer_placeholders()[0]
    if "porte_monnaie" in window and "produit" in window:
        passed()
    else:
        failed("Veuillez déclarer les variables porte_monnaie et produit")


def test_value():
    file = import_task_file()
    if file.produit == 45:
        passed()
    else:
        failed("Veuillez affecter la variable produit par la valeur 45!")

def test_windows():
    windows = get_answer_placeholders()
    if not "-" in windows[0]:
        failed("Utilisez l'opérateur de soustraction - ")
        return
    window = get_answer_placeholders()[0]
    if "str" in windows[1] and "porte_monnaie" in window[1]:
        passed()
    else:
        failed("Veuillez utiliser la fonction str()")


if __name__ == '__main__':
    run_common_tests()
    # test_answer_placeholders()       # TODO: uncomment test call
    test_var_used()
    test_value()
    test_windows()


