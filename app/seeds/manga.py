from app.models import db, Manga, environment, SCHEMA
from sqlalchemy import text

def seed_manga():
    manga_items = [
        Manga(title="One Piece", author="Eiichiro Oda", genre="Adventure, Fantasy", description="Follow Monkey D. Luffy and his crew on their journey to find the legendary One Piece treasure.", cover_image="https://i.postimg.cc/0jKJcv9v/onepiece.jpg"),
        Manga(title="Naruto", author="Masashi Kishimoto", genre="Action, Adventure", description="A young ninja named Naruto Uzumaki strives to become the Hokage.", cover_image="https://i.postimg.cc/kMv5Q2zQ/naruto.jpg"),
        Manga(title="Attack on Titan", author="Hajime Isayama", genre="Action, Drama", description="In a world where humanity is on the brink of extinction, they must fight for survival against titans.", cover_image="https://i.postimg.cc/7hbL9WVp/attackontitan.jpg"),
        Manga(title="My Hero Academia", author="Kohei Horikoshi", genre="Action, Superhero", description="A story set in a world where almost everyone has superpowers, following the young Izuku Midoriya.", cover_image="https://i.postimg.cc/2Spx1XzC/myheroacademia.jpg"),
        Manga(title="Demon Slayer", author="Koyoharu Gotouge", genre="Action, Supernatural", description="Tanjiro Kamado becomes a demon slayer to avenge his family and save his sister from a curse.", cover_image="https://i.postimg.cc/rwSnCvM5/demonslayer.jpg"),
        Manga(title="Dragon Ball", author="Akira Toriyama", genre="Action, Martial Arts", description="Follow Goku and his friends as they defend the Earth from powerful enemies.", cover_image="https://i.postimg.cc/TPy1yZQV/dragonball.jpg"),
        Manga(title="Death Note", author="Tsugumi Ohba", genre="Thriller, Supernatural", description="A high school student gains the power to kill anyone by writing their name in a mysterious notebook.", cover_image="https://i.postimg.cc/qMZpyr9R/deathnote.jpg"),
        Manga(title="Tokyo Ghoul", author="Sui Ishida", genre="Horror, Supernatural", description="Ken Kaneki struggles to live as a half-human, half-ghoul in a world where humans hunt ghouls.", cover_image="https://i.postimg.cc/NMgz0p6R/tokyoghoul.jpg"),
        Manga(title="Fullmetal Alchemist", author="Hiromu Arakawa", genre="Adventure, Fantasy", description="Two brothers use alchemy in their quest to restore their bodies after a failed experiment.", cover_image="https://i.postimg.cc/x18T8vCN/fullmetalalchemist.jpg"),
        Manga(title="One Punch Man", author="ONE", genre="Action, Comedy", description="Saitama, a superhero, defeats his enemies with a single punch but struggles to find a worthy opponent.", cover_image="https://i.postimg.cc/vm1bhXQF/onepunchman.jpg"),
        Manga(title="Hunter x Hunter", author="Yoshihiro Togashi", genre="Action, Adventure", description="Gon Freecss embarks on a journey to become a Hunter and find his missing father.", cover_image="https://i.postimg.cc/c1scWWGm/hunterxhunter.jpg"),
        Manga(title="Bleach", author="Tite Kubo", genre="Action, Supernatural", description="Ichigo Kurosaki, a teenager with the ability to see ghosts, becomes a Soul Reaper.", cover_image="https://i.postimg.cc/dQdnZw3d/bleach.jpg"),
        Manga(title="Sword Art Online", author="Reki Kawahara", genre="Adventure, Sci-Fi", description="Players get trapped in a virtual reality MMORPG where death in the game means death in real life.", cover_image="https://i.postimg.cc/vmLkNq0V/swordartonline.jpg"),
        Manga(title="Black Clover", author="Yūki Tabata", genre="Action, Fantasy", description="Asta, a boy born without magic, dreams of becoming the Wizard King in a world full of magic.", cover_image="https://i.postimg.cc/Z5psspGG/blackclover.jpg"),
        Manga(title="Fairy Tail", author="Hiro Mashima", genre="Adventure, Fantasy", description="Follow the adventures of Natsu Dragneel and his friends in the Fairy Tail guild.", cover_image="https://i.postimg.cc/0NZXbdMj/fairytail.jpg"),
        Manga(title="The Promised Neverland", author="Kaiu Shirai", genre="Mystery, Horror", description="Children at an orphanage uncover the dark secret behind their lives and plan an escape.", cover_image="https://i.postimg.cc/wM3rVsL4/promisedneverland.jpg"),
        Manga(title="JoJo's Bizarre Adventure", author="Hirohiko Araki", genre="Action, Supernatural", description="The Joestar family battles supernatural foes using special powers called Stands.", cover_image="https://i.postimg.cc/Vvrx7Rfz/jojo.jpg"),
        Manga(title="Haikyuu!!", author="Haruichi Furudate", genre="Sports, Drama", description="Hinata Shoyo dreams of becoming a great volleyball player despite his small stature.", cover_image="https://i.postimg.cc/XNxZ9cZC/haikyuu.jpg"),
        Manga(title="Re:Zero", author="Tappei Nagatsuki", genre="Fantasy, Drama", description="Subaru Natsuki is transported to a fantasy world where he has the ability to return to life after death.", cover_image="https://i.postimg.cc/xTzG3fFh/rezero.jpg"),
        Manga(title="Toradora!", author="Yuyuko Takemiya", genre="Romance, Comedy", description="The unlikely friendship between Ryuuji and Taiga helps them in their quest for love.", cover_image="https://i.postimg.cc/25Jfs7Rp/toradora.jpg"),
        Manga(title="Food Wars!", author="Yuto Tsukuda", genre="Cooking, Comedy", description="Young chef Soma enrolls in an elite culinary school to prove his cooking skills.", cover_image="https://i.postimg.cc/VLX8qFLk/foodwars.jpg"),
        Manga(title="Vinland Saga", author="Makoto Yukimura", genre="Historical, Action", description="Thorfinn embarks on a journey to avenge his father and find the legendary Vinland.", cover_image="https://i.postimg.cc/s2nJpdhh/vinlandsaga.jpg"),
        Manga(title="Blue Exorcist", author="Kazue Kato", genre="Action, Supernatural", description="Rin Okumura, the son of Satan, enrolls in a school to become an exorcist.", cover_image="https://i.postimg.cc/ZRvXZ1ft/blueexorcist.jpg"),
        Manga(title="Mob Psycho 100", author="ONE", genre="Action, Supernatural", description="Shigeo 'Mob' Kageyama, a powerful psychic, tries to live a normal life despite his abilities.", cover_image="https://i.postimg.cc/Jzk7Vp7B/mobpsycho.jpg"),
        Manga(title="Chainsaw Man", author="Tatsuki Fujimoto", genre="Action, Horror", description="Denji, a boy with a chainsaw dog demon, becomes a devil hunter to pay off his debt.", cover_image="https://i.postimg.cc/QMw3yLbG/chainsawman.jpg"),
    ]

    for manga in manga_items:
        db.session.add(manga)

    db.session.commit()

def undo_manga():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.manga RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM manga"))

    db.session.commit()
