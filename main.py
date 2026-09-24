from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.core.clipboard import Clipboard

import os
import sys


# =========================================================
# APP FILE PATH
# =========================================================

def resource_path(filename):
    """
    Finds files correctly when running normally
    and when the app is converted to an EXE.
    """

    if getattr(sys, "frozen", False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(
            os.path.abspath(__file__)
        )

    return os.path.join(
        base_path,
        filename
    )


# =========================================================
# OFFLINE ENGLISH -> LUGANDA DICTIONARY
# =========================================================

dictionary = {
    "hello": "gyebale ko",
    "hi": "gyebale",
    "how are you": "oli otya",
    "i am fine": "ndi bulungi",
    "fine": "bulungi",
    "thank you": "webale",
    "thanks": "webale",
    "welcome": "twanirizza",
    "yes": "yee",
    "no": "nedda",
    "please": "mwattu",
    "sorry": "nsonyiwa",
    "water": "amazzi",
    "food": "emmere",
    "eat": "lya",
    "drink": "nywa",
    "come": "jjangu",
    "go": "genda",
    "love": "okwagala",
    "i love you": "nkwagala",
    "friend": "mukwano",
    "man": "omusajja",
    "woman": "omukazi",
    "child": "omwana",
    "baby": "omwana omuto",
    "house": "ennyumba",
    "school": "ssomero",
    "book": "ekitabo",
    "money": "ssente",
    "work": "emirimu",
    "today": "leero",
    "tomorrow": "enkya",
    "yesterday": "jjjo",
    "morning": "enkya",
    "good morning": "wasuze otya",
    "good night": "sula bulungi",
    "good evening": "osiibye otya",
    "what is your name": "erinnya lyo ani",
    "my name is": "erinnya lyange nze",
    "where are you": "oli wa",
    "i am going": "ngenda",
    "help": "yamba",
    "big": "nnene",
    "small": "tono",
    "god": "katonda",
    "father": "kitaawe",
    "mother": "mmaama"
}


# =========================================================
# COLORS
# =========================================================

BLUE = (0.05, 0.32, 0.62, 1)
DARK_BLUE = (0.03, 0.20, 0.40, 1)

UGANDA_YELLOW = (1.0, 0.75, 0.0, 1)
UGANDA_RED = (0.75, 0.05, 0.05, 1)
UGANDA_BLACK = (0.05, 0.05, 0.05, 1)

WHITE = (1, 1, 1, 1)
LIGHT_BG = (0.94, 0.96, 0.98, 1)

GREEN = (0.05, 0.48, 0.20, 1)
DARK_TEXT = (0.12, 0.12, 0.12, 1)
GREY = (0.45, 0.45, 0.45, 1)


# =========================================================
# APPLICATION
# =========================================================

class TranslatorApp(App):

    # =====================================================
    # APP ICON
    # =====================================================

    icon = resource_path(
        "translator_app_icon.png"
    )

    # =====================================================
    # BUILD APPLICATION
    # =====================================================

    def build(self):

        Window.clearcolor = LIGHT_BG

        # Main container
        main = BoxLayout(
            orientation="vertical",
            padding=dp(15),
            spacing=dp(12)
        )

        # =================================================
        # HEADER
        # =================================================

        header = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            height=dp(160),
            spacing=dp(2)
        )

        # -------------------------------------------------
        # LOGO / IMAGE
        # -------------------------------------------------

        logo = Image(
            source=resource_path(
                "translator_app_icon.png"
            ),
            size_hint_y=None,
            height=dp(65),
            allow_stretch=True,
            keep_ratio=True
        )

        header.add_widget(
            logo
        )

        # -------------------------------------------------
        # TITLE
        # -------------------------------------------------

        title = Label(
            text="🇺🇬  VVDDA TRANSLATOR",
            font_size=dp(23),
            bold=True,
            color=WHITE
        )

        # -------------------------------------------------
        # SUBTITLE
        # -------------------------------------------------

        subtitle = Label(
            text="English  →  Luganda",
            font_size=dp(14),
            color=WHITE
        )

        # -------------------------------------------------
        # OFFLINE STATUS
        # -------------------------------------------------

        offline = Label(
            text="●  100% OFFLINE",
            font_size=dp(11),
            bold=True,
            color=UGANDA_YELLOW
        )

        header.add_widget(
            title
        )

        header.add_widget(
            subtitle
        )

        header.add_widget(
            offline
        )

        # =================================================
        # HEADER BACKGROUND
        # =================================================

        header_container = BoxLayout(
            size_hint_y=None,
            height=dp(160)
        )

        header_background = Button(
            text="",
            background_normal="",
            background_color=BLUE,
            size_hint_y=None,
            height=dp(160)
        )

        header_background.add_widget(
            header
        )

        header_container.add_widget(
            header_background
        )

        main.add_widget(
            header_container
        )

        # =================================================
        # ENGLISH SECTION
        # =================================================

        english_label = Label(
            text="ENGLISH",
            font_size=dp(13),
            bold=True,
            color=DARK_TEXT,
            size_hint_y=None,
            height=dp(25),
            halign="left",
            valign="middle"
        )

        english_label.bind(
            size=lambda obj, size:
            setattr(
                obj,
                "text_size",
                (size[0], None)
            )
        )

        main.add_widget(
            english_label
        )

        # =================================================
        # INPUT
        # =================================================

        self.entry = TextInput(
            hint_text="Type an English word or phrase...",
            multiline=False,
            font_size=dp(18),
            padding=[
                dp(15),
                dp(13)
            ],
            background_color=WHITE,
            foreground_color=DARK_TEXT,
            cursor_color=BLUE,
            size_hint_y=None,
            height=dp(60)
        )

        self.entry.bind(
            text=self.auto_translate
        )

        main.add_widget(
            self.entry
        )

        # =================================================
        # BUTTON ROW
        # =================================================

        button_row = BoxLayout(
            orientation="horizontal",
            spacing=dp(8),
            size_hint_y=None,
            height=dp(52)
        )

        translate_button = Button(
            text="TRANSLATE",
            font_size=dp(15),
            bold=True,
            background_normal="",
            background_color=BLUE,
            color=WHITE
        )

        translate_button.bind(
            on_press=self.translate_now
        )

        clear_button = Button(
            text="CLEAR",
            font_size=dp(14),
            bold=True,
            background_normal="",
            background_color=(0.82, 0.84, 0.87, 1),
            color=DARK_TEXT
        )

        clear_button.bind(
            on_press=self.clear_all
        )

        button_row.add_widget(
            translate_button
        )

        button_row.add_widget(
            clear_button
        )

        main.add_widget(
            button_row
        )

        # =================================================
        # RESULT HEADER
        # =================================================

        result_header = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height=dp(35)
        )

        luganda_label = Label(
            text="LUGANDA",
            font_size=dp(13),
            bold=True,
            color=DARK_TEXT,
            halign="left"
        )

        result_header.add_widget(
            luganda_label
        )

        main.add_widget(
            result_header
        )

        # =================================================
        # RESULT BOX
        # =================================================

        result_container = BoxLayout(
            orientation="vertical",
            padding=dp(15),
            size_hint_y=None,
            height=dp(115)
        )

        self.result = Label(
            text="Your translation will appear here",
            font_size=dp(23),
            bold=True,
            color=GREEN,
            halign="left",
            valign="middle"
        )

        self.result.bind(
            size=lambda obj, size:
            setattr(
                obj,
                "text_size",
                (size[0], None)
            )
        )

        result_container.add_widget(
            self.result
        )

        main.add_widget(
            result_container
        )

        # =================================================
        # COPY BUTTON
        # =================================================

        copy_button = Button(
            text="📋  COPY TRANSLATION",
            font_size=dp(14),
            bold=True,
            background_normal="",
            background_color=GREEN,
            color=WHITE,
            size_hint_y=None,
            height=dp(48)
        )

        copy_button.bind(
            on_press=self.copy_translation
        )

        main.add_widget(
            copy_button
        )

        # =================================================
        # DICTIONARY BUTTON
        # =================================================

        dictionary_button = Button(
            text="📖  VIEW OFFLINE DICTIONARY",
            font_size=dp(14),
            bold=True,
            background_normal="",
            background_color=UGANDA_YELLOW,
            color=UGANDA_BLACK,
            size_hint_y=None,
            height=dp(50)
        )

        dictionary_button.bind(
            on_press=self.show_dictionary
        )

        main.add_widget(
            dictionary_button
        )

        # =================================================
        # STATUS
        # =================================================

        self.status = Label(
            text="Ready • 100% Offline",
            font_size=dp(11),
            color=GREY,
            size_hint_y=None,
            height=dp(28)
        )

        main.add_widget(
            self.status
        )

        return main

    # =====================================================
    # TRANSLATE
    # =====================================================

    def translate_now(
        self,
        instance=None
    ):

        english = (
            self.entry.text
            .lower()
            .strip()
        )

        if not english:

            self.result.text = (
                "Type an English word or phrase"
            )

            self.result.color = (
                0.75,
                0.05,
                0.05,
                1
            )

            self.status.text = (
                "Waiting for input..."
            )

            return

        if english in dictionary:

            self.result.text = (
                dictionary[english]
            )

            self.result.color = GREEN

            self.status.text = (
                "✓ Translation found"
            )

        else:

            self.result.text = (
                "Word not found"
            )

            self.result.color = (
                0.75,
                0.05,
                0.05,
                1
            )

            examples = (
                list(dictionary.keys())[:5]
            )

            self.status.text = (
                "Try: "
                + ", ".join(examples)
                + "..."
            )

    # =====================================================
    # AUTO TRANSLATE
    # =====================================================

    def auto_translate(
        self,
        instance,
        value
    ):

        text = (
            value.strip().lower()
        )

        if text in dictionary:

            self.translate_now()

    # =====================================================
    # CLEAR
    # =====================================================

    def clear_all(
        self,
        instance=None
    ):

        self.entry.text = ""

        self.result.text = (
            "Your translation will appear here"
        )

        self.result.color = GREEN

        self.status.text = (
            "Ready • 100% Offline"
        )

        self.entry.focus = True

    # =====================================================
    # COPY TRANSLATION
    # =====================================================

    def copy_translation(
        self,
        instance=None
    ):

        translation = (
            self.result.text.strip()
        )

        if (
            not translation
            or translation
            == "Your translation will appear here"
            or translation
            == "Word not found"
        ):

            self.status.text = (
                "Nothing to copy"
            )

            return

        Clipboard.copy(
            translation
        )

        self.status.text = (
            "✓ Translation copied"
        )

    # =====================================================
    # SHOW DICTIONARY
    # =====================================================

    def show_dictionary(
        self,
        instance=None
    ):

        layout = BoxLayout(
            orientation="vertical",
            padding=dp(10),
            spacing=dp(10)
        )

        search = TextInput(
            hint_text="Search dictionary...",
            multiline=False,
            font_size=dp(16),
            size_hint_y=None,
            height=dp(50),
            padding=[
                dp(10),
                dp(10)
            ]
        )

        layout.add_widget(
            search
        )

        scroll = ScrollView()

        words_label = Label(
            font_size=dp(15),
            color=DARK_TEXT,
            size_hint_y=None,
            halign="left",
            valign="top"
        )

        def update_words(
            instance=None,
            value=""
        ):

            search_text = (
                search.text
                .lower()
                .strip()
            )

            words = ""

            for english, luganda in sorted(
                dictionary.items()
            ):

                if (
                    not search_text
                    or search_text in english
                    or search_text in luganda.lower()
                ):

                    words += (
                        f"{english}  →  "
                        f"{luganda}\n\n"
                    )

            words_label.text = words

        search.bind(
            text=update_words
        )

        words_label.bind(
            texture_size=lambda instance, value:
            setattr(
                instance,
                "height",
                value[1]
            )
        )

        update_words()

        scroll.add_widget(
            words_label
        )

        layout.add_widget(
            scroll
        )

        close_button = Button(
            text="CLOSE",
            size_hint_y=None,
            height=dp(50),
            background_normal="",
            background_color=BLUE,
            color=WHITE
        )

        layout.add_widget(
            close_button
        )

        popup = Popup(
            title="OFFLINE DICTIONARY",
            content=layout,
            size_hint=(
                0.95,
                0.90
            )
        )

        close_button.bind(
            on_press=popup.dismiss
        )

        popup.open()


# =========================================================
# START APP
# =========================================================

if __name__ == "__main__":

    TranslatorApp().run()