from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout

# Lista e pyetjeve dhe përgjigjeve me 30 pyetje
questions = [
    {"question": "Cili nga operatorët përdoret për krahasim në Python?",
        "answers": ["==", "!=", "<>", "==="], "correct": [0, 1]},
    {"question": "Si shkruhet funksioni për të printuar diçka në ekran?",
        "answers": ["print()", "echo()", "display()"], "correct": [0]},
    {"question": "Si krijohet një listë në Python?",
        "answers": ["{}", "[]", "()", "<>"], "correct": [1]},
    {"question": "Cili është tipi i të dhënave për numrat me presje?",
        "answers": ["int", "float", "str"], "correct": [1]},
    {"question": "Cili është rezultati i 2 ** 3 në Python?",
        "answers": ["6", "8", "9"], "correct": [1]},
    {"question": "Cili funksion përdoret për të marrë input nga përdoruesi?",
        "answers": ["input()", "get()", "read()"], "correct": [0]},
    {"question": "Cili nga më poshtë është një string?",
        "answers": ["123", "'123'", "[123]"], "correct": [1]},
    {"question": "Si i quajmë loops që përdoren në Python?",
        "answers": ["for", "while", "if"], "correct": [0, 1]},
    {"question": "Cili është operatori për ndarje në Python?",
        "answers": ["/", "%", "//"], "correct": [0, 2]},
    {"question": "Cili është funksioni për të konvertuar një numër në string?",
        "answers": ["str()", "int()", "float()"], "correct": [0]},
    {"question": "Cili operator përdoret për ndarje modulo?",
        "answers": ["%", "//", "/"], "correct": [0]},
    {"question": "Si e ndërton një tuple në Python?",
        "answers": ["()", "[]", "{}"], "correct": [0]},
    {"question": "Cili është sinonimi për append() në një listë?",
        "answers": ["push()", "add()", "append()"], "correct": [2]},
    {"question": "Si krijohet një set në Python?",
        "answers": ["()", "[]", "{}"], "correct": [2]},
    {"question": "Si përdoret else me një if statement?",
        "answers": ["else", "elif", "if"], "correct": [0]},
    {"question": "Cili është rezultati i 'hello' * 2?",
        "answers": ["hellohello", "hello2", "hello hello"], "correct": [0]},
    {"question": "Cili është sinonimi për ndarje të plotë në Python?",
        "answers": ["%", "//", "/"], "correct": [1]},
    {"question": "Si i ndan një string në lista?",
        "answers": ["split()", "join()", "slice()"], "correct": [0]},
    {"question": "Cili është funksioni për të bashkuar një listë?",
        "answers": ["append()", "extend()", "join()"], "correct": [2]},
    {"question": "Si të shënojmë një koment në Python?",
        "answers": ["#", "//", "/*"], "correct": [0]},
    {"question": "Si krijohet një fjalor (dictionary)?",
        "answers": ["()", "[]", "{}"], "correct": [2]},
    {"question": "Cili funksion lexon nga një file?",
        "answers": ["open()", "read()", "write()"], "correct": [1]},
    {"question": "Si e përkthen një string në integer?",
        "answers": ["int()", "str()", "float()"], "correct": [0]},
    {"question": "Si i krahasojmë dy lista?",
        "answers": ["==", "!=", "<>"], "correct": [0]},
    {"question": "Cili funksion përdoret për të lexuar një file?",
        "answers": ["open()", "read()", "write()"], "correct": [1]},
    {"question": "Si përdoret funksioni range()?",
        "answers": ["loop", "list", "string"], "correct": [0]},
    {"question": "Si përdoret break në një loop?",
        "answers": ["break", "exit", "stop"], "correct": [0]},
    {"question": "Si përsëriten vlerat e një liste në Python?",
        "answers": ["for", "while", "each"], "correct": [0, 1]},
    {"question": "Cili operator ndan me mbetje?",
        "answers": ["%", "//", "/"], "correct": [0]},
    {"question": "Si e zgjidhim një ekuacion?",
        "answers": ["eq()", "solve()", "math.solve()"], "correct": [1]}
]


class MainMenu(Screen):
    pass


class GameScreen(Screen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.current_question = 0
        self.selected_answers = []
        self.score = 0

    def start_game(self, name):
        if name.strip() == '':
            name = 'Lojtar'
        self.player_name = name
        self.current_question = 0
        self.score = 0
        self.load_question()

    def load_question(self):
        if self.current_question >= len(questions):
            self.end_game()
            return

        question_data = questions[self.current_question]
        self.ids.question_label.text = question_data["question"]

        # Pastrimi i përgjigjeve të mëparshme dhe përzgjedhjes
        self.ids.answer_box.clear_widgets()
        self.selected_answers = []

        # Shfaqja e përgjigjeve me ToggleButton për përzgjedhje të shumëfishta
        grid = GridLayout(cols=2, spacing=10, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))

        for i, answer in enumerate(question_data["answers"]):
            btn = ToggleButton(
                text=answer,
                group=None,  # Lejohet zgjedhja e shumëfishtë
                on_release=lambda btn, i=i: self.toggle_answer(i, btn),
                size_hint=(0.45, None),
                height=40
            )
            grid.add_widget(btn)

        self.ids.answer_box.add_widget(grid)

    def toggle_answer(self, index, btn):
        if btn.state == 'down':
            self.selected_answers.append(index)
            btn.background_color = (0, 0, 1, 1)  # Blu për zgjedhjen
        else:
            self.selected_answers.remove(index)
            # Ngjyrë e bardhë kur zgjidhja hiqet
            btn.background_color = (1, 1, 1, 1)

    def check_selected_answer(self):
        question_data = questions[self.current_question]
        if sorted(self.selected_answers) == sorted(question_data["correct"]):
            self.score += 1
            self.show_dialog("Përgjigje e saktë!", "Ju fituat 1 pikë.")
        else:
            self.show_dialog("Përgjigje e gabuar", "Provo përsëri.")

        # Kalimi në pyetjen tjetër
        self.current_question += 1
        if self.current_question < len(questions):
            self.load_question()
        else:
            self.end_game()

    def show_dialog(self, title, text):
        dialog = MDDialog(
            title=title,
            text=text,
            buttons=[MDRaisedButton(
                text="Ok", on_release=lambda _: dialog.dismiss())]
        )
        dialog.open()

    def end_game(self):
        self.show_dialog(
            "Loja përfundoi!", f"Rezultati juaj është: {self.score}/{len(questions)}"
        )


class KodiMagjikApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_file('main.kv')


if __name__ == '__main__':
    KodiMagjikApp().run()
