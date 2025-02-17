import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Ponto de entrada da aplicação. Escolha a interface de usuário a ser iniciada."
    )
    parser.add_argument(
        '--ui',
        choices=['flask', 'kivy'],
        default='flask',
        help="Interface de usuário a ser iniciada (default: flask)"
    )
    args = parser.parse_args()

    if args.ui == 'flask':
        from app.ui.flask import main_flask
        main_flask.app.run(debug=True)
    elif args.ui == 'kivy':
        from app.ui.kivy.main_kivy import JogadorKivyApp
        JogadorKivyApp().run()

if __name__ == '__main__':
    main()