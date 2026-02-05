import gifos
import os
import subprocess

t = gifos.Terminal(750, 500, 15, 15, font_size=15)
t.set_fps(15)

t.gen_text("", 1, count=5)
t.toggle_show_cursor(False)
t.gen_text("MEGHA_OS Modular BIOS v4.44", 1)
t.gen_text("Copyright (C) 2023, \x1b[31mE CORP HOLDINGS LTD\x1b[0m", 2)
t.gen_text(
    "\x1b[94mcreated with GitHub Profile Terminal credit github.com/meghayay\x1b[0m",
    4,
)
t.gen_text("Pentium(tm) M 1.7GHz/600MHz", 6)
t.gen_text(
    "Press \x1b[94mDEL\x1b[0m to enter SETUP, \x1b[94mESC\x1b[0m to cancel Memory Test",
    t.num_rows,
)
for i in range(0, 1048576, 104858):  # 64K Memory
    t.delete_row(7)
    if i < 30000:
        t.gen_text(
            f"Memory Test: {i}", 7, count=2, contin=True
        )  # slow down upto a point
    else:
        t.gen_text(f"Memory Test: {i}", 7, contin=True)
t.delete_row(7)
t.gen_text("Memory Test: 1024MB OK", 7, count=10, contin=True)
t.gen_text("", 11, count=10, contin=True)
t.clear_frame()


bottom_text = "GEMBUDS GLOBAL (2026)"
t.gen_text(
    bottom_text,
    contin=True,
    row_num=t.num_rows - 3,
    col_num=((t.num_cols - len(bottom_text)) // 2),
)
for i in range(0, 30):
    for j in range(2, 22):
        t.delete_row(j)
    with open(f"./globe_frames/frame_{i}.txt") as frame:
        globe = ""
        for line in frame:
            globe = globe + line
        t.gen_text(globe, 2, 19, contin=True)

# lol
global_globe = []
for j in range(2, 22):
    t.delete_row(j)
with open("./globe_frames/frame_29.txt") as frame:
    globe = ""
    for i, line in enumerate(frame):
        globe = globe + line
        global_globe.append(line)
    t.gen_text(globe, 2, 19, contin=True, count=10)

# t.delete_row(t.num_rows - 1)
location_text = "Triangulating location: "
city_text = "New Delhi, India"
t.gen_text(
    location_text,
    row_num=t.num_rows - 2,
    col_num=((t.num_cols - len(location_text) - len(city_text)) // 2),
    contin=True,
)
t.gen_typing_text("....................", t.num_rows - 2, contin=True)
t.delete_row(t.num_rows - 2)
t.gen_text(
    location_text + "....................",
    row_num=t.num_rows - 2,
    col_num=((t.num_cols - len(location_text) - len(city_text)) // 2),
    contin=True,
    count=10,
)
t.delete_row(18)
line_with_melbourne = global_globe[16]
line_with_melbourne = (
    line_with_melbourne[:32] + "\x1b[32m" + "(O)" + "\x1b[0m" + line_with_melbourne[35:]
)
t.gen_text(line_with_melbourne, 18, 2 + 17, contin=True, count=15)

t.delete_row(t.num_rows - 2)
for i in range(3):
    t.delete_row(t.num_rows - 2)
    t.gen_text(
        location_text,
        row_num=t.num_rows - 2,
        col_num=((t.num_cols - len(location_text) - len(city_text)) // 2),
        contin=True,
        count=5,
    )
    t.delete_row(t.num_rows - 2)
    t.gen_text(
        location_text + "\x1b[32mNew Delhi, India\x1b[0m",
        row_num=t.num_rows - 2,
        col_num=((t.num_cols - len(location_text) - len(city_text)) // 2),
        contin=True,
        count=5,
    )

t.delete_row(t.num_rows - 2)
t.gen_text(
    location_text + "\x1b[32mNew Delhi, India\x1b[0m",
    row_num=t.num_rows - 2,
    col_num=((t.num_cols - len(location_text) - len(city_text)) // 2),
    contin=True,
    count=5,
)

log_prmpt = "login: "
uname = "meghayay"
pword_prmpt = "password: "
pword = "***********"
t.delete_row(t.num_rows - 2)
t.gen_text(
    log_prmpt,
    row_num=t.num_rows - 2,
    col_num=23,
    contin=True,
)
t.gen_text(pword_prmpt, row_num=t.num_rows - 1, col_num=20, contin=True, count=10)
t.toggle_show_cursor(True)
# t.toggle_blink_cursor(False)
t.gen_typing_text(uname, t.num_rows - 2, contin=True, speed=0)
t.gen_typing_text(pword, t.num_rows - 1, contin=True, speed=0)
t.clone_frame(5)

# PROMPT AND STATS
t.clear_frame()
t.clone_frame(5)
t.toggle_show_cursor(False)
t.set_prompt("\x1b[33mmeghayay\x1b[0m@gitbox $ ")
t.gen_prompt(1, count=15)
prompt_col = t.curr_col
t.toggle_show_cursor(True)
t.gen_typing_text("\x1b[91mchmo\x1b[0m", 1, contin=True)
t.delete_row(1, prompt_col)
t.gen_text(
    "\x1b[91mchm\x1b[0m\x1b[90mod +x README.sh && ./README.sh\x1b[0m", 1, contin=True
)
t.clone_frame(10)
t.delete_row(1, prompt_col)
t.gen_text("\x1b[32mchmod\x1b[0m +x README.sh && ./README.sh\x1b[0m", 1, contin=True)
t.clone_frame(5)
age = gifos.utils.calc_age(18, 10, 2006)
user_details = f"""
\x1b[30;101mmeghayay@github\x1b[0m
    --------------
\x1b[96mStack:   \x1b[93mFigma, Rust, Typescript, Cpp\x1b[0m
\x1b[96mFocus:   \x1b[93mUX Research, DSA, Frontend, Web3\x1b[0m
\x1b[96mKernel:  \x1b[93mComputer Science\x1b[0m
\x1b[96mUptime:  \x1b[93m{age.years} years, {age.months} months\x1b[0m
\x1b[96mIDE:     \x1b[93mvs_code 0.10\x1b[0m

\x1b[30;101mContact:\x1b[0m
--------------
\x1b[96mEmail:   \x1b[93mmeghagdsc@gmail.com\x1b[0m
\x1b[96mLinkedIn:\x1b[93mjehmegh\x1b[0m
\x1b[96mX:       \x1b[93mjehmegh\x1b[0m
"""

t.gen_text(user_details, 2, count=5, contin=True)
t.gen_prompt(t.curr_row)
t.gen_typing_text(
    "\x1b[32m# Thank you for visiting my profile :D, have a nice day!\x1b[0m",
    t.curr_row,
    contin=True,
)

# Just generate the gif with no loop in the first place to save some trouble
# The t.gen_gif command is just a simple wrapper around this anyway, just added the
# -loop -1 flag

cmd = [
    "ffmpeg", "-hide_banner", "-loglevel", "error", "-r", "15", 
    "-i", "./frames/frame_%d.png", "-loop", "-1", 
    "-filter_complex", "[0:v] split [a][b];[a] palettegen [p];[b][p] paletteuse", 
    "output.gif"
]
subprocess.run(cmd)

# upload the gif to save hella space
image = gifos.utils.upload_imgbb("output.gif", 648000)  # 7.5 days expiration
readme_file_content = rf"""
<div align="justify">
<picture>
    <source media="(prefers-color-scheme: dark)" srcset="{image.url}">
    <source media="(prefers-color-scheme: light)" srcset="{image.url}">
    <img alt="GIFOS_README_TERMINAL" src="{image.url}">
</picture>

<sub><i>Generated automatically using [x0rzavi/github-readme-terminal](https://github.com/x0rzavi/github-readme-terminal)</i></sub>

</div>
    """
with open("README.md", "w") as fp:
    fp.write(readme_file_content)
    print("INFO: README.md file generated")
