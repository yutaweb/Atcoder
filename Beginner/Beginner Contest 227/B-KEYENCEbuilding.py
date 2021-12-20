import math

def main(data):
    N = data[0]
    S = data[1].split(" ")

    count = 0
    for val in S:
        base = math.ceil((int(val) - 3)/7)
        flag = False
        # print(f"val : {val} base : {base}")
        for a in range(1, base + 1):
            # print(f"a : {a}")
            if flag:
                break
            for b in range(1, base + 1):
                # print(f"b : {b}")
                if int(val) == 4*a*b+3*a+3*b:
                    flag = True
                    break

        if not flag:
            count += 1

    print(count)

if __name__ == "__main__":
   data = []
   with open('./input-B.txt') as f:
       for line in f:
           data.append(line.strip('\r\n'))
   main(data)