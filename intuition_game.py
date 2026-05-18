import customtkinter as ctk
from PIL import Image, ImageTk
import random
import os
def get_expected_score(age, gender, level):
    if age < 13:     base = 72
    elif age < 20:   base = 68
    elif age < 35:   base = 65
    elif age < 55:   base = 60
    else:            base = 55
    if gender == "Female": base += 5
    if level  == "Expert": base += 8
    return min(base, 99)
def get_intuition_rank(score):
    if score >= 85:   return "Psychic-Level",     "#FFD700"
    elif score >= 70: return "Strong Intuition",  "#9B59B6"
    elif score >= 55: return "Average Intuition", "#2ECC71"
    else:             return "Below Average",     "#E74C3C"
QUESTIONS = [
    {
        "prompt":      "What animal is hiding behind the bush?",
        "mystery_img": "images/bush.png",
        "reveal_img":  "images/bush_reveal.png",
        "options":     ["Cat", "Hedgehog", "Fox", "Rabbit"],
        "correct":     "Fox",
        "accent":      "#2ECC71",
        "bg":          "#0d1a0d",
    },
    {
        "prompt":      "Is it Day or Night outside?",
        "mystery_img": "images/sky_mystery.png",
        "reveal_img":  "images/sky_reveal_day.png",
        "options":     ["Day", "Night"],
        "correct":     "Day",
        "accent":      "#f5a623",
        "bg":          "#0d0d2e",
    },
    {
        "prompt":      "Winter or Summer?",
        "mystery_img": "images/season_mystery.png",
        "reveal_img":  "images/season_reveal_winter.png",
        "options":     ["Winter", "Summer"],
        "correct":     "Winter",
        "accent":      "#00d4ff",
        "bg":          "#0d1e3a",
    },
    {
        "prompt":      "Who is behind the mysterious door?",
        "mystery_img": "images/door_mystery.png",
        "reveal_img":  "images/door_reveal_ghost.png",
        "options":     ["Ghost", "Wizard", "Robot", "Nobody"],
        "correct":     "Ghost",
        "accent":      "#e94560",
        "bg":          "#1a0d0d",
    },
    {
        "prompt":      "Is the sea Calm or Stormy?",
        "mystery_img": "images/sea_mystery.png",
        "reveal_img":  "images/sea_reveal_calm.png",
        "options":     ["Calm", "Stormy"],
        "correct":     "Calm",
        "accent":      "#0f9b8e",
        "bg":          "#0d1a2e",
    },
    {
        "prompt":      "What is hiding inside the cave?",
        "mystery_img": "images/cave_mystery.png",
        "reveal_img":  "images/cave_reveal_dragon.png",
        "options":     ["Dragon", "Treasure", "Bear", "Nothing"],
        "correct":     "Dragon",
        "accent":      "#f5a623",
        "bg":          "#1a1200",
    },
    {
        "prompt":      "What is inside the magical box?",
        "mystery_img": "images/box_mystery.png",
        "reveal_img":  "images/box_reveal_rabbit.png",
        "options":     ["Rabbit", "Snake", "Dove", "Diamond"],
        "correct":     "Rabbit",
        "accent":      "#FFD700",
        "bg":          "#1a1500",
    },
    {
        "prompt":      "What creature lives in this pond?",
        "mystery_img": "images/pond_mystery.png",
        "reveal_img":  "images/pond_reveal_frog.png",
        "options":     ["Fish", "Frog", "Crocodile", "Duck"],
        "correct":     "Frog",
        "accent":      "#2ECC71",
        "bg":          "#001a0d",
    },
    {
        "prompt":      "What is hiding in the magical tree?",
        "mystery_img": "images/tree_mystery.png",
        "reveal_img":  "images/tree_reveal_fairy.png",
        "options":     ["Owl", "Fairy", "Witch", "Squirrel"],
        "correct":     "Fairy",
        "accent":      "#9B59B6",
        "bg":          "#0d001a",
    },
    {
        "prompt":      "What is emerging from the fog?",
        "mystery_img": "images/fog_mystery.png",
        "reveal_img":  "images/fog_reveal_robot.png",
        "options":     ["Horse", "Car", "Robot", "Wolf"],
        "correct":     "Robot",
        "accent":      "#888888",
        "bg":          "#111111",
    },
]
IMG_W, IMG_H = 660, 280

def load_img(path):
    if os.path.exists(path):
        img = Image.open(path).resize((IMG_W, IMG_H), Image.LANCZOS)
        return ImageTk.PhotoImage(img)
    return None

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Intuition Test")
        self.geometry("740x780")
        self.resizable(False, False)
        self.configure(fg_color="#0d0d1a")
        self.current_page = None
        self.user_data    = {}
        self.show_page("login")

    def show_page(self, name):
        if self.current_page:
            self.current_page.destroy()
        pages = {
            "login":       LoginPage,
            "result_card": ResultCardPage,
            "test":        TestPage,
        }
        self.current_page = pages[name](self)
        self.current_page.pack(fill="both", expand=True)
class LoginPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="#0d0d1a")
        self.master = master


        ctk.CTkLabel(self, text="INTUITION TEST  🧠",
                     font=("Arial", 43, "bold", ),
                     text_color="#00d4ff").pack()
        ctk.CTkLabel(self, text="How strong is your sixth sense?",
                     font=("Arial", 13),
                     text_color="#666666").pack(pady=(2, 20))

        form = ctk.CTkFrame(self, corner_radius=20,
                            fg_color="#12122a",
                            border_color="#00d4ff",
                            border_width=1)
        form.pack(padx=60, pady=5, fill="x")
        ctk.CTkLabel(form, text="Your Name",
                     font=("Arial", 13, "bold"),
                     text_color="#00d4ff",
                     anchor="w").pack(fill="x", padx=30, pady=(25, 3))
        self.name_entry = ctk.CTkEntry(form,
                                       placeholder_text="e.g. Ayat",
                                       height=42, corner_radius=10,
                                       border_color="#00d4ff",
                                       fg_color="#1e1e3a")
        self.name_entry.pack(fill="x", padx=30, pady=(0, 15))
        ctk.CTkLabel(form, text="Your Age",
                     font=("Arial", 13, "bold"),
                     text_color="#00d4ff",
                     anchor="w").pack(fill="x", padx=30, pady=(0, 3))
        self.age_entry = ctk.CTkEntry(form,
                                      placeholder_text="e.g. 20",
                                      height=42, corner_radius=10,
                                      border_color="#00d4ff",
                                      fg_color="#1e1e3a")
        self.age_entry.pack(fill="x", padx=30, pady=(0, 15))
        ctk.CTkLabel(form, text="⚧  Gender",
                     font=("Arial", 13, "bold"),
                     text_color="#00d4ff",
                     anchor="w").pack(fill="x", padx=30, pady=(0, 5))
        self.gender_var = ctk.StringVar(value="Male")
        gf = ctk.CTkFrame(form, fg_color="transparent")
        gf.pack(padx=30, anchor="w", pady=(0, 15))
        for v in ["Male", "Female"]:
            ctk.CTkRadioButton(gf, text=v,
                               variable=self.gender_var, value=v,
                               font=("Arial", 13),
                               fg_color="#00d4ff").pack(side="left", padx=(0, 25))
        ctk.CTkLabel(form, text="Experience Level",
                     font=("Arial", 13, "bold"),
                     text_color="#00d4ff",
                     anchor="w").pack(fill="x", padx=30, pady=(0, 5))
        self.level_var = ctk.StringVar(value="Beginner")
        lf = ctk.CTkFrame(form, fg_color="transparent")
        lf.pack(padx=30, anchor="w", pady=(0, 25))
        for v in ["Beginner", "Expert"]:
            ctk.CTkRadioButton(lf, text=v,
                               variable=self.level_var, value=v,
                               font=("Arial", 13),
                               fg_color="#00d4ff").pack(side="left", padx=(0, 25))

        self.error_label = ctk.CTkLabel(self, text="",
                                        text_color="#ff4444",
                                        font=("Arial", 12))
        self.error_label.pack(pady=5)

        ctk.CTkButton(self,
                      text="Submit & See My Profile",
                      font=("Arial", 15, "bold"),
                      height=50, corner_radius=12,
                      fg_color="#00d4ff",
                      text_color="#000000",
                      hover_color="#00a8cc",
                      command=self.submit).pack(pady=5, padx=60, fill="x")
    def submit(self):
        name = self.name_entry.get().strip()
        age  = self.age_entry.get().strip()
        if not name:
            self.error_label.configure(text="Please enter your name.")
            return
        if not age.isdigit() or not (5 <= int(age) <= 100):
            self.error_label.configure(text="Enter a valid age (5–100).")
            return
        self.master.user_data = {
            "name":   name,
            "age":    int(age),
            "gender": self.gender_var.get(),
            "level":  self.level_var.get(),
        }
        self.master.show_page("result_card")

class ResultCardPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="#0d0d1a")
        self.master = master
        d           = master.user_data
        expected    = get_expected_score(d["age"], d["gender"], d["level"])
        rank, color = get_intuition_rank(expected)

        ctk.CTkLabel(self, text="Your Intuition Profile",
                     font=("Arial", 26, "bold"),
                     text_color="#00d4ff").pack(pady=(30, 10))

        card = ctk.CTkFrame(self, corner_radius=20,
                            fg_color="#12122a",
                            border_color="#00d4ff",
                            border_width=1)
        card.pack(padx=60, pady=5, fill="x")

        emoji = "👦" if d["gender"] == "Male" else "👧"
        av    = ctk.CTkFrame(card, width=80, height=80,
                             corner_radius=40,
                             fg_color="#1e1e3a")
        av.pack(pady=(20, 5))
        av.pack_propagate(False)
        ctk.CTkLabel(av, text=emoji, font=("Arial", 36)).pack(expand=True)

        ctk.CTkLabel(card, text=d["name"],
                     font=("Arial", 20, "bold")).pack()
        ctk.CTkLabel(card,
                     text=f"Age {d['age']}  •  {d['gender']}  •  {d['level']}",
                     font=("Arial", 12),
                     text_color="#888888").pack(pady=(2, 15))

        ctk.CTkFrame(card, height=1,
                     fg_color="#2a2a4a").pack(fill="x", padx=25)

        ctk.CTkLabel(card,
                     text=f"Expected score for age {d['age']}",
                     font=("Arial", 12),
                     text_color="#888888").pack(pady=(15, 0))
        ctk.CTkLabel(card, text=f"{expected}%",
                     font=("Arial", 52, "bold"),
                     text_color="#00d4ff").pack()
        ctk.CTkLabel(card, text=rank,
                     font=("Arial", 17, "bold"),
                     text_color=color).pack(pady=(0, 20))

        ctk.CTkLabel(self,
                     text="Now let's see if you can beat that!",
                     font=("Arial", 13),
                     text_color="#666666").pack(pady=8)
        ctk.CTkButton(self, text="Start the Test!",
                      font=("Arial", 15, "bold"),
                      height=50, corner_radius=12,
                      fg_color="#00d4ff",
                      text_color="#000000",
                      hover_color="#00a8cc",
                      command=lambda: master.show_page("test")
                      ).pack(padx=60, fill="x")
class TestPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="#0d0d1a")
        self.master    = master
        self.round     = 0
        self.score     = 0
        self.questions = random.sample(QUESTIONS, len(QUESTIONS))
        self.total     = len(self.questions)
        self._img_ref  = None
        self.show_question()
    def _placeholder(self, parent, emoji, bg, accent):
        import tkinter as tk
        c = tk.Canvas(parent, width=IMG_W, height=IMG_H,
                      bg=bg, highlightthickness=0)
        c.pack()
        c.create_text(IMG_W // 2, IMG_H // 2,
                      text=emoji, font=("Arial", 80), fill=accent)
        c.create_text(IMG_W // 2, IMG_H // 2 + 70,
                      text="[ Add image to images/ folder ]",
                      font=("Arial", 11), fill="#444444")
    def show_question(self):
        for w in self.winfo_children():
            w.destroy()

        q      = self.questions[self.round]
        accent = q["accent"]
        bg     = q["bg"]
        topbar = ctk.CTkFrame(self, fg_color="#12122a", corner_radius=0)
        topbar.pack(fill="x")
        ctk.CTkLabel(topbar,
                     text=f"Question {self.round + 1} / {self.total}",
                     font=("Arial", 13),
                     text_color="#888888").pack(side="left", padx=20, pady=12)
        ctk.CTkLabel(topbar,
                     text=f"{self.score} pts",
                     font=("Arial", 13, "bold"),
                     text_color="#FFD700").pack(side="right", padx=20)
        pb = ctk.CTkProgressBar(self, height=6,
                                 progress_color=accent,
                                 fg_color="#1e1e3a")
        pb.pack(fill="x")
        pb.set(self.round / self.total)
        ctk.CTkLabel(self, text=q["prompt"],
                     font=("Arial", 20, "bold"),
                     text_color="white",
                     wraplength=680).pack(pady=(18, 8))
        self.img_frame = ctk.CTkFrame(self,
                                      corner_radius=15,
                                      fg_color=bg,
                                      border_color=accent,
                                      border_width=2)
        self.img_frame.pack(padx=30, pady=5)

        photo = load_img(q["mystery_img"])
        if photo:
            import tkinter as tk
            lbl = tk.Label(self.img_frame, image=photo, bd=0, bg=bg)
            lbl.pack()
            self._img_ref = photo
        else:
            self._placeholder(self.img_frame, bg, accent)
        ctk.CTkLabel(self,
                     text="Close your eyes, breathe, then trust your gut!",
                     font=("Arial", 12),
                     text_color="#555555").pack(pady=(8, 4))
        btn_colors = ["#e94560", "#0f9b8e", "#f5a623", "#9b59b6"]
        random.shuffle(btn_colors)
        bf = ctk.CTkFrame(self, fg_color="transparent")
        bf.pack(pady=6)

        for i, opt in enumerate(q["options"]):
            ctk.CTkButton(bf,
                          text=opt,
                          width=max(130, 580 // len(q["options"])),
                          height=54,
                          corner_radius=12,
                          font=("Arial", 16, "bold"),
                          fg_color=btn_colors[i % len(btn_colors)],
                          text_color="white",
                          command=lambda o=opt: self.check_answer(o)
                          ).grid(row=0, column=i, padx=6)

        self.feedback_label = ctk.CTkLabel(self, text="",
                                           font=("Arial", 15, "bold"))
        self.feedback_label.pack(pady=6)
    def check_answer(self, chosen):
        q       = self.questions[self.round]
        correct = q["correct"]

        if chosen == correct:
            self.score += 1
            self.feedback_label.configure(
                text=f"YES! It was {correct}!",
                text_color="#2ECC71")
        else:
            self.feedback_label.configure(
                text=f"Nope! It was {correct}!",
                text_color="#E74C3C")
        for w in self.winfo_children():
            if isinstance(w, ctk.CTkFrame) and w != self.winfo_children()[0]:
                for btn in w.winfo_children():
                    if isinstance(btn, ctk.CTkButton):
                        btn.configure(state="disabled")
        self._show_reveal(q)
        self.round += 1
        self.after(2500, self._next_or_finish)
    def _show_reveal(self, q):
        accent = q["accent"]
        bg     = q["bg"]
        self.img_frame.destroy()
        reveal_frame = ctk.CTkFrame(self,
                                    corner_radius=15,
                                    fg_color=bg,
                                    border_color="#FFD700",
                                    border_width=3)
        reveal_frame.pack(padx=30, pady=5,
                          before=self.feedback_label)

        photo = load_img(q["reveal_img"])
        if photo:
            import tkinter as tk
            lbl = tk.Label(reveal_frame, image=photo, bd=0, bg=bg)
            lbl.pack()
            self._img_ref = photo
        else:
            self._placeholder(reveal_frame, bg, "#FFD700")
        ctk.CTkLabel(reveal_frame,
                     text=f"It was:  {q['correct']}  ",
                     font=("Arial", 16, "bold"),
                     text_color="#FFD700",
                     fg_color="#000000",
                     corner_radius=8).pack(pady=(0, 8))
    def _next_or_finish(self):
        if self.round < self.total:
            self.show_question()
        else:
            self.show_final_score()
    def show_final_score(self):
        for w in self.winfo_children():
            w.destroy()
        d           = self.master.user_data
        expected    = get_expected_score(d["age"], d["gender"], d["level"])
        actual_pct  = int((self.score / self.total) * 100)
        rank, color = get_intuition_rank(actual_pct)

        ctk.CTkLabel(self, text="Final Results",
                     font=("Arial", 30, "bold"),
                     text_color="#00d4ff").pack(pady=(30, 5))

        card = ctk.CTkFrame(self, corner_radius=20,
                            fg_color="#12122a",
                            border_color="#00d4ff",
                            border_width=1)
        card.pack(padx=60, pady=10, fill="x")

        emoji = "👦" if d["gender"] == "Male" else "👧"
        ctk.CTkLabel(card, text=emoji,
                     font=("Arial", 42)).pack(pady=(20, 0))
        ctk.CTkLabel(card, text=d["name"],
                     font=("Arial", 18, "bold")).pack()
        ctk.CTkLabel(card,
                     text=f"{self.score} / {self.total} correct",
                     font=("Arial", 13),
                     text_color="#888888").pack(pady=3)
        ctk.CTkLabel(card, text=f"{actual_pct}%",
                     font=("Arial", 56, "bold"),
                     text_color="#00d4ff").pack()
        ctk.CTkLabel(card, text=rank,
                     font=("Arial", 18, "bold"),
                     text_color=color).pack(pady=3)

        ctk.CTkFrame(card, height=1,
                     fg_color="#2a2a4a").pack(fill="x", padx=25, pady=10)

        diff = actual_pct - expected
        if diff > 0:
            msg, mc = f"You beat expected by {diff}%! Incredible!", "#2ECC71"
        elif diff == 0:
            msg, mc = "Exactly as expected. Perfectly average!", "#F39C12"
        else:
            msg, mc = f"{abs(diff)}% below expected. Train harder!", "#E74C3C"

        ctk.CTkLabel(card, text=msg,
                     font=("Arial", 13, "bold"),
                     text_color=mc,
                     wraplength=500).pack()

        sb = ctk.CTkProgressBar(card, height=12,
                                  progress_color=mc,
                                  fg_color="#1e1e3a",
                                  corner_radius=6)
        sb.pack(fill="x", padx=30, pady=(8, 20))
        sb.set(actual_pct / 100)

        br = ctk.CTkFrame(self, fg_color="transparent")
        br.pack(pady=15)
        ctk.CTkButton(br, text="Try Again",
                      font=("Arial", 13, "bold"),
                      height=45, width=180, corner_radius=12,
                      fg_color="#00d4ff", text_color="#000000",
                      hover_color="#00a8cc",
                      command=lambda: self.master.show_page("test")
                      ).pack(side="left", padx=10)
        ctk.CTkButton(br, text="Home",
                      font=("Arial", 13),
                      height=45, width=140, corner_radius=12,
                      fg_color="#1e1e3a", hover_color="#2a2a4a",
                      command=lambda: self.master.show_page("login")
                      ).pack(side="left", padx=10)
if __name__ == "__main__":
    app = App()
    app.mainloop()