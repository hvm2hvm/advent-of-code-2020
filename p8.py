data = open("input/p8", "rb").read().decode()

input_instructions = [i.strip().split(' ')
                      for i in data.split('\n') if i and i.strip()]
input_instructions = [(ins, int(num)) for ins, num in input_instructions]

def run_ins(instructions):
    visit_count = [0] * len(instructions)

    ip = 0
    acc = 0

    ended = False

    while visit_count[ip] == 0:
        ins, num = instructions[ip]

        new_ip = ip + 1

        if ins == "acc":
            acc += num
        elif ins == "jmp":
            new_ip = ip + num

        visit_count[ip] += 1

        ip = new_ip

        if ip >= len(instructions):
            ended = True
            break

    return ended, acc

ended, acc = run_ins(input_instructions)

print(f"part 1: acc before {'end' if ended else 'break'}: {acc}")

# brute force because I wasn't into it
for ip, (ins, num) in enumerate(input_instructions):
    new_ins = None

    if ins == 'nop':
        new_ins = 'jmp'
    elif ins == 'jmp':
        new_ins = 'nop'

    if new_ins is not None:
        new_instructions = input_instructions[:ip] + [(new_ins, num)] +  input_instructions[ip+1:]
        ended, acc = run_ins(new_instructions)

        if ended:
            print(f"part 2: found ending with acc {acc} at {ip} ({ins} to {new_ins})")
            break

        # print(f"switched {ins} to {new_ins} at addr {ip}: {'ended' if ended else 'looped'} with acc {acc}")
