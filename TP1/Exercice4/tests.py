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
    if "note1" in window and "note2" in window and "note3" in window:
        passed()
    else:
        failed("Veuillez affecter les variables note1, note2 et note3 par leurs valeurs")


def test_moyenne():
    file = import_task_file()
    if file.moyenne == 14.166666666666666:
        passed()
    else:
        failed("Résultat erroné!")

if __name__ == '__main__':
    run_common_tests()
    # test_answer_placeholders()       # TODO: uncomment test call
    test_var_used()
    test_moyenne()


