import tkinter as tk
import webview
import os

class WebPageViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chargement")

        # Appeler la méthode load_web_page directement lors de l'initialisation
        self.load_web_page()

    def load_web_page(self):
        # Récupération du chemin absolu du fichier main.html
        current_directory = os.path.dirname(os.path.abspath(__file__))
        main_html_path = os.path.join(current_directory, "main.html")

        # Création de la fenêtre du navigateur web avec le titre spécifié
        webview.create_window("Chargement", url="file://" + main_html_path)
        webview.start()

if __name__ == "__main__":
    root = tk.Tk()
    app = WebPageViewerApp(root)
    root.mainloop()
