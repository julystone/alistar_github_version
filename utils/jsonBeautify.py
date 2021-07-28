import json
from datetime import datetime


# for i in range(782, 824):
#     if i == 800:
#         continue
#     file = f"./json_files/000{i}.json"

def json_beautify(object):
    res = json.dumps(object, sort_keys=True, indent=4, ensure_ascii=True)
    print(res)
    return res


if __name__ == '__main__':
    file = "./json_files/000734.json"
    with open(file, mode='r') as f:
        res = json.load(f)

    out = json_beautify(res)
    with open(f'{file[:-5]}_{datetime.now().strftime("%H%M%S")}.txt', mode='wb+') as f:
        f.write(out)
