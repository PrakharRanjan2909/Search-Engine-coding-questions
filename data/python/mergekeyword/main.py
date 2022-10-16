import glob

read_files = glob.glob("*.txt")

with open("results.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())

from pathlib import Path

file = Path("results.txt")
file.write_text(
    "\n".join(
        sorted(
            file.read_text().split("\n")
        )
    )
)
# lines_seen = set() # holds lines already seen
# with open("result.txt", "r+") as f:
#     d = f.readlines()
#     f.seek(0)
#     for i in d:
#         if i not in lines_seen:
#             f.write(i)
#             lines_seen.add(i)
#     f.truncate()