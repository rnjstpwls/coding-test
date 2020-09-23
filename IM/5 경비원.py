import sys
sys.stdin = open('input.txt')

def search(dir, len):
    if dir == 1:
        return len
    if dir == 2:
        return width + height + width - len
    if dir == 3:
        return total_length - len
    if dir == 4:
        return width + len


width, height = map(int, sys.stdin.readline().split())
total_length = 2 * (width+height)

N = int(sys.stdin.readline())
shops = [tuple(map(int,sys.stdin.readline().split())) for _ in range(N)]

dg_dir, dg_len = map(int, sys.stdin.readline().split())
dg = search(dg_dir, dg_len)
result = 0

for shop in shops:
    shop_dir, shop_len = shop[0], shop[1]
    current = search(shop_dir, shop_len)
    result += min(abs(dg-current), total_length-abs(dg-current))
print(result)