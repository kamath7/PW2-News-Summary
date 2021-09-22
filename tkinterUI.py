import tkinter as tk
from app import summarise_my_article

# print(summarise_my_article("https://www.republicworld.com/india-news/politics/aimims-waris-pathan-condemns-attack-on-owaisis-house-warns-no-one-can-threaten-us.html"))
def lalle():
    url = userUrl.get('1.0', "end").strip()
    my_data = summarise_my_article(url)
    title.config(state="normal")
    summary.config(state="normal")
    sentimentt.config(state="normal")

    title.delete('1.0', 'end')
    title.insert('1.0', my_data['title'])

    summary.delete('1.0', 'end')
    summary.insert('1.0', my_data['summary'])

    sentimentt.delete('1.0', 'end')
    sentimentt.insert('1.0', my_data['sentiment'])

    title.config(state="disabled")
    summary.config(state="disabled")
    sentimentt.config(state="disabled")

root = tk.Tk()
root.title('Your news summary')
root.geometry("1280x720")

tlabel = tk.Label(root, text="Title")
tlabel.pack()
title = tk.Text(root, height=1, width=140)
title.config(state="disabled", bg="#dddddd")
title.pack()

slabel = tk.Label(root, text="Summary")
slabel.pack()
summary = tk.Text(root, height=12, width=140)
summary.config(state="disabled", bg="#dddddd")
summary.pack()

senlabel = tk.Label(root, text="Sentiment of the Article")
senlabel.pack()
sentimentt = tk.Text(root, height=1, width=140)
sentimentt.config(state="disabled", bg="#dddddd")
sentimentt.pack()

userUrlLab = tk.Label(root, text="Enter News URL")
userUrlLab.pack()

userUrl = tk.Text(root, height=1, width=140)
userUrl.pack()

subBtn = tk.Button(root, text="Summarize", command=lalle)
subBtn.pack()

root.mainloop()



