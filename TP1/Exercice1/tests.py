from test_helper import run_common_tests, failed, passed, import_task_file, get_answer_placeholders


def test_var_used():
    window = get_answer_placeholders()[0]
    if "a" in window and "b" in window:
        passed()
    else:
        failed("Veuillez affecter les variables a et b par leurs valeurs")

def test_somme():
    file = import_task_file()
    if file.resultat == 29.492:
        passed()
    else:
        failed("Résultat erroné!")

def test_windows():
    windows = get_answer_placeholders()
    if not "+" in windows[0]:
        failed("Utilisez l'opérateur +")
        return

def test_affichage():
    window = get_answer_placeholders()[0]
    if "format" in window:
        passed()
    else:
        failed("Utilisez la fonction .format()")

def test_francs_value():
    file = import_task_file()

    if file.francs == file.c*6.55957:
        passed()
    else:
        failed("Résultat erroné!")

if __name__ == '__main__':
    run_common_tests()
    test_var_used()
    test_somme()
    test_windows()
    test_affichage()
    test_francs_value()


